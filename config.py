import os
import boto

STREAM_NAME = 'mchu-stomach-1-Stream1-12MR18JXOILTG'
PARTITION_KEY = 'partitionKey-1'
SHARD_ID = 'shardId-000000000000'

iter_type_at = 'AT_SEQUENCE_NUMBER'
iter_type_after = 'AFTER_SEQUENCE_NUMBER'
iter_type_trim = 'TRIM_HORIZON'
iter_type_latest = 'LATEST'

aws_key = os.environ['_AWS_KEY']
aws_secret = os.environ['_AWS_SECRET']
kinesis = boto.connect_kinesis(aws_key, aws_secret)
