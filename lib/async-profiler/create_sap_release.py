'''
Copyright (c) 2024 by SAP SE, Walldorf, Germany.
All rights reserved. Confidential and proprietary.
'''

import argparse
import json
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import utils

def get_release_by_tag(releases, tag):
    for release in releases:
        if release['tag_name'] == tag:
            return release
    return None

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--tag', help='the release tag', metavar='TAG', required=True)
    args = parser.parse_args()

    # upstream release must exist
    upstream_release = utils.github_api_request(api=f'releases/tags/{args.tag}', github_org='async-profiler', repository='async-profiler', raiseError=False)
    if upstream_release is None:
        print(f'Upstream release {args.tag} not found.')
        return -1

    # sap release must not yet exist
    sap_release = utils.github_api_request(api=f'releases/tags/{args.tag}', repository='async-profiler', raiseError=False)
    if sap_release is not None:
        print(f'SAP release {args.tag} already exists.')
        return -1

    # a tag must exist in SAP repository
    sap_tags = utils.github_api_request(api='tags', repository='async-profiler', per_page=100)
    sap_tag_exists = False
    for x in sap_tags:
        if x['name'] == args.tag:
            sap_tag_exists = True

    if sap_tag_exists is False:
        print(f'Tag {args.tag} not found in SAP repository.')
        return -1

    data = json.dumps({"tag_name": args.tag, "name": upstream_release['name'], "body": upstream_release['body']})
    utils.github_api_request(api='releases', repository='async-profiler', data=data, method='POST', add_headers={"Content-Type": "application/json"})

    return 0

if __name__ == "__main__":
    sys.exit(main())
