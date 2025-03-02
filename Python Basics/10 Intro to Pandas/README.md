<div align="center">

# 📊 Intro to Pandas 📈

</div>

## 📖 Overview
This project demonstrates **Pandas Series and DataFrame operations** for financial data management. It covers **indexing, locating specific values, and performing arithmetic operations on financial datasets**.

## 🔑 Key Features
- **Creating Pandas Series (`pd.Series()`)** for individual trade values.
- **Constructing DataFrames (`pd.DataFrame()`)** for employee and portfolio data.
- **Indexing and retrieving data using `.loc[]`.**
- **Performing arithmetic operations on DataFrames.**

## 💻 Code Breakdown
```python
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

# Adding Portfolio Values
DataFrame3 = DataFrame1 + DataFrame2

# Printing Portfolio DataFrames
print("Portfolio 1: \n")
print(DataFrame1, "\n")

print("Portfolio 2: \n")
print(DataFrame2, "\n")

print("Portfolio 1 + Portfolio 2: \n")
print(DataFrame3, "\n")
```

## �� Explanation
1. **Creating Pandas Series (`pd.Series()`)**
   - Stores trade values with custom **trader name indexing**.
   - Uses `.loc[]` to retrieve specific values by index.

2. **Building a Pandas DataFrame (`pd.DataFrame()`)**
   - Stores structured employee data with **name-based indexing (`set_index()`)**.
   - Provides an easy way to access and manipulate tabular financial data.

3. **Performing DataFrame Arithmetic Operations**
   - **Adds two portfolio DataFrames (`DataFrame1 + DataFrame2`)**.
   - Aggregates financial data efficiently for trading analytics.

## 🚀 Why Use Pandas for Financial Data?
✅ **Simplifies data analysis** – Easily structure and manipulate financial datasets.  
✅ **Efficient numerical computations** – Optimized for handling large financial records.  
✅ **Essential for quantitative finance** – Used in backtesting, portfolio management, and trade analytics.  

## 🔥 Future Enhancements
- ✅ Implement **data visualization with Matplotlib & Seaborn**.
- ✅ Integrate **live stock market data using APIs**.
- ✅ Use **grouping & aggregation (`groupby()`) for deeper insights**.

## 🎯 Summary
This **Python Pandas project** introduces **Series and DataFrame operations**, focusing on **indexing, retrieving values, and performing arithmetic on financial datasets**. These skills are vital for **data-driven finance, portfolio analysis, and trade tracking**.

Happy Coding! 🚀🐍
