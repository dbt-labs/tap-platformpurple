#!/bin/bash

echo "$STITCH_CONFIG" > persist.json
echo "$TAP_CONFIG" > config.json
echo "$CATALOG" > catalog.json

tap-platformpurple -c config.json --catalog catalog.json

{ tap-platformpurple -s state.json -c config.json --catalog catalog.json | target-stitch -c persist.json > state.log; }

tail -n1 state.log > state.json
