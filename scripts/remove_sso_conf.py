#!/usr/bin/python3

import json

with open("/etc/ssowat/conf.json.persistent", "r", encoding='utf-8') as jsonFile:
    data = json.load(jsonFile)
    data["skipped_urls"].remove("/Microsoft-Server-ActiveSync")
    data["skipped_urls"].remove("/principals")

with open("/etc/ssowat/conf.json.persistent", "w", encoding='utf-8') as jsonFile:
    jsonFile.write(json.dumps(data, indent=4, sort_keys=True))
