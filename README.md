# forSCHU

### install python influxDB
 pip instal linfluxdb



### Setup Influx DB with Docker
docker run --rm \
      -e INFLUXDB_DB=db0 \
      -e INFLUXDB_ADMIN_USER=admin -e INFLUXDB_ADMIN_PASSWORD=supersecretpassword \
      -e INFLUXDB_USER=telegraf -e INFLUXDB_USER_PASSWORD=secretpassword \
      -v /home/youruser/influxdbfodler:/var/lib/influxdb \
      influxdb /init-influxdb.sh

### Set according IP of InfluxDB-docker in Grafana
  docker network inspect bridge | grep elastic -A 5
