# forSCHU


SCHU is the Egyptian god of air.

[https://en.wikipedia.org/wiki/Shu_(Egyptian_god)]

This Project is made to show air-quality with a raspberry pi and the sensor MHZ-14a.

### install python influxDB
 pip instal linfluxdb



### Setup Influx DB with Docker
docker run --rm \
      -e INFLUXDB_DB=db0 \
      -e INFLUXDB_ADMIN_USER=admin -e INFLUXDB_ADMIN_PASSWORD=supersecretpassword \
      -e INFLUXDB_USER=telegraf -e INFLUXDB_USER_PASSWORD=secretpassword \
      -v /home/youruser/influxdbfodler:/var/lib/influxdb \
      influxdb /init-influxdb.sh

#### Start Influx DB as permanent Service
docker run -d --restart always -p 8086:8086 -v /home/youruser/influxdbfodle:/var/lib/influxdb influxdb




## Start grafana as permanent Service (do not remeber how i set it up 1year ago ;))
docker run --restart always -d --name=grafana -p 3000:3000 grafana/grafana

### Set according IP of InfluxDB-docker in Grafana
  docker network inspect bridge | grep elastic -A 5
