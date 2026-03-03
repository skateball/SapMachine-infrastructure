# SapMachine

Fast. Reliable. Open.

## Latest News

{% assign news = site.pages | where: "layout", "news" | sort: "date" | reverse | limit: site.news.max_on_homepage %}
{% for article in news %}
- **{{ article.date | date: "%d.%m.%Y" }}** – [{{ article.title }}]({{ article.url }})
{% endfor %}

[Alle Nachrichten anzeigen](/news/)

<!-- Rest deines Contents -->
