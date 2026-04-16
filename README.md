# A Trading Bot on Binance Futures Testnet
    
This is a python bot that can place both Market and Limit orders on Binance Futures Testnet (USDT-M)

## Installation:

1. Clone the repo.
   
```
git clone https://github.com/Mukshub/A-Simplified-Trading_Bot.git
cd A-Simplified-Trading-Bot
```

2. Set up the virtual environment.

```
python -m venv .venv
venv\Scripts\activate    # Windows
source venv/bin/activate # Mac/Linux
```

3. Install requirements
```
pip install -r requirements.txt
```
    
4. Create your own API and Secret Keys at [https://testnet.binancefuture.com]

5. Create a .env file at the root with this structure
```
API_KEY=xx
SECRET_KEY=xx
```
## How to Run it

#### with Web UX
* Run `python app.py`
* go to `localhost:5000` in your browser
#### In Terminal
* To place a market order: `python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001`
* To place a limit order: `python cli.py --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.001 --price 75000`



## Assumptions
* This bot only works on **Binance Futures Testnet**, not the real Binance market.
* LIMIT orders **require** a `--price` argument
* Only supports **BTCUSDT** style symbols (USDT-M futures)

