FROM minio/minio:RELEASE.2021-01-08T21-18-21Z

COPY create_default_bucket.sh .

RUN chmod +x ./create_default_bucket.sh

ENTRYPOINT [ "./create_default_bucket.sh" ]