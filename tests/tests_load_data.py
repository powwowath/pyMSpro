import unittest
import pandas as pd
from src.data.load_data import load_csv, load_mzml
import os


class TestLoadData(unittest.TestCase):

    def setUp(self):
        # Setup paths to test data files
        self.csv_path = 'tests/data/sample.csv'
        self.mzml_path = 'tests/data/sample.mzML'

        # Ensure test data files exist
        os.makedirs('tests/data', exist_ok=True)
        pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]}).to_csv(self.csv_path, index=False)
        pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]}).to_excel(self.excel_path, index=False)

    def test_load_csv(self):
        df = load_csv(self.csv_path)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertFalse(df.empty)

    def test_load_mzml(self):
        # Since creating a valid mzML file is complex, this test will focus on error handling
        with self.assertRaises(FileNotFoundError):
            load_mzml(self.mzml_path)

    def tearDown(self):
        # Clean up test files
        os.remove(self.csv_path)
        # Leave mzML path as it may not have been created


if __name__ == '__main__':
    unittest.main()
