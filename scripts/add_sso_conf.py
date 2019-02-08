#!/usr/bin/python3

import json

with open("/etc/ssowat/conf.json.persistent", "r", encoding='utf-8') as jsonFile:
    try:
        data = json.load(jsonFile)
    except:
        print("File /etc/ssowat/conf.json.persistent corrupt, make a new file")
        data = {}
    if not "skipped_urls" in data:
        data["skipped_urls"] = []
    data["skipped_urls"] = list(set(data["skipped_urls"]) | set(["/Microsoft-Server-ActiveSync", "/principals"]))

with open("/etc/ssowat/conf.json.persistent", "w", encoding='utf-8') as jsonFile:
    jsonFile.write(json.dumps(data, indent=4, sort_keys=True))
