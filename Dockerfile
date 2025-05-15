FROM docker.elastic.co/logstash/logstash:7.17.9
RUN bin/logstash-plugin install logstash-output-mongodb
RUN bin/logstash-plugin install logstash-output-elasticsearch
