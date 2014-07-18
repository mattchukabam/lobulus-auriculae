#!/usr/bin/env bash

source .env
_AWS_KEY=$_AWS_KEY _AWS_SECRET=$_AWS_SECRET python listen.py
