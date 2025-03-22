# 📈 Binance Crypto Trading Bot & Backtester with Python

## Overview
This Python-based project features a **Crypto Trading Bot** and **Backtesting System** that interacts with the **Binance API**. It enables live trading simulation and strategy evaluation using historical data, offering full control over trading thresholds such as **buy/sell limits**, **stop-loss**, and **quantity management**.

---

## 🚀 Features
- **Live Trading Bot**:
  - Executes automated buy/sell orders using Binance testnet.
  - Real-time monitoring of BTC price.
  - Customizable trading thresholds including second buy/sell orders and stop-loss.

- **Backtesting System**:
  - Fetches historical data (1-minute intervals) from Binance.
  - Simulates trades and calculates profit/loss.
  - Supports dual buy/sell levels and stop-loss triggers.

- **Object-Oriented Design**:
  - Modular and reusable code with **TradeParameters**, **MarketData**, **TradingBot**, and **Backtester** classes.

---

## 📂 File Structure
```
crypto_trading_bot/
├── .env                 # Contains APIKey and Secret
├── bot.py               # Main script with all class definitions and logic
└── README.md            # This documentation
```

---

## 🔧 Setup Instructions
1. **Install Dependencies**:
```bash
pip install python-binance pandas python-dotenv
```

2. **Setup .env File**:
```bash
APIKey=your_api_key_here
Secret=your_api_secret_here
```

3. **Run the Bot**:
```bash
python bot.py
```

---

## 📊 Key Classes Explained
### `TradeParameters`
Encapsulates trading thresholds:
- `buy_threshold`
- `second_buy_threshold`
- `sell_threshold`
- `second_sell_threshold`
- `stop_loss`
- `quantity`

### `MarketData`
- Fetches **live BTC price**.
- Retrieves **historical price data** from Binance (using `get_klines`).

### `TradingBot`
- Monitors real-time price.
- Executes buy/sell orders based on thresholds.
- Handles stop-loss and double trade entries.

### `Backtester`
- Simulates trades over historical data.
- Tracks balance, BTC holdings, trade history.
- Returns **profit/loss metrics**.

---

## 💡 Example Use
```python
# Backtest for BTC with custom thresholds
run_custom_backtest(
  symbol="BTCUSDT",
  buy_threshold=84200,
  second_buy_threshold=82000,
  sell_threshold=85000,
  second_sell_threshold=87000,
  stop_loss=81000,
  quantity=0.001
)
```

---

## 📈 Sample Output
```
Custom Backtest Results for BTCUSDT:
Cash Balance: $21000.00
BTC Holding: 1.00
Profit: $500.00
Current Price: 85000.0
```

---

## 📬 Contact & Contributions
**Email**: [jahedul.hoque12@gmail.com](mailto:jahedul.hoque12@gmail.com)  
**LinkedIn**: [Jahedul Hoque](https://www.linkedin.com/in/jahedul-hoque/)  
**GitHub**: [jahedul-hoque](https://github.com/jahedul-hoque)

Feel free to **fork this repo**, suggest improvements, or contribute with new features like **technical indicators**, **data visualization**, or **multi-asset support**.

---

## 🎯 Future Enhancements
- Non Cummulative P&L statement per 1440 minute intervals for 7 intervals.
- Adding a cummulative P&L Statement at the end of the 7 intervals.
- Calculating the sharp ratio of investment.
- Evaluate strategy per interval and look for trends.

---

Happy Trading! 🚀

