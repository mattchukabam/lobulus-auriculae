#!/usr/bin/env bash

echo "Before:"
heroku config
echo ""

for line in `cat .env`; do
  heroku config:set $line
done

echo "After:"
heroku config
echo ""
