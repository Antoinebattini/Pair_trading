from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

class trading():

    def __init__(self):
        
        self.account = account()
        self.trading_client = self.account.getAccount()
        self.keys = self.account.getKeys()

        self.ticker = tickers()
        self.stock_df = self.ticker.getStock()

        # HTTP request header
        self.headers = {
            "accept": "application/json",
            "APCA-API-KEY-ID": self.keys[1],
            "APCA-API-SECRET-KEY": self.keys[2]
        }

        self.endpoint_positions = self.keys[0] + "/v2/positions"
        self.endpoint_orders = self.keys[0] + "/v2/orders"


    def signals_to_trade(self, spread, signal):
        pass

    def open(self, ticker1, ticker2, price1, price2):
        order_long = MarketOrderRequest(
            symbol = ticker1
            qty = 1
            side=OrderSide.BUY,
            time_in_force=TimeInForce.DAY,
            client_order_id= ticker1 + "/ID" #changer ID par le ID
        ) 
        order_short = MarketOrderRequest(
            symbol = ticker2
            qty = price1/price2
            side=OrderSide.BUY,
            time_in_force=TimeInForce.DAY,
            client_order_id= ticker2 + "/ID" #changer ID par le ID
        ) 
        market_order_long = self.trading_client.submit_order(
                        order_data=order_long
                    )
        market_order_short = self.trading_client.submit_order(
                        order_data=order_short
                    )


    def close(self):
        url_ticker1 = self.endpoint_positions + "/" + ticker1
        url_ticker2 = self.endpoint_positions + "/" + ticker2

        response_ticker1 = requests.delete(url_ticker1, headers=self.headers)
        response_ticker2 = requests.delete(url_ticker2, headers=self.headers)