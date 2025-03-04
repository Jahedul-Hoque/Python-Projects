loggingOn = "Shan has logged into his citrix VM."
tradeValue = 10000
traderName = "shan"


Message = f"{traderName.upper()} is trading {tradeValue} GBP"
taskEnded = loggingOn.replace(
    "Shan has logged into his citrix VM.",
    f"{traderName.capitalize()} has finished trading",
)


print(loggingOn)
print(Message)
print(taskEnded)
print()
