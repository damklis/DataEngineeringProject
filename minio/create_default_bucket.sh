#!/bin/sh

echo "Creating default bucket $DEFAULT_BUCKET"

mkdir -p /data/$DEFAULT_BUCKET \
&& /usr/bin/minio server /data