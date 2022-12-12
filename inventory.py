#!/bin/python
import json

inventory = {}

inventory["webservers"] = {
    "hosts": ["server1.example.com"],
    "vars": {
        "package": "httpd",
        "service": "httpd"
    }
}

inventory["databases"] = {
    "hosts": ["server2.example.com"],
    "vars": {
        "package": "mariadb-server",
        "service": "mariadb"
    }
}

print(json.dumps(inventory, indent=2))
