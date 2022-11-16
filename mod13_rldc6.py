import unittest
import datetime

class StockTest(unittest.TestCase):

    symbol = input("Enter stock symbol: ")
    chartType = input("Enter chart type: ")
    timeSeries = input("Enter time series: ")
    startDate = input("Enter start date YYYY-MM-DD: ")
    endDate = input("Enter end date YYYY-MM-DD: ")

    def test_symbol(self):
        self.assertTrue(self.symbol.isupper())
        self.assertTrue(self.symbol.isalpha())
        self.assertTrue(len(self.symbol) >= 1)
        self.assertTrue(len(self.symbol) <= 7)

    def test_type(self):
        self.assertTrue(self.chartType.isnumeric())
        self.assertTrue(len(self.chartType) == 1)
        self.assertTrue(self.chartType == "1" or self.chartType == "2")

    def test_time(self):
        self.assertTrue(self.timeSeries.isnumeric())
        self.assertTrue(len(self.timeSeries) == 1)
        self.assertTrue(self.timeSeries == "1" or self.timeSeries == "2" or self.timeSeries == "3" or self.timeSeries == "4")

    def test_StartDate(self):
        self.assertIsInstance(datetime.datetime.strptime(self.startDate, "%Y-%m-%d"), datetime.datetime)
        
    def test_EndDate(self):
        self.assertIsInstance(datetime.datetime.strptime(self.endDate, "%Y-%m-%d"), datetime.datetime)

if __name__ == '__main__':
    unittest.main()