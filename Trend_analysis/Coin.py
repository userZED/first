import datetime
import pandas as pd
import numpy as np
import requests
import os
import csv
import websocket
import threading
import time
import json


#1622505601 same as 01:06:2021



#for websocket subscribe
#https://binance-docs.github.io/apidocs/spot/en/#live-subscribing-unsubscribing-to-streams
"""

{
"method": "SUBSCRIBE",
"params":
[
"btcusdt@aggTrade",
"btcusdt@depth"
],
"id": 1
}"""


class coin(object):


    def __init__(self,symbol,exhange_symbol) -> None:
        """always use symbols lowercase"""
        self.symbol = symbol
        self.exchange_symbol = exhange_symbol


 


        #example of kline dictionary
 

        
        self.base_columns = ["Open_time"
                                ,"Open"
                                ,"High"
                                ,"Low"
                                ,"Close"
                                ,"Volume"
                                ,"Close_time"
                                ,"Quote_asset_volume"
                                ,"Number_of_trades"
                                ,"Taker_buy_base_asset_volume"
                                ,"Taker_buy_quote_asset_volume"
                                ,"Ignore"]

        self.trade_base_columns= ["event_Type"
                                    ,"event_time"
                                    ,"symbol"
                                    ,"trade_id"
                                    ,"price"
                                    ,"quantitiy"
                                    ,"buyer_order_id"
                                    ,"seller_order_id"
                                    ,"trade_time"
                                    ,"is_buyer_market?"
                                    ,"ignore"

        ]
       
    def Get_Historical_OHLC_Data(self, interval = "1m", startTime = None, endTime = None, limit = 500) -> list:
        
        
        """
        limit:default 500
        exchange symbol:exhange coin symbol default busd
        'If startTime and endTime are not sent, the most recent klines are returned' from binance api
        This function returns current coin data it can be used either current with requests.GET
        data or historical data based on startime and endTime
        -> LIST:
        [
            [
                Open time\n
                Open\n
                High\n
                Low\n
                Close\n
                Volume\n
                Close time\n
                Quote asset volume\n
                Number of trades\n
                Taker buy base asset volume\n
                Taker buy quote asset volume\n
                Ignore.!
            ]
            .
            .
            .

            
        """
        

        Klinesticks_endpoint = "https://api.binance.com/api/v3/klines"
        response =requests.get(Klinesticks_endpoint, params={"symbol": (self.symbol+self.exchange_symbol).upper()
                                                                ,"interval": interval
                                                                ,"startTime": startTime
                                                                ,"endTime": endTime
                                                                ,"limit": limit
                                                                })
        
        return response.json()      
        #return response.status_code


    def on_open(self, ws):
        print("opened")
        
    def on_close(self, ws):
        print("websocket closed")

    def on_error(self, ws, error):
        print(error)

    def message_for_candle(self, ws, message):
        data = json.loads(message)    
        return data


    def Websocket_Candlestick_Stream(self, *args):
        """args[0] =interval in munite"""

        """
        for candle data:
        URL = https://binance-docs.github.io/apidocs/spot/en/#kline-candlestick-streams
        """
        BASE_ENDPOINT ="wss://stream.binance.com:9443/ws/{}@kline_{}".format(self.symbol + self.exchange_symbol ,args[0])
        ws = websocket.WebSocketApp(BASE_ENDPOINT, on_message = self.message_for_candle, on_open = self.on_open, on_close = self.on_close, on_error = self.on_error)
        ws.run_forever()

    def message_for_trade(self, ws, message):
        data = json.loads(message)
        return  data
        
        
            
        
    def Websocket_trade_Stream(self): #it must be a stream
        BASE_ENDPOINT ="wss://stream.binance.com:9443/ws/{}@trade".format(self.symbol+self.exchange_symbol)
        ws =websocket.WebSocketApp(BASE_ENDPOINT,on_message = self.message_for_trade, on_open = self.on_open, on_close = self.on_close, on_error = self.on_error)
        ws.run_forever()






if __name__ == "__main__":
    
    print("base Coin class")
