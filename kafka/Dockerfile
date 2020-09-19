FROM confluentinc/cp-kafka:5.3.1

ENV KAFKA_CONFLUENT_SUPPORT_METRICS_ENABLE "false"
ENV KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR "1"
ENV KAFKA_HEAP_OPTS "-Xmx512m -Xms512m"

ADD create_default_topic.sh .

RUN  apt-get update \
&& apt-get install --force-yes -y net-tools \
&& chmod +x ./create_default_topic.sh

CMD [ "./create_default_topic.sh" ]