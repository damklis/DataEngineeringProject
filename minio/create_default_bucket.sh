#!/bin/sh

echo "Creating default bucket $DEFAULT_BUCKET"

mkdir -p /data/$DEFAULT_BUCKET \
    && minio server /data
