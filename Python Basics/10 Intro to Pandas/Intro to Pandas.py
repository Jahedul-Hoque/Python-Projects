import pandas as pd
# Series: Collumn of a data frame


Trades = [200, 210, 220, 230, 240]
TradeValues = pd.Series(Trades, index = ["Trader 1", "Trader 2", "Trader 3", "Trader 4", "Trader 5"], dtype="int16")
print (TradeValues, "\n")
# Print TradeValues with a given index of data type Integer that contains 16 bits


print("Trader 2 has traded", TradeValues.loc["Trader 2"], "USDT")
# Locates an index of Trader 2


# Data Frame: Combination of an excel sheet and a database table
NewDataFrame = pd.DataFrame({
    'Name': ['Jad', 'Shanawaz', 'Jim', 'Kevin'],
    'Salary':[35000, 150000, 1000000, 125000],
    'Title': ['EUS Engineer', 'Developer', 'CEO', 'Developer']
})
NewDataFrame = NewDataFrame.set_index("Name")
print(NewDataFrame, "\n")
# Create a data frame and index it to "Name"


DataFrame1 = pd.DataFrame({
"Portfolio Value": [1000, 1500, 2000, 2500]
},index=[1,2,3,4], dtype="int16")
# Creates DataFrame1

DataFrame2 = pd.DataFrame({
"Portfolio Value": [1000, 1500, 2000, 2500]
}, index=[1,2,3,4], dtype="int16")
# Creates DataFrame2

DataFrame3 = DataFrame1+DataFrame2
# Creates DataFrame3 from adding DataFrame1 + DataFrame2


print("Portfolio 1: \n")
print(DataFrame1, "\n")

print("Portfolio 2: \n")
print(DataFrame2, "\n")

print("Portfolio 1 + Portfolio 2: \n")
print(DataFrame3, "\n")
# Adds all the values with matching indexes