import pandas as pd

# Creating a Pandas Series (1D data structure)
trades = [200, 210, 220, 230, 240]
trade_values = pd.Series(
    trades,
    index=["Trader 1", "Trader 2", "Trader 3", "Trader 4", "Trader 5"],
    dtype="int16",
)
print(trade_values, "\n")


# Retrieving specific trade data using .loc[]
print("Trader 2 has traded", trade_values.loc["Trader 2"], "USDT")


# Creating a DataFrame (structured table format)
new_data_frame = pd.DataFrame(
    {
        "Name": ["Jad", "Shanawaz", "Jim", "Kevin"],
        "Salary": [35000, 150000, 1000000, 125000],
        "Title": ["EUS Engineer", "Developer", "CEO", "Developer"],
    }
)
new_data_frame = new_data_frame.set_index("Name")
print(new_data_frame, "\n")


# Creating two Portfolio DataFrames
data_frame_1 = pd.DataFrame(
    {"Portfolio Value": [1000, 1500, 2000, 2500]},
    index=[1, 2, 3, 4],
    dtype="int16",
)
data_frame_2 = pd.DataFrame(
    {"Portfolio Value": [1000, 1500, 2000, 2500]},
    index=[1, 2, 3, 4],
    dtype="int16",
)

# Adding Portfolio Values with matching indexes
data_frame_3 = data_frame_1 + data_frame_2


# Printing Portfolio DataFrames
print("Portfolio 1: \n")
print(data_frame_1, "\n")

print("Portfolio 2: \n")
print(data_frame_2, "\n")

print("Portfolio 1 + Portfolio 2: \n")
print(data_frame_3, "\n")
