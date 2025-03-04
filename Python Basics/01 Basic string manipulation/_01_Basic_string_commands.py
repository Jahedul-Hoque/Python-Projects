logging_on = "Shan has logged into his citrix VM."
trade_value = 10000
trader_name = "shan"


message = f"{trader_name.upper()} is trading {trade_value} GBP"
task_ended = logging_on.replace(
    "Shan has logged into his citrix VM.",
    f"{trader_name.capitalize()} has finished trading",
)


print(logging_on)
print(message)
print(task_ended)
print()
