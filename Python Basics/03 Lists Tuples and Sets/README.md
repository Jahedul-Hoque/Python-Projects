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
trade_securities = ["Gold", "Silver", "Bonds", "FX", "Crypto"]
different_trade_securities = ["Bitcoin", "Gamestop"]
# initialise list

print("Trade Security List:", trade_securities)
print()


print("Quantity of Securities:", len(trade_securities))
print()
# print length of list

print("First security:", [trade_securities])
print()
# prints index 0 of list

print("Every security after the first 2 securities:", trade_securities[2:])
print()
# prints everything including and after index 2

trade_securities.append("Trump Coin")
# add element to the end

print("Adding Trump coin to the end of list:", trade_securities)
print()

trade_securities.insert(1, "Melena Coin")
# inserts element at index 1
print("Adding Melena coin to the second index of list:", trade_securities)
print()

trade_securities.extend(different_trade_securities)
print("Adding new list to the end of current list:", trade_securities)
print()
# adding 2 lists together

DeletedSecurity = trade_securities.pop()
print("Last security on the Trade security list is:", DeletedSecurity)
print()
# removes last value on the list, assigns it to new variable and prints it out

trade_securities.sort()
print("Sorting list based on alphebetical order\n")
print(trade_securities)
print()


print("Golds index number is", trade_securities.index("Gold"))
print()
# print the index of a security

for trade in trade_securities:
    print(trade_securities.index(trade), "is indexed to ", trade)

    # trade becomes an index value for the elements in the list


print()
trade_security_set = {"Gold", "Silver", "FX", "FX", "FX"}
new_trade_securities = {"Gold", "MemeCoin", "Gamestop", "FX"}
print(
    "Union of 2 sets without any duplicates: ",
    trade_securities.union(new_trade_securities),
    "\n",
)
print("Length of set without duplicates: ", len(trade_security_set), "\n")
# sets have no order and will remove duplicates

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