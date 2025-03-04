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
