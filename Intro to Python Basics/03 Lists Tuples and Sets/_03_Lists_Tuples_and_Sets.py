TradeSecurities = ["Gold", "Silver", "Bonds", "FX", "Crypto"]
DifferentTradeSecurities = ["Bitcoin", "Gamestop"]
# initialise list

print ("Trade Security List:", TradeSecurities)
print()


print ("Quantity of Securities:", len(TradeSecurities))
print()
#print length of list

print ("First security:", TradeSecurities[0])
print()
#prints index 0 of list

print ("Every security after the first 2 securities:", TradeSecurities[2:])
print()
#prints everything including and after index 2

TradeSecurities.append("Trump Coin")
# add element to the end

print ("Adding Trump coin to the end of list:", TradeSecurities)
print()

TradeSecurities.insert(1, "Melena Coin")
#inserts element at index 1
print ("Adding Melena coin to the second index of list:", TradeSecurities)
print()

TradeSecurities.extend(DifferentTradeSecurities)
print("Adding new list to the end of current list:", TradeSecurities)
print()
#adding 2 lists together

DeletedSecurity = TradeSecurities.pop()
print("Last security on the Trade security list is:", DeletedSecurity)
print()
#removes last value on the list, assigns it to new variable and prints it out

TradeSecurities.sort()
print("Sorting list based on alphebetical order")
print(TradeSecurities)