from flask import Flask, request, jsonify
from clickhouse_driver import Client
import re

app = Flask(__name__)

@app.route('/get-tables', methods=['GET'])
def get_tables():
    # Dummy response, replace with actual logic to fetch table names from ClickHouse
    tables = ["table1", "table2", "table3"]
    return jsonify({"tables": tables})

@app.route('/preview-data', methods=['POST'])
def preview_data():
    data = request.json
    source = data.get('source')
    selected_tables = data.get('selectedTables', [])
    join_conditions = data.get('joinConditions', "")

    if source == "ClickHouse":
        preview_result = fetch_joined_data(selected_tables, join_conditions)
        return jsonify(preview_result)
    return jsonify({"error": "Invalid source"})

@app.route('/start-ingestion', methods=['POST'])
def start_ingestion():
    data = request.json
    source = data.get('source')
    selected_tables = data.get('selectedTables', [])
    join_conditions = data.get('joinConditions', "")

    if source == "ClickHouse":
        ingestion_result = execute_join_query(selected_tables, join_conditions)
        return jsonify({"recordsProcessed": ingestion_result})
    return jsonify({"error": "Invalid source"})

def fetch_joined_data(tables, join_conditions):
    # Construct SQL JOIN query based on selected tables and conditions
    query = construct_join_query(tables, join_conditions)
    
    client = Client(host='localhost', port=9000, database='your_db')
    result = client.execute(query)
    
    return result

def execute_join_query(tables, join_conditions):
    # Construct SQL JOIN query and execute ingestion
    query = construct_join_query(tables, join_conditions)
    
    client = Client(host='localhost', port=9000, database='your_db')
    result = client.execute(query)
    
    # Ingestion logic here
    return len(result)

def construct_join_query(tables, join_conditions):
    # Example: JOIN query construction logic
    if len(tables) < 2:
        return "SELECT * FROM {}".format(tables[0])  # Just a single table query
    
    # Construct the JOIN query by combining the tables and conditions
    join_query = " SELECT * FROM " + tables[0]
    for i in range(1, len(tables)):
        join_query += f" JOIN {tables[i]} ON {join_conditions} "
    
    return join_query

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
