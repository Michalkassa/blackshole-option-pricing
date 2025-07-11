from scipy.stats import norm
from numpy import log, sqrt, exp

class BlackScholes:
    def __init__(self, stock_price: float, strike: float, interest_rate: float, time_to_maturity: float, volatility: float):
        self.time_to_maturity = time_to_maturity
        self.strike = strike
        self.stock_price = stock_price
        self.volatility = volatility
        self.interest_rate = interest_rate

    def calculate(self,):
        time_to_maturity = self.time_to_maturity
        strike = self.strike
        stock_price = self.stock_price
        volatility = self.volatility
        interest_rate = self.interest_rate

        d1 = ((log(stock_price/strike) + (interest_rate + 0.5 * volatility ** 2))*time_to_maturity) / (volatility * sqrt(time_to_maturity))
        d2 = d1 - volatility * sqrt(time_to_maturity)
        call = stock_price * norm.cdf(d1) - (strike * exp(-(interest_rate* time_to_maturity)) * norm.cdf(d2))
        put = (strike * exp(-interest_rate*time_to_maturity) * norm.cdf(-d2)) - (stock_price* norm.cdf(-d1))

        self.call = round(call, 2)
        self.put = round(put, 2)

        return call, put


model = BlackScholes(
    time_to_maturity=1,
    strike=100,
    stock_price=100,
    volatility=0.2,
    interest_rate=0.05)

model.calculate()
print(model.call)
print(model.put)