import pandas as pd
import matplotlib as mp
import matplotlib.pyplot as plt
import os
import yfinance as yf

stock_df = yf.download("AAPL")

stock_df.hist(figsize=(12,8))

plt.savefig("plot.png")
os.system("xdg-open plot.png")
 # Saves the plot as an image file since terminal doesnt support GUI



