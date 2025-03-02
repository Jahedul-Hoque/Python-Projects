import pandas as pd
# Series: Collumn of a data frame


Trades = [200, 210, 220, 230, 240]
TradeValues = pd.Series(Trades, index = ["Trader 1", "Trader 2", "Trader 3", "Trader 4", "Trader 5"], dtype="int16")
print (TradeValues, "\n")
# Print TradeValues with a given index of data type Integer that contains 16 bits


print("Trader 2 has traded", TradeValues.loc["Trader 2"], "USDT")
# Locates an index of Trader 2


# Data Frame: Combination of an excel sheet and a database table
df = pd.DataFrame({
    'Name': ['Jad', 'Shanawaz', 'Jim', 'Kevin'],
    'Salary':[35000, 150000, 1000000, 125000],
    'Title': ['EUS Engineer', 'Developer', 'CEO', 'Developer']
})

df = df.set_index("Name")

print(df)
