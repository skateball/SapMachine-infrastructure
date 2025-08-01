#! /usr/bin/env python3

"""
This script updates the blog article list in the Blogs.md file.

Usage:
    update_blogs.py clone|update

License: MIT
"""
import itertools
import re
import sys
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import List

POSTS_PER_PERSON = 10
TABLE_WITH_HEADER = True


@dataclass
class BlogArticle:
    date: datetime.date
    title: str
    link: str
    categories: List[str]
    """ includes tags """


def get_last_blog_posts_from_wordpress_rss(
        rss_url: str, category_rexep: str, author_regexp: str = ".*",
        limit: int = POSTS_PER_PERSON) -> \
        List[BlogArticle]:
    """
    Get the last blog posts from the wordpress RSS feed.
    """
    import feedparser

    feed = feedparser.parse(rss_url)
    posts = []
    for entry in feed.entries[:limit]:
        # make first letter of every word uppercase
        categories_and_tags = [t["term"] for t in entry.tags]
        authors = [a["name"] for a in entry["authors"]]
        if (not any(re.match(category_rexep, c) for c in
                    categories_and_tags) or not any(
            re.match(author_regexp, a) for a in authors)):
            continue
        cats = sorted(list(set(categories_and_tags)))
        # remove duplicates, ignore case
        cats = [x[0] for x in
                itertools.groupby(cats, lambda x: x.lower())]
        posts.append(BlogArticle(date=datetime.fromtimestamp(
            time.mktime(entry.published_parsed)),
            title=entry["title"], link=entry["link"],
            categories=cats))

    return posts


posts = {"Johannes": get_last_blog_posts_from_wordpress_rss(
    "https://mostlynerdless.de/feed/", "Java.*|OpenJDK|eBPF"), }


def create_blog_posts_md(posts: List[BlogArticle]) -> str:
    """
    Create the markdown for the blog posts.

    Blog Posts are stored in a table of the form:

    Date | Title | Categories and tags
    -----|-------|-------
    Feb 12, 2023 | [Title](Link) | Cat1, Cat2, Tag1, Tag2

    The table doesn't have a header if TABLE_WITH_HEADER is False.
    """
    if TABLE_WITH_HEADER:
        header = "Date | Title | Categories and Tags|\n"
        header += "-----|-------|-------|\n"
    else:
        header = ""
    rows = []
    for post in posts:
        date = post.date.strftime("%b %d, %Y")
        title = f"[{post.title}]({post.link})"
        categories = ", ".join(post.categories)
        rows.append(f"{date} | {title} | {categories}|")
    return header + "\n".join(rows)


def update_blogs_md(blogs_file: Path) -> bool:
    """
    Update the Blogs.md file with the latest blog posts and
    return false if the file was not changed.

    The section for every person (like "Johannes") starts with
    `<!-- start PERSON -->` and ends with the nearest `<!-- end -->`

    It replaces the old content with the new content and write the
    file back to disk if it was changed.
    """
    blogs_md = blogs_file.read_text()
    for person, persons_posts in posts.items():
        start = f"<!-- start {person} -->"
        end = "<!-- end -->"
        start_pos = blogs_md.find(start)
        end_pos = blogs_md.find(end, start_pos)
        if start_pos == -1 or end_pos == -1:
            print(
                f"Could not find start or end of {person} blog posts")
            continue
        new_content = create_blog_posts_md(persons_posts)
        blogs_md = (blogs_md[:start_pos] +
                    start + "\n" + new_content + "\n" +
                    blogs_md[end_pos:])
    if blogs_file.read_text() == blogs_md:
        return False
    blogs_file.write_text(blogs_md)
    return True


if __name__ == '__main__':

    # first command line argument is "clone" or "update"
    if len(sys.argv) != 2 or sys.argv[1] not in ("clone", "update"):
        print("Usage: update_blogs.py clone|update")
        sys.exit(1)

    if sys.argv[1] == "clone":
        # clone the repository from https://github.com/SAP/SapMachine.wiki.git
        # into a temp folder, call update_blogs_md and delete the temp folder
        # commit and push the changes if update_blogs_md returns True
        import tempfile
        import shutil
        import subprocess

        temp_dir = tempfile.mkdtemp()

        subprocess.check_call(
            f"git clone https://github.com/SAP/SapMachine.wiki.git " + temp_dir,
            shell=True)

        subprocess.check_call(
            f"git -C {temp_dir} config user.name \"SapMachine Bot\"",
            shell=True)

        update_blogs_md(Path(temp_dir) / "Blogs.md")
        subprocess.check_call("git -C " + temp_dir + " add Blogs.md",
                              shell=True)
        subprocess.check_call(
            "git -C " + temp_dir + " commit -m \"Update Blogs.md\"",
            shell=True)
        subprocess.check_call("git -C " + temp_dir + " push origin master",
                              shell=True)
        shutil.rmtree(temp_dir)
    else:
        # update the Blogs.md file in the current directory
        changed = update_blogs_md(
            Path(__file__).parent.parent / "Blogs.md")
        if changed:
            print(
                "Blogs.md was changed. Please commit and push the changes.")
