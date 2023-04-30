## Usefull comands

Update mage in docker

```bash
docker pull mageai/mageai:latest
```

Build Docker Compose

```
docker compose build
```

Build Docker Up / Down

```
docker compose up
docker compose down
```

Connect to docker Containr (Helpful for dbt or other)

```
docker exec -it <CONTAINER_ID> bash 
```

DBT Build

```
dbt build --select --select stg_arrivals.sql stg_departures.sql models/core --var 'is_test_run: false'
```
