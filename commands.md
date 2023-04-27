## Mage with PostgresSQL

Add secret files (on windows)

Alter the Docker command slightly to work for Windows file path syntax:

```bash
docker run -it -p 6789:6789 ^
    -v "C:\Some Path\dragon\secrets\credentials.json":/home/secrets ^
```

Update mage in docker

```bash
docker pull mageai/mageai:latest

docker build -it mage-server . 

```

```
docker exec -it -p 6789:6789 bash 
```

docker build --platform linux/amd64 --tag my-app:latest .

docker-compose up -d

Update Mage

```bash
docker pull mageai/mageai:latest
```




dbt build --select fact_flights.sql dim_daily_flights_agg.sql dim_monthly_flights_agg.sql dim_monthly_country_agg.sql \

--var 'is_test_run: false'
