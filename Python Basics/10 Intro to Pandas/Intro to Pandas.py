import pandas as pd

# Creating a Pandas Series (1D data structure)
Trades = [200, 210, 220, 230, 240]
TradeValues = pd.Series(Trades, index=["Trader 1", "Trader 2", "Trader 3", "Trader 4", "Trader 5"], dtype="int16")
print(TradeValues, "\n")


# Retrieving specific trade data using .loc[]
print("Trader 2 has traded", TradeValues.loc["Trader 2"], "USDT")


# Creating a DataFrame (structured table format)
NewDataFrame = pd.DataFrame({
    'Name': ['Jad', 'Shanawaz', 'Jim', 'Kevin'],
    'Salary': [35000, 150000, 1000000, 125000],
    'Title': ['EUS Engineer', 'Developer', 'CEO', 'Developer']
})
NewDataFrame = NewDataFrame.set_index("Name")
print(NewDataFrame, "\n")


# Creating two Portfolio DataFrames
DataFrame1 = pd.DataFrame({"Portfolio Value": [1000, 1500, 2000, 2500]}, index=[1,2,3,4], dtype="int16")
DataFrame2 = pd.DataFrame({"Portfolio Value": [1000, 1500, 2000, 2500]}, index=[1,2,3,4], dtype="int16")

# Adding Portfolio Values with matching indexes
DataFrame3 = DataFrame1 + DataFrame2


# Printing Portfolio DataFrames
print("Portfolio 1: \n")
print(DataFrame1, "\n")

print("Portfolio 2: \n")
print(DataFrame2, "\n")

print("Portfolio 1 + Portfolio 2: \n")
print(DataFrame3, "\n")