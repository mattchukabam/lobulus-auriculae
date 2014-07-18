#!/usr/bin/env bash

curl -XPOST -H 'Content-Type: application/json' http://lobulus-auriculae.herokuapp.com/events -d \
    '{ "ts": "2014-07-17T00:00:00Z", "kind": "test", "id": "test1", "action": "testAction", "value": "testValue" }'
