import upbit
ub = upbit.upBit


class yatchacha():
    def get(name):
        targetMarket = ub.findCoinCode(name)
        if targetMarket == 'error':
            return [-1]
        else:
            detail = ub.getDaily(targetMarket)
            dt = ub.yatchacha(detail[0], targetMarket, name)
            return dt

    def chart(name, type, min = 1):
        targetMarket = ub.findCoinCode(name)
        if targetMarket == 'error':
            return [-1]
        else:
            if type == 'd':
                return ub.get_candle(targetMarket, 'd', 100)
            elif type == 'm':
                return ub.get_candle(targetMarket, 'm', 100, min)
            elif type == 'w':
                return ub.get_candle(targetMarket, 'w', 100)
            elif type == 'mo':
                return ub.get_candle(targetMarket, 'mo', 100)
            else:
                return [-1]
