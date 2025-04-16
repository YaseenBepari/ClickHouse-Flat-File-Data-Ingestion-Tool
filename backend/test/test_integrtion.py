import unittest
import requests
import os

BASE_URL = "http://localhost:5000/start-ingestion"

class TestDataIngestion(unittest.TestCase):

    def test_clickhouse_to_flatfile(self):
        """Test Case 1: Single ClickHouse table -> Flat File"""
        payload = {
            "source": "ClickHouse",
            "host": "localhost",
            "port": 8443,
            "database": "default",
            "user": "default",
            "jwtToken": "your_token_here",
            "table": "uk_price_paid",
            "selectedColumns": ["price", "postcode", "transfer_date"]
        }

        response = requests.post(BASE_URL, json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        print("ClickHouse to FlatFile:", data)
        self.assertIn("recordsProcessed", data)
        self.assertGreater(data["recordsProcessed"], 0)

    def test_flatfile_to_clickhouse(self):
        """Test Case 2: Flat File -> New ClickHouse Table"""
        payload = {
            "source": "FlatFile",
            "filePath": "uk_price_paid_export.csv",
            "delimiter": ",",
            "targetTable": "uk_price_import",
            "database": "default"
        }

        response = requests.post(BASE_URL, json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        print("FlatFile to ClickHouse:", data)
        self.assertIn("recordsProcessed", data)
        self.assertGreater(data["recordsProcessed"], 0)

    def test_invalid_source(self):
        """Test Case 4: Invalid source"""
        payload = {
            "source": "InvalidSource"
        }

        response = requests.post(BASE_URL, json=payload)
        self.assertEqual(response.status_code, 400)
        print("Invalid source:", response.json())

    def test_data_preview(self):
        """Test Case 5: (Optional) Data Preview"""
        # This assumes a preview endpoint exists
        response = requests.get("http://localhost:5000/preview?source=ClickHouse&table=uk_price_paid&limit=100")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        print("Data Preview:", data)
        self.assertIsInstance(data, list)

if __name__ == '__main__':
    unittest.main()
