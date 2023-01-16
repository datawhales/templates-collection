# PostgreSQL DB 관련
## Docker
- DB 띄우기
    ```bash
    docker run --name postgres-server \
        -e POSTGRES_DB=mydatabase \
        -e POSTGRES_USER=myuser \
        -e POSTGRES_PASSWORD=mypassword \
        -p 5432:5432 \
        -d postgres:14.0
    ```
- DB 내리기
    ```bash
    docker rm -f postgres-server
    ```

## Docker Compose
- `docker-compose.yaml` 작성
- DB 띄우기
    ```bash
    docker compose up -d
    ```
- DB 내리기
    ```bash
    docker compose down -v
    ```

## Helm Chart
- Helm Chart template 디렉토리 생성
    ```bash
    helm create <CHART_NAME>
    ```
- Template 수정
- Helm Chart 실행
    ```bash
    helm install <CHART_NAME> <CHART_PATH>
    ```
- Port-forward
    ```bash
    kubectl port-forward <POD_NAME> 5432:5432
    ```
- DB 접속
    ```bash
    psql -U myuser -h localhost -p 5432 -d mydatabase
    ```
- Helm Chart 실행 중지
    ```bash
    helm uninstall <CHART_NAME>
    ```

## SQL
- Table 생성
    ```bash
    # Run create_table.sql
    psql -h localhost -U myuser -d mydatabase -a -f create_table.sql
    ```
- Table 삭제
    ```bash
    # Run drop_table.sql
    psql -h localhost -U myuser -d mydatabase -a -f drop_table.sql
    ```

## Python Scripts
- Table 생성
    ```bash
    python scripts/create_table.py
    ```
