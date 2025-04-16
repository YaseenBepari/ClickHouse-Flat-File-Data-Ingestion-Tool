from clickhouse_driver import Client

def clickhouse_ingest(config):
    host = config.get('host')
    port = config.get('port')
    database = config.get('database')
    user = config.get('user')
    jwt_token = config.get('jwtToken')
    selected_tables = config.get('tables', [])
    join_condition = config.get('joinCondition', '')
    selected_columns = config.get('selectedColumns', [])

    # Build the JOIN query
    if len(selected_tables) < 2:
        return "At least two tables are required for a join."

    # Basic JOIN logic (supporting INNER JOIN for simplicity)
    base_table = selected_tables[0]
    query = f"SELECT {', '.join(selected_columns)} FROM {base_table}"

    for table in selected_tables[1:]:
        query += f" INNER JOIN {table} ON {join_condition}"

    # Connect to ClickHouse client
    client = Client(
        host=host,
        port=port,
        database=database,
        user=user,
        password=jwt_token,  # Using JWT token as password
        secure=True
    )

    try:
        result = client.execute(query)

        # Save to CSV
        file_path = f"joined_result.csv"
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(','.join(selected_columns) + '\n')
            for row in result:
                f.write(','.join(map(str, row)) + '\n')

        return len(result)

    except Exception as e:
        return f"Error executing query: {str(e)}"
