#Stock Data Visualizer Scrum Team 13
from datetime import date
from datetime import datetime
import pygal
import requests

def validateSymbol(symbol):
    if symbol.isalpha() == True and len(symbol) >= 1 and len(symbol) <= 7 and symbol.isupper() == True:
        return True
    else:
        return False

def validateChartType(type):
    if type != 1 and type != 2: 
        return False 
    else:
        return True

def validateTimeSeries(timeSeries):
    if timeSeries > 0 and timeSeries < 5:
        return True
    else:
        return False

def validateDate(date_string):
    date_obj = datetime.strptime(date_string, '%Y-%m-%d')
    return date_obj


i = True
while i:
    # Print Title
    print("Stock Data Visualizer")
    print("-----------------------\n")

    # P1. Get Stock Symbol
    validSymbol = False
    while validSymbol == False:
        stockSymbol = input("Enter the stock symbol you are looking for: ")
        validSymbol = validateSymbol(stockSymbol)
        if(validSymbol == False):
            print("Invalid symbol try again")

    # P2. Get Chart Type
    validType = False
    while validType == False:
        print("\nChart Types")
        print("-------------")
        print("1. Bar")
        print("2. Line\n")
        chartType = int(input("Enter the chart type you want (1, 2): "))
        validType = validateChartType(chartType)
        if validType == False: print("Enter a 1 or 2 for chart type")

    # P3. Get Time Series
    validTimeSeries = False
    while validTimeSeries == False:
        print("Select the Time Series of the chart you want to Generate: ")
        print("1. Intraday")
        print("2. Daily")
        print("3. Weekly")
        print("4. Monthly")
        time_series = int(input("\nEnter time series option (1, 2, 3, 4): "))
        validTimeSeries=validateTimeSeries(time_series)
        if validTimeSeries == False:
            print("Error: Please enter a value within the range.")

    # P4. Get Start Date
    n = True
    while n:
        userDate = input('Enter a date formatted as YYYY-MM-DD: ')
        try:
            finalDate = validateDate(userDate)
        except:
            print("You must enter a properly formatted date.")
        if finalDate != None:
            n = False


    # P5. Get End Date
    x = True
    while x:
        endDate = input("Enter the end Date formatted as YYYY-MM-DD: ")
        try:
            finalEndDate = validateDate(endDate)
        except:
            print("You must enter a properly formatted date.")
        if finalEndDate != None and finalEndDate > finalDate:
            x = False
        else:
            print("The end date must take place after the beginning date.")


    # P6. Generate Graph
    format = "%Y-%m-%d %H:%M:%S"
    startDate_dt = datetime.strptime(str(finalDate), format)
    endDate_dt = datetime.strptime(str(finalEndDate), format)
    dateKeyList = []
    openValues = []
    highValues = []
    lowValues = []
    closeValues = []

    if chartType == 1:
        chart = pygal.Bar()
    else:
        chart = pygal.Line()
    chart.title = 'Stock Data for ' + stockSymbol + ': ' + str(finalDate) + ' to ' + str(finalEndDate)
    if time_series == 1:
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='+stockSymbol+'&interval=60min&outputsize=full&apikey=TF2MH4AQ3EMH4GZL'
    elif time_series == 2:
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol='+stockSymbol+'&outputsize=full&apikey=TF2MH4AQ3EMH4GZL'
    elif time_series == 3:
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol='+stockSymbol+'&outputsize=full&apikey=TF2MH4AQ3EMH4GZL'
    else:
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol='+stockSymbol+'&outputsize=full&apikey=TF2MH4AQ3EMH4GZL'
    r = requests.get(url)
    data = r.json()
    data.pop('Meta Data')
    dateList = data.values()
    for dictionary in dateList:
        for dateKey in dictionary:
            if time_series == "1":
                dateKey_dt = datetime.strptime(dateKey, "%Y-%m-%d %H:%M:%S")
            else:
                dateKey_dt = datetime.strptime(dateKey, "%Y-%m-%d")  
                
            if startDate_dt <= dateKey_dt <= endDate_dt:  
                dateKeyList.append(dateKey)
                openValues.append(float(dictionary[dateKey]['1. open']))
                highValues.append(float(dictionary[dateKey]['2. high']))
                lowValues.append(float(dictionary[dateKey]['3. low']))
                closeValues.append(float(dictionary[dateKey]['4. close']))
    dateKeyList.reverse()
    openValues.reverse()
    highValues.reverse()
    lowValues.reverse()
    closeValues.reverse()
    chart.x_labels = map(str, dateKeyList)
    chart.add('Open', openValues)
    chart.add('High',  highValues)
    chart.add('Low',      lowValues)
    chart.add('Close',  closeValues)
    chart.render_in_browser()

    # Ask to repeat
    choice = input("\nWould you like to view more stock data? Press 'y' to continue: ")
    if(choice != 'y'):
        i = False