<div align="center">

# 🐍 Integer/Float manipulation 💰

</div>

## 📖 Overview
This project demonstrates basic **numeric operations in Python** related to trading. It explores **integer and float data types, arithmetic operations, absolute values, and rounding functions**.

## 🔑 Key Features
- **Checks variable data types** using `type()`.
- **Performs arithmetic operations** on trade values.
- **Uses `abs()` to convert negative trade values to positive.**
- **Applies `round()` to round floating point trade values.**

## 💻 Code Breakdown
```python
# Defining an integer trade value
TradeIntegerValue = 3
print(type(TradeIntegerValue))  # Prints variable type (int)

# Defining a floating-point trade value
TradeFloatValue = 3.54
print(type(TradeFloatValue))  # Prints variable type (float)

# Modifying Trade Value
TradeValue = 1000
TradeValue += 100  # Adds 100 to the variable
print(TradeValue)  # Outputs updated TradeValue

# Handling negative trade values
NegativeTradeValue = -1000
print(abs(NegativeTradeValue))  # Prints absolute (positive) value

# Rounding floating point values
print(round(TradeFloatValue))  # Prints rounded version of TradeFloatValue
```

## 🔍 Explanation
1. **Checking Data Types (`type()`)**
   - Determines if a variable is an **integer (`int`)** or a **floating-point number (`float`)**.

2. **Arithmetic Operations (`+=`)**
   - Increases `TradeValue` by **100** dynamically.

3. **Absolute Value (`abs()`)**
   - Converts **negative trade values** into **positive numbers**.

4. **Rounding Values (`round()`)**
   - Rounds `TradeFloatValue` to the **nearest whole number**.

## 🚀 Why Use These Operations?
✅ **Essential for financial calculations** – Helps ensure data integrity.  
✅ **Simplifies data transformations** – Quick rounding and absolute values.  
✅ **Enhances real-time trading computations** – Easily modify trade values dynamically.  

## 🔥 Future Enhancements
- ✅ Implement **currency formatting** using `locale`.
- ✅ Integrate **percentage calculations** for trade profits/losses.
- ✅ Store and manipulate trade values in **pandas DataFrames**.

## 🎯 Summary
This **Python trade operations script** introduces fundamental numeric operations **widely used in financial calculations**. The project demonstrates **type checking, arithmetic operations, absolute values, and rounding functions**, ensuring accurate trade data processing.

Happy Coding! 🚀🐍

