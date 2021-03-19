# Steeltoe Locust

## Setup

```sh
$ pipenv install
```
## Samples

```
# using command line arguments
$ pipenv run locust -H https://start-staging.steeltoe.io -u 1000 -r 10

# using config file
$ pipenv run locust --config steeltoe-staging.conf

# override a config setting
$ pipenv run locust --config steeltoe-staging.conf --run-time 1m

# run in Docker
$ docker run -p8089:8089 -v $PWD:/mnt/locust locustio/locust \
    --locustfile /mnt/locust/locustfile.py \

# use docker-compose to run a controller and 2 workers
$ docker-compose up --scale worker=2
```

Locally running locust swarm can be viewed at http://localhost:8089
