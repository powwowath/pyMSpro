import unittest
import pandas as pd
from src.data.preprocess_data import clean_data, normalize_data, filter_data


class TestPreprocessData(unittest.TestCase):

    def setUp(self):
        data = {
            'A': [1, 2, 3, None, 5],
            'B': [5, None, None, 4, 5],
            'C': [10, 20, 30, 40, 50]
        }
        self.df = pd.DataFrame(data)

    def test_clean_data(self):
        df_cleaned = clean_data(self.df)
        self.assertFalse(df_cleaned.isnull().values.any())
        self.assertEqual(len(df_cleaned), 2)  # After removing rows with NaN and duplicates

    def test_normalize_data_zscore(self):
        df_normalized = normalize_data(self.df.fillna(0), method='z-score')
        self.assertAlmostEqual(df_normalized.mean().mean(), 0, places=1)
        self.assertAlmostEqual(df_normalized.std().mean(), 1, places=1)

    def test_normalize_data_minmax(self):
        df_normalized = normalize_data(self.df.fillna(0), method='min-max')
        self.assertAlmostEqual(df_normalized.min().min(), 0, places=1)
        self.assertAlmostEqual(df_normalized.max().max(), 1, places=1)

    def test_filter_data(self):
        df_filtered = filter_data(self.df, threshold=5)
        self.assertTrue((df_filtered.dropna().min().min() >= 5))


if __name__ == '__main__':
    unittest.main()
