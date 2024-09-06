import os
import pandas as pd
import numpy as np
import math
import datetime as dt

from sklearn.metrics import mean_squared_error, mean_absolute_error, explained_variance_score, r2_score 
from sklearn.metrics import mean_poisson_deviance, mean_gamma_deviance, accuracy_score
from sklearn.preprocessing import MinMaxScaler

from itertools import cycle
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

import seaborn as sns 
import matplotlib.pyplot as plt 
from colorama import Fore

import tkinter as tk

bitcoindf = pd.read_csv('BTC-USD.csv')
bitcoindf = bitcoindf.rename(columns={'Date': 'date','Open':'open','High':'high','Low':'low','Close':'close','Adj Close':'adj_close','Volume':'volume'})
dogecoindf = pd.read_csv('DOGE-USD.csv')
dogecoindf = dogecoindf.rename(columns={'Date': 'date','Open':'open','High':'high','Low':'low','Close':'close','Adj Close':'adj_close','Volume':'volume'})
ethereumdf = pd.read_csv('ETH-USD.csv')
ethereumdf = ethereumdf.rename(columns={'Date': 'date','Open':'open','High':'high','Low':'low','Close':'close','Adj Close':'adj_close','Volume':'volume'})
cardanodf = pd.read_csv('ADA-USD.csv')
cardanodf = cardanodf.rename(columns={'Date': 'date','Open':'open','High':'high','Low':'low','Close':'close','Adj Close':'adj_close','Volume':'volume'})
bnbdf = pd.read_csv('BNB-USD.csv')
bnbdf = bnbdf.rename(columns={'Date': 'date','Open':'open','High':'high','Low':'low','Close':'close','Adj Close':'adj_close','Volume':'volume'})
hexdf = pd.read_csv('HEX-USD.csv')
hexdf = hexdf.rename(columns={'Date': 'date','Open':'open','High':'high','Low':'low','Close':'close','Adj Close':'adj_close','Volume':'volume'})
dotdf = pd.read_csv('DOT1-USD.csv')
dotdf = dotdf.rename(columns={'Date': 'date','Open':'open','High':'high','Low':'low','Close':'close','Adj Close':'adj_close','Volume':'volume'})
solanadf = pd.read_csv('SOL1-USD.csv')
solanadf = solanadf.rename(columns={'Date': 'date','Open':'open','High':'high','Low':'low','Close':'close','Adj Close':'adj_close','Volume':'volume'})
tetherdf = pd.read_csv('USDT-USD.csv')
tetherdf = tetherdf.rename(columns={'Date': 'date','Open':'open','High':'high','Low':'low','Close':'close','Adj Close':'adj_close','Volume':'volume'})
usdcdf = pd.read_csv('USDC-USD.csv')
usdcdf = usdcdf.rename(columns={'Date': 'date','Open':'open','High':'high','Low':'low','Close':'close','Adj Close':'adj_close','Volume':'volume'})
xrpdf = pd.read_csv('XRP-USD.csv')
xrpdf = xrpdf.rename(columns={'Date': 'date','Open':'open','High':'high','Low':'low','Close':'close','Adj Close':'adj_close','Volume':'volume'})

bitcoindf = bitcoindf.fillna(method = 'ffill')
dogecoindf = dogecoindf.fillna(method = 'ffill')
ethereumdf = ethereumdf.fillna(method = 'ffill')
cardanodf = cardanodf.fillna(method = 'ffill')
bnbdf = bnbdf.fillna(method='ffill')
hexdf = hexdf.fillna(method='ffill')
dotdf = dotdf.fillna(method='ffill')
solanadf = solanadf.fillna(method='ffill')
tetherdf = tetherdf.fillna(method='ffill')
usdcdf = usdcdf.fillna(method='ffill')
xrpdf = xrpdf.fillna(method='ffill')

bitcoindf['date'] = pd.to_datetime(bitcoindf.date)
dogecoindf['date'] = pd.to_datetime(dogecoindf.date)
ethereumdf['date'] = pd.to_datetime(ethereumdf.date)
cardanodf['date'] = pd.to_datetime(cardanodf.date)
bnbdf['date'] = pd.to_datetime(bnbdf.date)
hexdf['date'] = pd.to_datetime(hexdf.date)
dotdf['date'] = pd.to_datetime(dotdf.date)
solanadf['date'] = pd.to_datetime(solanadf.date)
tetherdf['date'] = pd.to_datetime(tetherdf.date)
usdcdf['date'] = pd.to_datetime(usdcdf.date)
xrpdf['date'] = pd.to_datetime(xrpdf.date)

last1year_bitcoindf = bitcoindf[bitcoindf['date'] > '09-2020']
last1year_cardanodf = cardanodf[cardanodf['date'] > '09-2020']
last1year_dogecoindf = dogecoindf[dogecoindf['date'] > '09-2020']
last1year_ethereumdf = ethereumdf[ethereumdf['date'] > '09-2020']
last1year_bnbdf = bnbdf[bnbdf['date'] > '09-2020']
last1year_hexdf = hexdf[hexdf['date'] > '09-2020']
last1year_dotdf = dotdf[dotdf['date'] > '09-2020']
last1year_solanadf = solanadf[solanadf['date'] > '09-2020']
last1year_tetherdf = tetherdf[tetherdf['date'] > '09-2020']
last1year_usdcdf = usdcdf[usdcdf['date'] > '09-2020']
last1year_xrpdf = xrpdf[xrpdf['date'] > '09-2020']

last1month_bitcoindf = bitcoindf[bitcoindf['date'] > '08-2021']
last1month_cardanodf = cardanodf[cardanodf['date'] > '08-2021']
last1month_dogecoindf = dogecoindf[dogecoindf['date'] > '08-2021']
last1month_ethereumdf = ethereumdf[ethereumdf['date'] > '08-2021']
last1month_bnbdf = bnbdf[bnbdf['date'] > '08-2021']
last1month_hexdf = hexdf[hexdf['date'] > '08-2021']
last1month_dotdf = dotdf[dotdf['date'] > '08-2021']
last1month_solanadf = solanadf[solanadf['date'] > '08-2021']
last1month_tetherdf = tetherdf[tetherdf['date'] > '08-2021']
last1month_usdcdf = usdcdf[usdcdf['date'] > '08-2021']
last1month_xrpdf = xrpdf[xrpdf['date'] > '08-2021']

import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

selected_crypto = []
        
def plot_graph_1():
    tcp = tk.Tk() 
    tcp.title('Total Closing Price') 
    tcp.geometry("500x500")
    fig = plt.figure(figsize=(15, 30))

    counter1 = 1
    l = len(selected_crypto)
    n = (l//2)+1
    for i in selected_crypto:
        if i=='BinanceCoin':
            plt.subplot(n, 2, counter1)
            plt.plot(bnbdf['date'], bnbdf['close'], color="blue")
            plt.title('Binance Coin Close Price')
            counter1+=1
        elif i=='Bitcoin':
            plt.subplot(n, 2, counter1)
            plt.plot(bitcoindf['date'], bitcoindf['close'], color="red")
            plt.title('Bitcoin Close Price')
            counter1+=1
        elif i=='Cardano':
            plt.subplot(n, 2, counter1)
            plt.plot(cardanodf['date'], cardanodf['close'], color="black")
            plt.title('Cardano Close Price')
            counter1+=1
        elif i=='Dogecoin':
            plt.subplot(n, 2, counter1)
            plt.plot(dogecoindf['date'], dogecoindf['close'], color="orange")
            plt.title('Dogecoin Close Price')
            counter1+=1
        elif i=='Ethereum':
            plt.subplot(n, 2, counter1)
            plt.plot(ethereumdf['date'], ethereumdf['close'], color="green")
            plt.title('Ethereum Close Price')
            counter1+=1
        elif i=='HEX':
            plt.subplot(n, 2, counter1)
            plt.plot(hexdf['date'], hexdf['close'], color="purple")
            plt.title('Hex Close Price')
            counter1+=1
        elif i=='Polkadot':
            plt.subplot(n, 2, counter1)
            plt.plot(dotdf['date'], dotdf['close'], color="red")
            plt.title('Polkadot Close Price')
            counter1+=1
        elif i=='Solana':
            plt.subplot(n, 2, counter1)
            plt.plot(solanadf['date'], solanadf['close'], color="green")
            plt.title('Solana Close Price')
            counter1+=1
        elif i=='Tether':
            plt.subplot(n, 2, counter1)
            plt.plot(tetherdf['date'], tetherdf['close'], color="orange")
            plt.title('Tether Close Price')
            counter1+=1
        elif i=='USDCoin':
            plt.subplot(n, 2, counter1)
            plt.plot(usdcdf['date'], usdcdf['close'], color="pink")
            plt.title('USD Coin Close Price')
            counter1+=1
        elif i=='XRP':
            plt.subplot(n, 2, counter1)
            plt.plot(xrpdf['date'], xrpdf['close'], color="brown")
            plt.title('Ripple Close Price')
            counter1+=1
        plt.subplots_adjust(hspace=1.2)

    canvas = FigureCanvasTkAgg(fig, master=tcp)
    canvas.draw()
    canvas.get_tk_widget().pack()

def plot_graph_2():
    lcp = tk.Tk() 
    lcp.title('Latest Closing Price') 
    lcp.geometry("500x500")
    fig = plt.figure(figsize=(15, 30))

    counter2 = 1
    for i in selected_crypto:
        if i=='BinanceCoin':
            plt.subplot(len(selected_crypto), 1, counter2)
            plt.plot(last1year_bnbdf['date'], last1year_bnbdf['close'], color="blue")
            plt.legend(["BNB"])
            counter2+=1
        elif i=='Bitcoin':
            plt.subplot(len(selected_crypto), 1, counter2)
            plt.plot(last1year_bitcoindf['date'], last1year_bitcoindf['close'], color="red")
            plt.legend("B")
            counter2+=1
        elif i=='Cardano':
            plt.subplot(len(selected_crypto), 1, counter2)
            plt.plot(last1year_cardanodf['date'], last1year_cardanodf['close'], color="black")
            plt.legend("C")
            counter2+=1
        elif i=='Dogecoin':
            plt.subplot(len(selected_crypto), 1, counter2)
            plt.plot(last1year_dogecoindf['date'], last1year_dogecoindf['close'], color="orange")
            plt.legend("D")
            counter2+=1
        elif i=='Ethereum':
            plt.subplot(len(selected_crypto), 1, counter2)
            plt.plot(last1year_ethereumdf['date'], last1year_ethereumdf['close'], color="green")
            plt.legend("E")
            counter2+=1
        elif i=='HEX':
            plt.subplot(len(selected_crypto), 1, counter2)
            plt.plot(last1year_hexdf['date'], last1year_hexdf['close'], color="purple")
            plt.legend(["HEX"])
            counter2+=1
        elif i=='Polkadot':
            plt.subplot(len(selected_crypto), 1, counter2)
            plt.plot(last1year_dotdf['date'], last1year_dotdf['close'], color="red")
            plt.legend(["DOT"])
            counter2+=1
        elif i=='Solana':
            plt.subplot(len(selected_crypto), 1, counter2)
            plt.plot(last1year_solanadf['date'], last1year_solanadf['close'], color="green")
            plt.legend(["SOL"])
            counter2+=1
        elif i=='Tether':
            plt.subplot(len(selected_crypto), 1, counter2)
            plt.plot(last1year_tetherdf['date'], last1year_tetherdf['close'], color="orange")
            plt.legend(["USDT"])
            counter2+=1
        elif i=='USDCoin':
            plt.subplot(len(selected_crypto), 1, counter2)
            plt.plot(last1year_usdcdf['date'], last1year_usdcdf['close'], color="pink")
            plt.legend(["USDC"])
            counter2+=1
        elif i=='XRP':
            plt.subplot(len(selected_crypto), 1, counter2)
            plt.plot(last1year_xrpdf['date'], last1year_xrpdf['close'], color="brown")
            plt.legend(["XRP"])
            counter2+=1
        plt.subplots_adjust(hspace=1.2)

    canvas = FigureCanvasTkAgg(fig, master=lcp)
    canvas.draw()
    canvas.get_tk_widget().pack()

def plot_graph_3():
    volume = tk.Tk() 
    volume.title('Volume') 
    volume.geometry("500x500")
    fig = plt.figure(figsize = (15,15))

    counter3 = 1
    for i in selected_crypto:
        if i=='BinanceCoin':
            plt.plot(last1year_bnbdf['date'], last1year_bnbdf['volume'])
            counter3+=1
        elif i=='Bitcoin':
            plt.plot(last1year_bitcoindf['date'] , last1year_bitcoindf['volume'])
            counter3+=1
        elif i=='Cardano':
            plt.plot(last1year_cardanodf['date'] , last1year_cardanodf['volume'])
            counter3+=1
        elif i=='Dogecoin':
            plt.plot(last1year_dogecoindf['date'], last1year_dogecoindf['volume'])
            counter3+=1
        elif i=='Ethereum':
            plt.plot(last1year_ethereumdf['date'], last1year_ethereumdf['volume'])
            counter3+=1
        elif i=='HEX':
            plt.plot(last1year_hexdf['date'], last1year_hexdf['volume'])
            counter3+=1
        elif i=='Polkadot':
            plt.plot(last1year_dotdf['date'], last1year_dotdf['volume'])
            counter3+=1
        elif i=='Solana':
            plt.plot(last1year_solanadf['date'], last1year_solanadf['volume'])
            counter3+=1
        elif i=='Tether':
            plt.plot(last1year_tetherdf['date'], last1year_tetherdf['volume'])
            counter3+=1
        elif i=='USDCoin':
            plt.plot(last1year_usdcdf['date'], last1year_usdcdf['volume'])
            counter3+=1
        elif i=='XRP':
            plt.plot(last1year_xrpdf['date'], last1year_xrpdf['volume'])
            counter3+=1
        plt.subplots_adjust(hspace=1.2)
        plt.title('Volume of Crypto')
        plt.legend(selected_crypto)

    canvas = FigureCanvasTkAgg(fig, master=volume)
    canvas.draw()
    canvas.get_tk_widget().pack()
    
def plot_graph_4():
    cop = tk.Tk() 
    cop.title('Close and Open Price') 
    cop.geometry("500x500")
    fig = plt.figure(figsize=(15, 30))

    counter4 = 1
    for i in selected_crypto:
        if i=='BinanceCoin':
            plt.subplot(len(selected_crypto), 1, counter4)
            plt.plot(last1month_bnbdf['date'], last1month_bnbdf['close'], color="blue")
            plt.plot(last1month_bnbdf['date'], last1month_bnbdf['open'], color="green")
            plt.legend(["C", "O"])
            plt.title("Binance Coin")
            counter4+=1
        elif i=='Bitcoin':
            plt.subplot(len(selected_crypto), 1, counter4)
            plt.plot(last1month_bitcoindf['date'], last1month_bitcoindf['close'])
            plt.plot(last1month_bitcoindf['date'], last1month_bitcoindf['open'])
            plt.legend(["C", "O"])
            plt.title("Bitcoin")
            counter4+=1
        elif i=='Cardano':
            plt.subplot(len(selected_crypto), 1, counter4)
            plt.plot(last1month_cardanodf['date'], last1month_cardanodf['close'], color="black")
            plt.plot(last1month_cardanodf['date'], last1month_cardanodf['open'], color="grey")
            plt.legend(["C", "O"])
            plt.title("Cardano")
            counter4+=1
        elif i=='Dogecoin':
            plt.subplot(len(selected_crypto), 1, counter4)
            plt.plot(last1month_dogecoindf['date'], last1month_dogecoindf['close'], color="orange")
            plt.plot(last1month_dogecoindf['date'], last1month_dogecoindf['open'], color="green")
            plt.legend(["C", "O"])
            plt.title("Dogecoin")
            counter4+=1
        elif i=='Ethereum':
            plt.subplot(len(selected_crypto), 1, counter4)
            plt.plot(last1month_ethereumdf['date'], last1month_ethereumdf['close'], color="blue")
            plt.plot(last1month_ethereumdf['date'], last1month_ethereumdf['open'], color="yellow")
            plt.legend(["C", "O"])
            plt.title("Ethereum")
            counter4+=1
        elif i=='HEX':
            plt.subplot(len(selected_crypto), 1, counter4)
            plt.plot(last1month_hexdf['date'], last1month_hexdf['close'], color="purple")
            plt.plot(last1month_hexdf['date'], last1month_hexdf['open'], color="pink")
            plt.legend(["C", "O"])
            plt.title("Hex")
            counter4+=1
        elif i=='Polkadot':
            plt.subplot(len(selected_crypto), 1, counter4)
            plt.plot(last1month_dotdf['date'], last1month_dotdf['close'], color="red")
            plt.plot(last1month_dotdf['date'], last1month_dotdf['open'], color="orange")
            plt.legend(["C", "O"])
            plt.title("Polkadot")
            counter4+=1
        elif i=='Solana':
            plt.subplot(len(selected_crypto), 1, counter4)
            plt.plot(last1month_solanadf['date'], last1month_solanadf['close'], color="green")
            plt.plot(last1month_solanadf['date'], last1month_solanadf['open'], color="lightgreen")
            plt.legend(["C", "O"])
            plt.title("Solana")
            counter4+=1
        elif i=='Tether':
            plt.subplot(len(selected_crypto), 1, counter4)
            plt.plot(last1month_tetherdf['date'], last1month_tetherdf['close'], color="orange")
            plt.plot(last1month_tetherdf['date'], last1month_tetherdf['open'], color="yellow")
            plt.legend(["C", "O"])
            plt.title("Tether")
            counter4+=1
        elif i=='USDCoin':
            plt.subplot(len(selected_crypto), 1, counter4)
            plt.plot(last1month_usdcdf['date'], last1month_usdcdf['close'], color="pink")
            plt.plot(last1month_usdcdf['date'], last1month_usdcdf['open'], color="purple")
            plt.legend(["C", "O"])
            plt.title("USD Coin")
            counter4+=1
        elif i=='XRP':
            plt.subplot(len(selected_crypto), 1, counter4)
            plt.plot(last1month_xrpdf['date'], last1month_xrpdf['close'], color="brown")
            plt.plot(last1month_xrpdf['date'], last1month_xrpdf['open'], color="red")
            plt.legend(["C", "O"])
            plt.title("Ripple")
            counter4+=1
        plt.subplots_adjust(hspace=1.2)

    canvas = FigureCanvasTkAgg(fig, master=cop)
    canvas.draw()
    canvas.get_tk_widget().pack()

def plot_graph_5():
    ma = tk.Tk() 
    ma.title('Moving Average') 
    ma.geometry("500x500")
    fig = plt.figure(figsize=(15, 30))

    counter5 = 1
    l = len(selected_crypto)
    n = (l//2)+1
    for i in selected_crypto:
        if i=='BinanceCoin':
            plt.subplot(n, 2, counter5)
            plt.plot(bnbdf['date'], bnbdf['close'].rolling(50).mean(), color="blue")
            plt.plot(bnbdf['date'], bnbdf['close'].rolling(200).mean(), color="green")
            plt.title('Binance Coin Close Price Moving Average')
            counter5+=1
        elif i=='Bitcoin':
            plt.subplot(n, 2, counter5)
            plt.plot(bitcoindf['date'], bitcoindf['close'].rolling(50).mean())
            plt.plot(bitcoindf['date'], bitcoindf['close'].rolling(200).mean())
            plt.title('Bitcoin Close Price moving average')
            counter5+=1
        elif i=='Cardano':
            plt.subplot(n, 2, counter5)
            plt.plot(cardanodf['date'], cardanodf['close'].rolling(50).mean(), color="black")
            plt.plot(cardanodf['date'], cardanodf['close'].rolling(200).mean(), color="red")
            plt.title('Cardano Close Price moving average')
            counter5+=1
        elif i=='Dogecoin':
            plt.subplot(n, 2, counter5)
            plt.plot(dogecoindf['date'], dogecoindf['close'].rolling(50).mean(), color="orange")
            plt.plot(dogecoindf['date'], dogecoindf['close'].rolling(200).mean(), color="grey")
            plt.title('Dogecoin Close Price moving average')
            counter5+=1
        elif i=='Ethereum':
            plt.subplot(n, 2, counter5)
            plt.plot(ethereumdf['date'], ethereumdf['close'].rolling(50).mean(), color="green")
            plt.plot(ethereumdf['date'], ethereumdf['close'].rolling(200).mean(), color="blue")
            plt.title('Ethereum Close Price moving average')
            counter5+=1
        elif i=='HEX':
            plt.subplot(n, 2, counter5)
            plt.plot(hexdf['date'], hexdf['close'].rolling(50).mean(), color="purple")
            plt.plot(hexdf['date'], hexdf['close'].rolling(200).mean(), color="pink")
            plt.title('Hex Close Price Moving Average')
            counter5+=1
        elif i=='Polkadot':
            plt.subplot(n, 2, counter5)
            plt.plot(dotdf['date'], dotdf['close'].rolling(50).mean(), color="red")
            plt.plot(dotdf['date'], dotdf['close'].rolling(200).mean(), color="orange")
            plt.title('Polkadot Close Price Moving Average')
            counter5+=1
        elif i=='Solana':
            plt.subplot(n, 2, counter5)
            plt.plot(solanadf['date'], solanadf['close'].rolling(50).mean(), color="green")
            plt.plot(solanadf['date'], solanadf['close'].rolling(200).mean(), color="lightgreen")
            plt.title('Solana Close Price Moving Average')
            counter5+=1
        elif i=='Tether':
            plt.subplot(n, 2, counter5)
            plt.plot(tetherdf['date'], tetherdf['close'].rolling(50).mean(), color="orange")
            plt.plot(tetherdf['date'], tetherdf['close'].rolling(200).mean(), color="yellow")
            plt.title('Tether Close Price moving average')
            counter5+=1
        elif i=='USDCoin':
            plt.subplot(n, 2, counter5)
            plt.plot(usdcdf['date'], usdcdf['close'].rolling(50).mean(), color="pink")
            plt.plot(usdcdf['date'], usdcdf['close'].rolling(200).mean(), color="purple")
            plt.title('USD Coin Close Price moving average')
            counter5+=1
        elif i=='XRP':
            plt.subplot(n, 2, counter5)
            plt.plot(xrpdf['date'], xrpdf['close'].rolling(50).mean(), color="brown")
            plt.plot(xrpdf['date'], xrpdf['close'].rolling(200).mean(), color="red")
            plt.title('Ripple Close Price moving average')
            counter5+=1
        plt.subplots_adjust(hspace=1.2)
        
    canvas = FigureCanvasTkAgg(fig, master=ma)
    canvas.draw()
    canvas.get_tk_widget().pack()

def plot_graph_6():
    cp = tk.Tk() 
    cp.title('Close Price Histogram') 
    cp.geometry("500x500")
    fig = plt.figure(figsize=(15, 30))

    counter6 = 1
    for i in selected_crypto:
        if i=='BinanceCoin':
            plt.subplot(len(selected_crypto), 1, counter6)
            sns.histplot(bnbdf['close'],color='darkblue', kde=True)
            plt.axvline(bnbdf['close'].mean(), color='k', linestyle='dashed', linewidth=2)
            plt.text(500,150,'Binance Coin Close Price', fontsize=16)
            counter6+=1
        elif i=='Bitcoin':
            plt.subplot(len(selected_crypto), 1, counter6)
            sns.histplot(bitcoindf['close'],color='darkred', kde=True)
            plt.axvline(bitcoindf['close'].mean(), color='k', linestyle='dashed', linewidth=2)
            plt.text(50000,400,'Bitcoin Close Price', fontsize=16)
            counter6+=1
        elif i=='Cardano':
            plt.subplot(len(selected_crypto), 1, counter6)
            sns.histplot(cardanodf['close'],color='darkgreen', kde=True)
            plt.axvline(cardanodf['close'].mean(), color='k', linestyle='dashed', linewidth=2)
            plt.text(2.3,200,'Cardano Close Price', fontsize=16)
            counter6+=1
        elif i=='Dogecoin':
            plt.subplot(len(selected_crypto), 1, counter6)
            sns.histplot(dogecoindf['close'],color='grey', kde=True)
            plt.axvline(dogecoindf['close'].mean(), color='k', linestyle='dashed', linewidth=2)
            plt.text(0.52,200,'Dogecoin Close Price', fontsize=16)
            counter6+=1
        elif i=='Ethereum':
            plt.subplot(len(selected_crypto), 1, counter6)
            sns.histplot(ethereumdf['close'],color='darkorange', kde=True)
            plt.axvline(ethereumdf['close'].mean(), color='k', linestyle='dashed', linewidth=2)
            plt.text(3100,400,'Ethereum Close Price', fontsize=16)
            counter6+=1
        elif i=='HEX':
            plt.subplot(len(selected_crypto), 1, counter6)
            sns.histplot(hexdf['close'],color='purple', kde=True)
            plt.axvline(hexdf['close'].mean(), color='k', linestyle='dashed', linewidth=2)
            plt.text(0.25,80,'Hex Close Price', fontsize=16)
            counter6+=1
        elif i=='Polkadot':
            plt.subplot(len(selected_crypto), 1, counter6)
            sns.histplot(dotdf['close'],color='darkred', kde=True)
            plt.axvline(dotdf['close'].mean(), color='k', linestyle='dashed', linewidth=2)
            plt.text(30,70,'Polkadot Close Price', fontsize=16)
            counter6+=1
        elif i=='Solana':
            plt.subplot(len(selected_crypto), 1, counter6)
            sns.histplot(solanadf['close'],color='darkgreen', kde=True)
            plt.axvline(solanadf['close'].mean(), color='k', linestyle='dashed', linewidth=2)
            plt.text(20,80,'Solana Close Price', fontsize=16)
            counter6+=1
        elif i=='Tether':
            plt.subplot(len(selected_crypto), 1, counter6)
            sns.histplot(tetherdf['close'],color='darkorange', kde=True)
            plt.axvline(tetherdf['close'].mean(), color='k', linestyle='dashed', linewidth=2)
            plt.text(1, 300, 'Tether Close Price', fontsize=16)
            counter6+=1
        elif i=='USDCoin':
            plt.subplot(len(selected_crypto), 1, counter6)
            sns.histplot(usdcdf['close'],color='pink', kde=True)
            plt.axvline(usdcdf['close'].mean(), color='k', linestyle='dashed', linewidth=2)
            plt.text(0.99, 200, 'USD Coin Close Price', fontsize=16)
            counter6+=1
        elif i=='XRP':
            plt.subplot(len(selected_crypto), 1, counter6)
            sns.histplot(xrpdf['close'],color='brown', kde=True)
            plt.axvline(xrpdf['close'].mean(), color='k', linestyle='dashed', linewidth=2)
            plt.text(1.5, 300, 'Ripple Close Price', fontsize=16)
            counter6+=1
        plt.subplots_adjust(hspace=1.2)

    canvas = FigureCanvasTkAgg(fig, master=cp)
    canvas.draw()
    canvas.get_tk_widget().pack()
    
def create_welcome_page():
    # Create the main window
    root = tk.Tk()
    root.title("Cryptic Nexus")
    root.geometry("500x500")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_coordinate = (screen_width - 500) // 2
    y_coordinate = (screen_height - 500) // 2

    # Set the window's position
    root.geometry(f"500x500+{x_coordinate}+{y_coordinate}")

    # Label with the text "Welcome to Cryptograph"
    label = tk.Label(root, text="Welcome to Cryptic Nexus", font=("Cabin Sketch", 24))
    label.pack(pady=20)

    # "Next" button to transition to the new page
    next_button = tk.Button(root, text="Proceed",font=("Berlin Sans FB", 12), command=create_new_page)
    next_button.pack(pady=10)

    # "Exit" button to close the application
    exit_button = tk.Button(root, text="Exit",font=("Berlin Sans FB", 12), command=root.destroy)
    exit_button.pack()

    root.mainloop()

def create_new_page():
    new_page = tk.Toplevel()
    new_page.title("Welcome")
    new_page.geometry("500x500")
    screen_width = new_page.winfo_screenwidth()
    screen_height = new_page.winfo_screenheight()

    x_coordinate = (screen_width - 500) // 2
    y_coordinate = (screen_height - 500) // 2

    # Set the window's position
    new_page.geometry(f"500x500+{x_coordinate}+{y_coordinate}")
    
    # Label with the text "Welcome to Cryptograph"
    label = tk.Label(new_page, text="What do you want to do?", font=("Cabin Sketch", 24))
    label.pack(pady=20)
    
    # "Compare" button
    compare_button = tk.Button(new_page, text="Compare",font=("Berlin Sans FB", 12),command=create_crypto_selection_page)
    compare_button.pack(pady=10)

    # "Predict" button
    predict_button = tk.Button(new_page, text="Predict",font=("Berlin Sans FB", 12),command=create_crypto_prediction_page)
    predict_button.pack()
    
def create_crypto_prediction_page():
    crypto_prediction_page = tk.Toplevel()
    crypto_prediction_page.title("Crypto Prediction Page")
    crypto_prediction_page.geometry("500x500")
    screen_width = crypto_prediction_page.winfo_screenwidth()
    screen_height = crypto_prediction_page.winfo_screenheight()

    x_coordinate = (screen_width - 500) // 2
    y_coordinate = (screen_height - 500) // 2

    # Set the window's position
    crypto_prediction_page.geometry(f"500x500+{x_coordinate}+{y_coordinate}")
    
    # Label with the text "Welcome to Cryptograph"
    label = tk.Label(crypto_prediction_page, text="Select ONE Cryptocurrency", font=("Cabin Sketch", 24))
    label.pack(pady=20)
    
    def print_selected_option():
        selected_option = variable.get()
        if selected_option=='BinanceCoin':
            closedf = bnbdf[['date','close']]
        elif selected_option=='Bitcoin':
            closedf = bitcoindf[['date','close']]
        elif selected_option=='Cardano':
            closedf = cardanodf[['date','close']]
        elif selected_option=='Dogecoin':
            closedf = dogecoindf[['date','close']]
        elif selected_option=='Ethereum':
            closedf = ethereumdf[['date','close']]
        elif selected_option=='HEX':
            closedf = hexdf[['date','close']]
        elif selected_option=='Polkadot':
            closedf = dotdf[['date','close']]
        elif selected_option=='Solana':
            closedf = solanadf[['date','close']]
        elif selected_option=='Tether':
            closedf = tetherdf[['date','close']]
        elif selected_option=='USDCoin':
            closedf = usdcdf[['date','close']]
        elif selected_option=='XRP':
            closedf = xrpdf[['date','close']] 
        
        import numpy as np            
        closedf = closedf[closedf['date'] > '2020-09-13']
        close_stock = closedf.copy()
        del closedf['date']
        scaler=MinMaxScaler(feature_range=(0,1))
        closedf=scaler.fit_transform(np.array(closedf).reshape(-1,1))
        training_size=int(len(closedf)*0.70)
        test_size=len(closedf)-training_size
        train_data,test_data=closedf[0:training_size,:],closedf[training_size:len(closedf),:1]
        
        tt = tk.Tk() 
        tt.title('Train and Test Data') 
        tt.geometry("800x600")

        fig, ax = plt.subplots(figsize=(15, 6))
        sns.lineplot(x=close_stock['date'][:255], y=close_stock['close'][:255], color='black', ax=ax)
        sns.lineplot(x=close_stock['date'][255:], y=close_stock['close'][255:], color='red', ax=ax)

        # Formatting
        ax.set_title('Train & Test data', fontsize=20, loc='center', fontdict=dict(weight='bold'))
        ax.set_xlabel('Date', fontsize=16, fontdict=dict(weight='bold'))
        ax.set_ylabel('Weekly Sales', fontsize=16, fontdict=dict(weight='bold'))
        plt.tick_params(axis='y', which='major', labelsize=16)
        plt.tick_params(axis='x', which='major', labelsize=16)
        plt.legend(loc='upper right', labels=('train', 'test'))
            
        canvas = FigureCanvasTkAgg(fig, master=tt)
        canvas.draw()
        canvas.get_tk_widget().pack()
        
        def create_dataset(dataset, time_step=1):
            dataX, dataY = [], []
            for i in range(len(dataset)-time_step-1):
                a = dataset[i:(i+time_step), 0]   ###i=0, 0,1,2,3-----99   100 
                dataX.append(a)
                dataY.append(dataset[i + time_step, 0])
            return np.array(dataX), np.array(dataY)
        time_step = 15
        X_train, y_train = create_dataset(train_data, time_step)
        X_test, y_test = create_dataset(test_data, time_step)
        
        from xgboost import XGBRegressor
        
        my_model = XGBRegressor(n_estimators=1000)
        my_model.fit(X_train, y_train, verbose=False)
        
        predictions = my_model.predict(X_test)
        
        train_predict=my_model.predict(X_train)
        test_predict=my_model.predict(X_test)

        train_predict = train_predict.reshape(-1,1)
        test_predict = test_predict.reshape(-1,1)
        
        train_predict = scaler.inverse_transform(train_predict)
        test_predict = scaler.inverse_transform(test_predict)
        
        original_ytrain = scaler.inverse_transform(y_train.reshape(-1,1)) 
        original_ytest = scaler.inverse_transform(y_test.reshape(-1,1)) 
        
        from plotly.subplots import make_subplots
        import plotly.graph_objs as go
        import pandas as pd
        import numpy as np
        from itertools import cycle

        look_back=time_step
        trainPredictPlot = np.empty_like(closedf)
        trainPredictPlot[:, :] = np.nan
        trainPredictPlot[look_back:len(train_predict)+look_back, :] = train_predict
            
        # shift test predictions for plotting
        testPredictPlot = np.empty_like(closedf)
        testPredictPlot[:, :] = np.nan
        testPredictPlot[len(train_predict)+(look_back*2)+1:len(closedf)-1, :] = test_predict

        names = cycle(['Original close price','Train predicted close price','Test predicted close price'])

        plotdf = pd.DataFrame({'date': close_stock['date'],
                            'original_close': close_stock['close'],
                            'train_predicted_close': trainPredictPlot.reshape(1,-1)[0].tolist(),
                            'test_predicted_close': testPredictPlot.reshape(1,-1)[0].tolist()})

        fig = px.line(plotdf,x=plotdf['date'], y=[plotdf['original_close'],plotdf['train_predicted_close'],
                                                plotdf['test_predicted_close']],
                    labels={'value':'Close price','date': 'Date'})
        fig.update_layout(title_text='Comparision between original close price vs predicted close price',
                        plot_bgcolor='white', font_size=15, font_color='black',legend_title_text='Close Price')
        fig.for_each_trace(lambda t:  t.update(name = next(names)))

        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        fig.show()

        # Creating a Tkinter window
        root = tk.Tk()
        root.title("Plot in Tkinter")

        # Function to embed Plotly plot into Tkinter window
        def plot_to_tkinter(fig):
            # Convert Plotly figure to HTML
            plotly_html = fig.to_html(full_html=False)

            # Embed HTML in a Tkinter window
            plot_frame = tk.Frame(root, width=800, height=600)
            plot_frame.grid(row=0, column=0)

            # Create a HTML widget to display the Plotly plot
            html_widget = tk.Label(plot_frame)
            html_widget.grid(row=0, column=0)
            html_widget.configure(text=plotly_html)

        # Function to display the plot in the Tkinter window
        def display_plot():
            plot_to_tkinter(fig)

        # Call the function to display the plot
        display_plot()

        # Start the Tkinter main loop
        root.destroy()
        x_input=test_data[len(test_data)-time_step:].reshape(1,-1)
        temp_input=list(x_input)
        temp_input=temp_input[0].tolist()

        from numpy import array

        lst_output=[]
        n_steps=time_step
        i=0
        pred_days = 10
        while(i<pred_days):
            
            if(len(temp_input)>time_step):
                
                x_input=np.array(temp_input[1:])
                #print("{} day input {}".format(i,x_input))
                x_input=x_input.reshape(1,-1)
                
                yhat = my_model.predict(x_input)
                #print("{} day output {}".format(i,yhat))
                temp_input.extend(yhat.tolist())
                temp_input=temp_input[1:]
            
                lst_output.extend(yhat.tolist())
                i=i+1
                
            else:
                yhat = my_model.predict(x_input)
                
                temp_input.extend(yhat.tolist())
                lst_output.extend(yhat.tolist())
                
                i=i+1
        last_days=np.arange(1,time_step+1)
        day_pred=np.arange(time_step+1,time_step+pred_days+1)
        
        temp_mat = np.empty((len(last_days)+pred_days+1,1))
        temp_mat[:] = np.nan
        temp_mat = temp_mat.reshape(1,-1).tolist()[0]

        last_original_days_value = temp_mat
        next_predicted_days_value = temp_mat

        last_original_days_value[0:time_step+1] = scaler.inverse_transform(closedf[len(closedf)-time_step:]).reshape(1,-1).tolist()[0]
        next_predicted_days_value[time_step+1:] = scaler.inverse_transform(np.array(lst_output).reshape(-1,1)).reshape(1,-1).tolist()[0]

        new_pred_plot = pd.DataFrame({
            'last_original_days_value':last_original_days_value,
            'next_predicted_days_value':next_predicted_days_value
        })

        names = cycle(['Last 15 days close price','Predicted next 10 days close price'])

        fig2 = px.line(new_pred_plot,x=new_pred_plot.index, y=[new_pred_plot['last_original_days_value'],
                                                            new_pred_plot['next_predicted_days_value']],
                    labels={'value': 'Close price','index': 'Timestamp'})
        fig2.update_layout(title_text='Compare last 15 days vs next 10 days',
                        plot_bgcolor='white', font_size=15, font_color='black',legend_title_text='Close Price')
        fig2.for_each_trace(lambda t:  t.update(name = next(names)))
        fig2.update_xaxes(showgrid=False)
        fig2.update_yaxes(showgrid=False)
        fig2.show()

        # Function to embed Plotly plot into Tkinter window
        def plot_to_tkinter(fig):
            # Convert Plotly figure to HTML
            plotly_html = fig.to_html(full_html=False)

            # Embed HTML in a Tkinter window
            plot_frame = tk.Frame(root, width=800, height=600)
            plot_frame.grid(row=0, column=0)

            # Create a HTML widget to display the Plotly plot
            html_widget = tk.Label(plot_frame)
            html_widget.grid(row=0, column=0)
            html_widget.configure(text=plotly_html)

        # Function to display the plot in the Tkinter window
        def plot_to_tkinter(fig, row, column):
            plotly_html = fig.to_html(full_html=False)
            html_widget = tk.Label(root)
            html_widget.grid(row=row, column=column)
            html_widget.configure(text=plotly_html)

        # Function to display both plots in the Tkinter window
        def display_plots():
            plot_to_tkinter(fig, 0, 0)  # Display the first plot at (row=0, column=0)

            fig2 = px.line(new_pred_plot, x=new_pred_plot.index, y=[new_pred_plot['last_original_days_value'],
                                                                    new_pred_plot['next_predicted_days_value']],
                            labels={'value': 'Close price', 'index': 'Timestamp'})
            fig2.update_layout(title_text='Compare last 15 days vs next 10 days',
                            plot_bgcolor='white', font_size=15, font_color='black', legend_title_text='Close Price')
            names = cycle(['Last 15 days close price', 'Predicted next 10 days close price'])
            fig2.for_each_trace(lambda t: t.update(name=next(names)))
            fig2.update_xaxes(showgrid=False)
            fig2.update_yaxes(showgrid=False)

            plot_to_tkinter(fig2, 1, 0)  # Display the second plot below the first one

        # Creating a Tkinter window
        root = tk.Tk()
        root.title("Plots in Tkinter")

        # Call the function to display the plots
        display_plots()

        # Start the Tkinter main loop
        root.destroy()
        my_model=closedf.tolist()
        my_model.extend((np.array(lst_output).reshape(-1,1)).tolist())
        my_model=scaler.inverse_transform(my_model).reshape(1,-1).tolist()[0]

        names = cycle(['Close Price'])

        fig = px.line(my_model,labels={'value': 'Close price','index': 'Timestamp'})
        fig.update_layout(title_text='Plotting whole closing price with prediction',
                        plot_bgcolor='white', font_size=15, font_color='black',legend_title_text='Stock')
        fig.for_each_trace(lambda t:  t.update(name = next(names)))
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        fig.show()
        
        
    options = ["BinanceCoin", "Bitcoin", "Cardano", "Dogecoin", "Ethereum", "HEX", "Polkadot", "Solana", "Tether", "USDCoin", "XRP"]

    variable = tk.StringVar(crypto_prediction_page)
    variable.set(options[0])  # Set default value

    dropdown = tk.OptionMenu(crypto_prediction_page, variable, *options)
    dropdown.pack()

    select_button = tk.Button(crypto_prediction_page, text="Select", command=print_selected_option)
    select_button.pack()


def create_crypto_selection_page():
    selected_crypto.clear()
    crypto_selection_page = tk.Toplevel()
    crypto_selection_page.title("Crypto Selection Page")
    crypto_selection_page.geometry("500x500")
    screen_width = crypto_selection_page.winfo_screenwidth()
    screen_height = crypto_selection_page.winfo_screenheight()

    x_coordinate = (screen_width - 500) // 2
    y_coordinate = (screen_height - 500) // 2

    # Set the window's position
    crypto_selection_page.geometry(f"500x500+{x_coordinate}+{y_coordinate}")
    
    crypto_list = [
        "BinanceCoin", "Bitcoin", "Cardano", "Dogecoin", "Ethereum",
        "HEX", "Polkadot", "Solana", "Tether", "USDCoin", "XRP"
    ]
        
    def show_selected_crypto():
        selected_text = ", ".join(selected_crypto)
        selected_label.config(text=selected_text, wraplength=480)

    def compare_crypto():
        crypto_selection_page.destroy()
        compare_page = tk.Toplevel()
        compare_page.title("Compare and Graph")
        compare_page.geometry("600x600")
        screen_width = compare_page.winfo_screenwidth()
        screen_height = compare_page.winfo_screenheight()

        x_coordinate = (screen_width - 600) // 2
        y_coordinate = (screen_height - 600) // 2

        # Set the window's position
        compare_page.geometry(f"600x600+{x_coordinate}+{y_coordinate}")
        
        compare_label = tk.Label(compare_page, text="Selected Cryptocurrencies: \n" + "\n".join(selected_crypto), font=("Berlin Sans FB", 18))
        compare_label.pack()
        
        label = tk.Label(compare_page, text="Which Graph do you want to plot?", font=("Cabin Sketch", 24))
        label.pack(pady=20)
    
        button1 = tk.Button(compare_page, text="Total CP",font=("Berlin Sans FB", 12),command=plot_graph_1)
        button2 = tk.Button(compare_page, text="Latest CP",font=("Berlin Sans FB", 12),command=plot_graph_2)
        button3 = tk.Button(compare_page, text="Volume",font=("Berlin Sans FB", 12),command=plot_graph_3)
        button4 = tk.Button(compare_page, text="COP",font=("Berlin Sans FB", 12),command=plot_graph_4)
        button5 = tk.Button(compare_page, text="Moving Average",font=("Berlin Sans FB", 12),command=plot_graph_5)
        button6 = tk.Button(compare_page, text="CP Histogram",font=("Berlin Sans FB", 12),command=plot_graph_6)

        button1.pack(side="left",padx=10)
        button2.pack(side="left",padx=10)
        button3.pack(side="left",padx=10)
        button4.pack(side="left",padx=10)
        button5.pack(side="left",padx=10)
        button6.pack(side="left",padx=10,pady=10)
        
    selection_label = tk.Label(crypto_selection_page, text="Select Cryptocurrencies:")
    selection_label.pack()

    crypto_checkboxes = []

    for crypto in crypto_list:
        var = tk.BooleanVar()
        checkbox = tk.Checkbutton(crypto_selection_page, text=crypto, variable=var, command=lambda crypto=crypto: on_checkbox_click(crypto))
        checkbox.pack()
        crypto_checkboxes.append((crypto, var))

    selected_label = tk.Label(crypto_selection_page, text="")
    selected_label.pack()

    compare_button = tk.Button(crypto_selection_page, text="Next",font=("Berlin Sans FB", 12), command=compare_crypto)
    compare_button.pack()

    def on_checkbox_click(crypto):
        if crypto in selected_crypto:
            selected_crypto.remove(crypto)
        else:
            selected_crypto.append(crypto)
        show_selected_crypto()

if __name__ == "__main__":
    create_welcome_page()