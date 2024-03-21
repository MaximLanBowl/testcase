from django.db import models
import requests


class TradeInfo(models.Model):
    last = models.FloatField()
    volume = models.FloatField()
    quote_volume = models.FloatField()


class BaseExchange(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()

    def get_ticker_info(self):
        api_url = 'https://www.coingecko.com/en/exchanges/bibox'
        requests.request.__get__(api_url)
        ticker_data = {
            "BTC/USDT": TradeInfo(last=57000, base_volume=11328, quote_volume=3456789),
            "ETH/BTC": TradeInfo(last=4026, base_volume=4567, quote_volume=0)
        }
        return ticker_data

