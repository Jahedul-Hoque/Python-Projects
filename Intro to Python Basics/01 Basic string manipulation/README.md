<div align="center">

# 🐍String Manipulation📈

</div>

## 📖 Overview
This project demonstrates a **basic Python logging system** for tracking trader activities. The program records **login events**, **trade execution messages**, and **trade completion status** using **string manipulation and f-strings**.

## 🔑 Key Features
- **Uses f-strings (`f"{}`)** for dynamic string formatting.
- **Replaces text dynamically** to update trade completion messages.
- **Tracks a trader's login, trading activity, and exit status.**

## 💻 Code Breakdown
```python
loggingOn = "Shan has logged into his citrix VM."
tradeValue = 10000
traderName = "shan"

# Creating a trade message using f-string
Message = f"{traderName.upper()} is trading {tradeValue} GBP"

# Replacing login message with trade completion status
taskEnded = loggingOn.replace("Shan has logged into his citrix VM.", 
                              f"{traderName.capitalize()} has finished trading")

print(loggingOn)
print(Message)
print(taskEnded)
print()
```

## 🔍 Explanation
1. **Trader Login Message (`loggingOn`)**
   - Stores the trader's **initial login event**.

2. **Trade Execution Message (`Message`)**
   - Uses **`f"{}`** format strings to dynamically update the trade message.
   - Converts `traderName` to **uppercase** for clarity.

3. **Trade Completion Update (`replace()`)**
   - Replaces the login message with **a new status message** after trading.
   - Uses **`capitalize()`** to format the trader’s name correctly.

## 🚀 Why Use f-strings and `replace()`?
✅ **Faster than `.format()`** – f-strings are **more readable and efficient**.
✅ **String immutability handling** – `replace()` avoids modifying the original string.
✅ **Easily customizable** – Can be adapted for **real-time trade logging**.

## 🔥 Future Enhancements
- ✅ Implement **real-time trade execution logs** using `datetime`.
- ✅ Store trade logs in a **CSV or database**.
- ✅ Integrate with **API-based trade monitoring**.

## 🎯 Summary
This **Python trading logger** demonstrates how to **dynamically format and manipulate strings** for tracking financial transactions. Using **f-strings and `replace()`**, the program efficiently manages trader actions from login to trade completion.

Happy Coding! 🚀🐍
