#!/bin/bash
curl -s https://data-asg.goldprice.org/dbXRates/USD | \
    jq -rM '.items[0] | "${alignr}Gold: $$\(.xauPrice|round)", "${alignr}Silver: $$\(.xagPrice * 100 | round / 100)"'
for asset in BTC ADA ETH; do
    curl -s https://api.blockchain.com/v3/exchange/tickers/${asset}-USD | \
        jq -rM '"${alignr}'${asset}': $$\(.last_trade_price * 100 | round / 100)"'
done
