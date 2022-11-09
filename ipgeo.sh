#!/bin/bash
ip=$(dig +short myip.opendns.com @resolver1.opendns.com)
curl -s https://ipinfo.io | jq -rM '.ip,.hostname,"\(.city), \(.region), \(.country)",.org'

