import unittest
import StockDataVisualizer
from datetime import datetime

class StockTest(unittest.TestCase):

    def setUp(self):
        self.goodSymbol = "GOOGL"
        self.badSymbolLength = "TESTTOOLONG"
        self.badSymbolCap = "testnocap"
        self.badSymbolNum = "1234"
        self.goodChartTypeOne = 1
        self.goodChartTypeTwo = 2
        self.badChartType = 3
        self.goodTimeSeriesOne = 1
        self.goodTimeSeriesTwo = 2
        self.goodTimeSeriesThree = 3
        self.goodTimeSeriesFour = 4
        self.badTimeSeries = 5
        self.badStartDate = "20212101-12121"
        self.badEndDate = "12345-1333-1111111111"
        self.goodStartDate = datetime.strptime("2021-01-01", '%Y-%m-%d')
        self.goodEndDate = datetime.strptime("2021-02-02", '%Y-%m-%d')


    def test_symbol(self):
        self.assertTrue(StockDataVisualizer.validateSymbol(self.goodSymbol))
        self.assertFalse(StockDataVisualizer.validateSymbol(self.badSymbolLength))
        self.assertFalse(StockDataVisualizer.validateSymbol(self.badSymbolCap))
        self.assertFalse(StockDataVisualizer.validateSymbol(self.badSymbolNum))

    def test_type(self):
        self.assertTrue(StockDataVisualizer.validateChartType(self.goodChartTypeOne))
        self.assertTrue(StockDataVisualizer.validateChartType(self.goodChartTypeTwo))
        self.assertFalse(StockDataVisualizer.validateChartType(self.badChartType))

    def test_time(self):
        self.assertTrue(StockDataVisualizer.validateTimeSeries(self.goodTimeSeriesOne))
        self.assertTrue(StockDataVisualizer.validateTimeSeries(self.goodTimeSeriesTwo))
        self.assertTrue(StockDataVisualizer.validateTimeSeries(self.goodTimeSeriesThree))
        self.assertTrue(StockDataVisualizer.validateTimeSeries(self.goodTimeSeriesFour))
        self.assertFalse(StockDataVisualizer.validateTimeSeries(self.badTimeSeries))

    def test_StartDate(self):
        testStartDate = StockDataVisualizer.validateDate("2021-01-01")
        self.assertEqual(self.goodStartDate, testStartDate)
        self.assertRaises(Exception, StockDataVisualizer.validateDate, self.badStartDate)
        
    def test_EndDate(self):
        testEndDate = StockDataVisualizer.validateDate("2021-02-02")
        self.assertEqual(self.goodEndDate, testEndDate)
        self.assertRaises(Exception, StockDataVisualizer.validateDate, self.badEndDate)

if __name__ == '__main__':
    unittest.main()