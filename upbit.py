import requests
import json
import pandas as pd
import random
from mplfinance.original_flavor import candlestick2_ohlc
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

class upBit:
    def getCoinList():
        data_all = requests.get("https://api.upbit.com/v1/market/all?isDetails=false")
        coin_list = json.loads(data_all.text)
        return coin_list

    def findCoinCode(name):
        data_all = requests.get("https://api.upbit.com/v1/market/all?isDetails=false")
        coin_list = json.loads(data_all.text)
        for coin in coin_list:
            if name == coin["korean_name"]:
                if coin["market"][0] == 'K':
                    return coin["market"]
            else:
                continue
        return 'error'

    def getCoinDetail(code):
        url = "https://api.upbit.com/v1/ticker?markets={}".format(code)
        req_data = requests.get(url)
        try:
            coin_data = json.loads(req_data.text)
            return coin_data
        except:
            return 'error'
        # for key, value in coin_data[0].items():
        #     print(key, ":", value)

    def getMinuteCandle(code):
        url = "https://api.upbit.com/v1/candles/minutes/1"
        querystring = {"market": code, "count": 2}
        response = requests.get(url, params=querystring)
        candle_data = json.loads(response.text)
        return candle_data

    def getPercent(firstVal, secondVal):
        diff = abs(firstVal - secondVal)
        if firstVal > secondVal:
            result = round(diff / firstVal * 100 * -1, 2)
            return result
        else:
            result = round(diff / firstVal * 100, 2)
            return result

    def getDaily(code):
        url = "https://api.upbit.com/v1/candles/days"
        querystring = {"market": code, "count": 1}
        response = requests.get(url, params=querystring)
        candle_data = json.loads(response.text)
        return candle_data

    def yatchacha(dt, market, name):
        try:
            link = 'https://upbit.com/exchange?code=CRIX.UPBIT.{}'.format(market)
            tdprice = format(dt["trade_price"], ',')
            udrate = format(dt["change_rate"] * 100, '.2f')
            if udrate == '0.00':
                udprice = '0.00'
            else:
                udprice = format(dt["change_price"], ',')
            if dt["change_rate"] > 0:
                updown = "{} {} (전일대비 +{}% ({}))".format(market, tdprice, udrate, udprice)
                upstat = 1
                newtitle = "{} {} ({}%)".format(name, tdprice, udrate)
            elif dt["change_rate"] < 0:
                updown = "{} {} (전일대비 {}% ({}))".format(market, tdprice, udrate, udprice)
                upstat = -1
                newtitle = "{} {} ({}%)".format(name, tdprice, udrate)
            else:
                updown = "{} {} (전일대비 {}% ({}))".format(market, tdprice, udrate, udprice)
                upstat = 0
                newtitle = "{} {} ({}%)".format(name, tdprice, udrate)
            data = {
                "거래량": format(int(dt["candle_acc_trade_volume"]), ','),
                "거래대금": format(int(dt["candle_acc_trade_price"]), ','),
                "시가": format(dt["opening_price"], ','),
                "고가": format(dt["high_price"], ','),
                "저가": format(dt["low_price"], ','),
                "전일종가": format(dt["prev_closing_price"], ','),
                "업비트링크": link
            }
            realData = [
                data, updown, upstat, newtitle
            ]
        except:
            return 'error'
        return realData

    def get_candle(coin, type, term, min = 1):
        if type == 'd':
            link = "https://api.upbit.com/v1/candles/days"
            params = {
                "count": term,
                "market": coin
            }
            response = requests.get(link, params=params)
            response = json.loads(response.text)
            data = []
            for r in response:
                temp_data = {
                    "Date": r["candle_date_time_kst"][5:10],
                    "open": float(r["opening_price"]),
                    "high": float(r["high_price"]),
                    "low": float(r["low_price"]),
                    "close": float(r["trade_price"]),
                }
                data.append(temp_data)
            df = pd.DataFrame(data, columns=['Date', 'open', 'high', 'low', 'close'])
            df = df[::-1]
            fig = plt.figure(figsize=(12, 8))
            ax = fig.add_subplot(111)
            ax.set_title(coin, fontsize=22)
            ax.xaxis.set_major_locator(plt.MaxNLocator(20))
            ax.set_xlabel('Date')
            ax.plot(df['Date'], df['close'])
            ax.ticklabel_format(axis='y', style='plain')
            plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.1f}'))  # No decimal places
            candlestick2_ohlc(ax, df['open'], df['high'], df['low'], df['close'], width=0.5, colorup='r', colordown='b')
            plt.grid()
            newdir = 'img/output{}.png'.format(random.randint(100,999))
            plt.savefig(newdir)
            print(newdir)
            return newdir
        elif type == 'm':
            link = "https://api.upbit.com/v1/candles/minutes/{}".format(min)
            params = {
                "count": term,
                "market": coin
            }
            response = requests.get(link, params=params)
            response = json.loads(response.text)
            data = []
            if int(min) >= 15:
                for r in response:
                    temp_data = {
                        "Date": r["candle_date_time_kst"],
                        "open": float(r["opening_price"]),
                        "high": float(r["high_price"]),
                        "low": float(r["low_price"]),
                        "close": float(r["trade_price"]),
                    }
                    data.append(temp_data)
                maxloc = 5
            else:
                for r in response:
                    temp_data = {
                        "Date": r["candle_date_time_kst"][11:19],
                        "open": float(r["opening_price"]),
                        "high": float(r["high_price"]),
                        "low": float(r["low_price"]),
                        "close": float(r["trade_price"]),
                    }
                    data.append(temp_data)
                maxloc = 15
            df = pd.DataFrame(data, columns=['Date', 'open', 'high', 'low', 'close'])
            df = df[::-1]
            fig = plt.figure(figsize=(12, 8))
            ax = fig.add_subplot(111)
            ax.set_title(coin, fontsize=22)
            ax.xaxis.set_major_locator(plt.MaxNLocator(maxloc))
            ax.set_xlabel('Date')
            ax.plot(df['Date'], df['close'])
            ax.ticklabel_format(axis='y', style='plain')
            plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.1f}'))  # No decimal places
            candlestick2_ohlc(ax, df['open'], df['high'], df['low'], df['close'], width=0.5, colorup='r', colordown='b')
            plt.grid()
            newdir = 'img/output{}.png'.format(random.randint(100,999))
            plt.savefig(newdir)
            return newdir
        elif type == 'w' or type == 'mo':
            if type == 'w':
                link = "https://api.upbit.com/v1/candles/weeks"
            elif type == 'mo':
                link = "https://api.upbit.com/v1/candles/months"
            params = {
                "count": term,
                "market": coin
            }
            response = requests.get(link, params=params)
            response = json.loads(response.text)
            data = []
            for r in response:
                temp_data = {
                    "Date": r["candle_date_time_kst"],
                    "open": float(r["opening_price"]),
                    "high": float(r["high_price"]),
                    "low": float(r["low_price"]),
                    "close": float(r["trade_price"]),
                }
                data.append(temp_data)
            maxloc = 5
            df = pd.DataFrame(data, columns=['Date', 'open', 'high', 'low', 'close'])
            df = df[::-1]
            fig = plt.figure(figsize=(12, 8))
            ax = fig.add_subplot(111)
            ax.set_title(coin, fontsize=22)
            ax.xaxis.set_major_locator(plt.MaxNLocator(maxloc))
            ax.set_xlabel('Date')
            ax.plot(df['Date'], df['close'])
            ax.ticklabel_format(axis='y', style='plain')
            plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.1f}'))  # No decimal places
            candlestick2_ohlc(ax, df['open'], df['high'], df['low'], df['close'], width=0.5, colorup='r', colordown='b')
            plt.grid()
            newdir = 'img/output{}.png'.format(random.randint(100,999))
            plt.savefig(newdir)
            return newdir
