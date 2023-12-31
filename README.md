# Django-ElasticSearch
A simple app runs based on django framework and search engine of elasticsearch.

## 1. ElasticSearch Setup. <br>
we will setup elasticsearch using docker container for simplicity but you can do whatever you want on how installing it. <br>
    <br>
Following the offical documentations on link https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html 
    
1.1. We need to make sure that docker is installed on the machine. if so then we will start docker decktop. and if not so we need to download docker and installed following that link. https://docs.docker.com/

1.2. We will pull the docker container using the following command.
~~~
docker pull docker.elastic.co/elasticsearch/elasticsearch:8.11.3
~~~  

1.3. Create a docker network. 
~~~
docker network create elastic
~~~

1.4. Run the container on network **elastic** and port **9200** and limit the memory to 1GB.
~~~
docker run --name es01 --net elastic -p 9200:9200 -it -m 1GB docker.elastic.co/elasticsearch/elasticsearch:8.11.3
~~~

1.5. Once it started it will give you username and password in the terminal so you can use them to access the ElasticSearch Instance.
~~~
✅ Elasticsearch security features have been automatically configured!
✅ Authentication is enabled and cluster connections are encrypted.

ℹ️  Password for the USERNAME user (reset with `bin/elasticsearch-reset-password -u elastic`):
  PASSWORD

ℹ️  HTTP CA certificate SHA-256 fingerprint:
  4d55d25e86285f009861d8224772985ffd23720dda972aa76df73cddafa53411

ℹ️  Configure Kibana to use this cluster:
• Run Kibana and click the configuration link in the terminal when Kibana starts.
• Copy the following enrollment token and paste it into Kibana in your browser (valid for the next 30 minutes):
  eyJ2ZXIiOiI4LjExLjMiLCJhZHIiOlsiMTcyLjE4LjAuMjo5MjAwIl0sImZnciI6IjRkNTVkMjVlODYyODVmMDA5ODYxZDgyMjQ3NzI5ODVmZmQyMzcyMGRkYTk3MmFhNzZkZjczY2RkYWZhNTM0MTEiLCJrZXkiOiJCNDhzd0l3QkRFN3FRV0dBS3RsVjo1dlpjQXB1MlFGZWRySTcwbDhPQWtBIn0=

ℹ️ Configure other nodes to join this cluster:
• Copy the following enrollment token and start new Elasticsearch nodes with `bin/elasticsearch --enrollment-token <token>` (valid for the next 30 minutes):
  eyJ2ZXIiOiI4LjExLjMiLCJhZHIiOlsiMTcyLjE4LjAuMjo5MjAwIl0sImZnciI6IjRkNTVkMjVlODYyODVmMDA5ODYxZDgyMjQ3NzI5ODVmZmQyMzcyMGRkYTk3MmFhNzZkZjczY2RkYWZhNTM0MTEiLCJrZXkiOiJCbzhzd0l3QkRFN3FRV0dBS3RsVjpKQ2o5U2ktTVF3bUVwVHZzZGFPcTFnIn0=

  If you're running in Docker, copy the enrollment token and run:
  `docker run -e "ENROLLMENT_TOKEN=<token>" docker.elastic.co/elasticsearch/elasticsearch:8.11.3`
~~~

1.6. You can use the browser to test it`s working correcly or using **elasticvue** GUI to help you with some more options.
https://elasticvue.com/




