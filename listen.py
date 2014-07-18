#!/usr/bin/env python

from __future__ import print_function
import sys

import json
import time
import datetime

import boto
from boto.kinesis.exceptions import ProvisionedThroughputExceededException

from config import *

def listening():
    response = kinesis.get_shard_iterator(STREAM_NAME, SHARD_ID, iter_type_latest)

    next_iterator = response['ShardIterator']

    while True:
        try:
            print('.', end='')

            response = kinesis.get_records(next_iterator)

            if len(response['Records']) > 0:
                records = '\n'.join(
                    [ d['Data'].strip() for d in response['Records'] ]
                )
                print('\n' + records)

            next_iterator = response['NextShardIterator']

            sys.stdout.flush()
            time.sleep(2)
        except ProvisionedThroughputExceededException as ptee:
            print(ptee.message)
            time.sleep(5)

if __name__ == '__main__':
    listening()
