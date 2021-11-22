import pandas as pd
import numpy as np

#1
#how can we determine support and resistance level

#in series of close prices we need to determine lower lows and higher highs
#and then we need to determine close price hit the trendline or not
#we called it a line but it can be area if we determine area also we need to determine how close price interact in these area

#2
#secondly we need to find pre-determined patterns


#3
#and last one using indicators to get another tips for coin nest movements
#all of the above methodes must work for all cryptocoins with the asyncronous way and later maybe for stocks



#these 3 stages and my personal ides will create our trading stretagie
solana_daily = pd.read_csv("SOL1-USD.csv")
close = np.array(solana_daily["Close"][-100:])
sorted_close=close
sorted_close.sort()

#wee need to determine how much x1 and x2 are close each other 
y1 = sorted_close[-2]
x1 = int(np.where(close == y1)[0])

y2 = sorted_close[-1]
x2 = int(np.where(close == y2)[0])

resistance_line_slope = (y2-y1)/(x2-x1)

