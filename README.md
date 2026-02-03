# Binance Futures Trading Bot

A simple Python-based CLI bot to place Market and Limit orders on the Binance Futures Testnet.

## Prerequisites

- Python 3.x
- Binance Futures Testnet Account (<https://testnet.binancefuture.com>)

## Setup

1. **Clone/Download the repository**
2. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Environment Setup**:
    - Rename `.env.example` to `.env`.
    - Edit `.env` and add your Binance Testnet API Key and Secret.

    ```
    BINANCE_API_KEY=your_key
    BINANCE_API_SECRET=your_secret
    BASE_URL=https://testnet.binancefuture.com
    ```

## Usage

Run the `cli.py` script with the required arguments.

### Arguments

- `--symbol`: Trading Pair (e.g., `BTCUSDT`)
- `--side`: `BUY` or `SELL`
- `--type`: `MARKET` or `LIMIT`
- `--qty`: Order Quantity (e.g., `0.001`)
- `--price`: Order Price (Required for `LIMIT` orders)

### Examples

**1. Place a Market Buy Order**

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.002
```

**2. Place a Limit Sell Order**

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.001 --price 90000
```

## Logs

Logs are saved to `trading_bot.log` and printed to the console.

## Structure

- `bot/`: Core logic (Client, Orders, Config, Validators)
- `cli.py`: Entry point
- `requirements.txt`: Dependencies
