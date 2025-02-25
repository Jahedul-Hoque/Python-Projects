<div align="center">

# 📜 Trade Securities List & Set Operations 💰

</div>

## 📖 Overview
This project demonstrates **list and set operations in Python** related to trading securities. It covers **list indexing, modifications, sorting, merging lists, and set operations** to ensure efficient trade data management.

## 🔑 Key Features
- **List Operations:** Adding, removing, sorting, and indexing trade securities.
- **Combining Lists:** Merging multiple security lists dynamically.
- **Set Operations:** Removing duplicates and performing set unions.
- **Looping Through Lists:** Printing index-element pairs for analysis.

## 💻 Code Breakdown
```python
TradeSecurities = ["Gold", "Silver", "Bonds", "FX", "Crypto"]
DifferentTradeSecurities = ["Bitcoin", "Gamestop"]

# Display trade securities list
print("Trade Security List:", TradeSecurities, "\n")

# Display number of securities
print("Quantity of Securities:", len(TradeSecurities), "\n")

# Access elements by index
print("First security:", TradeSecurities[0], "\n")

# Slice list (exclude first two elements)
print("Every security after the first 2 securities:", TradeSecurities[2:], "\n")

# Add securities
TradeSecurities.append("Trump Coin")
print("Adding Trump Coin to the end of list:", TradeSecurities, "\n")

TradeSecurities.insert(1, "Melena Coin")
print("Adding Melena Coin to the second index of list:", TradeSecurities, "\n")

# Merge lists
TradeSecurities.extend(DifferentTradeSecurities)
print("Adding new list to the end of current list:", TradeSecurities, "\n")

# Remove last element
DeletedSecurity = TradeSecurities.pop()
print("Last security on the Trade security list is:", DeletedSecurity, "\n")

# Sort list
TradeSecurities.sort()
print("Sorting list based on alphabetical order:\n", TradeSecurities, "\n")

# Find index of an item
print("Gold's index number is", TradeSecurities.index("Gold"), "\n")

# Print index-element pairs
for trade in TradeSecurities:
    print(TradeSecurities.index(trade), "is indexed to", trade)

# Set operations to remove duplicates
TradeSecuritySet = {"Gold", "Silver", "FX", "FX", "FX"}
NewTradeSecuritySet = {"Gold", "MemeCoin", "Gamestop", "FX"}
print("Union of 2 sets without any duplicates:", TradeSecuritySet.union(NewTradeSecuritySet), "\n")
print("Length of set without duplicates:", len(TradeSecuritySet), "\n")
```

## 🔍 Explanation
1. **List Indexing & Slicing**
   - Accesses elements via index (`[0]`, `[2:]`).
   
2. **Modifying Lists**
   - **Appending & Inserting:** Adds elements at specific positions.
   - **Extending Lists:** Merges multiple lists.
   - **Popping Elements:** Removes and stores the last item.
   - **Sorting:** Orders securities alphabetically.

3. **Looping & Indexing**
   - Iterates through the list to print **index-element pairs**.

4. **Set Operations**
   - **Union (`union()`)** combines sets without duplicates.
   - **Set Length (`len()`)** determines unique elements count.

## 🚀 Why Use Lists & Sets?
✅ **Lists maintain order & allow duplicates** – Useful for trade history.  
✅ **Sets remove duplicates automatically** – Useful for unique securities.  
✅ **Sorting & Indexing ensure data structure efficiency** – Useful in financial applications.  

## 🔥 Future Enhancements
- ✅ Implement **dictionary-based trade tracking**.
- ✅ Optimize **search operations using binary search (`bisect`)**.
- ✅ Store and manage trade data in **pandas DataFrames**.

## 🎯 Summary
This **Python trade securities project** explores **list and set operations** for effective financial data handling. The script showcases **sorting, merging, indexing, and duplicate removal**, ensuring efficient trade security management.

Happy Coding! 🚀🐍