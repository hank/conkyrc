#!/bin/bash
ip=$(dig +short myip.opendns.com @resolver1.opendns.com)
curl -s https://ipinfo.io | jq -rM '.ip,.hostname // "No Reverse DNS","\(.city), \(.region), \(.country)",.org'

