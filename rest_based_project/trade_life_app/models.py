from django.db import models


class Trade(models.Model):
    ccy = models.CharField(max_length=20)
    ccy_rounding_places = models.FloatField()
    ccy_rounding_direction = models.FloatField()
    index = models.CharField(max_length=20)
    notional = models.FloatField()
    spread = models.FloatField()
    start = models.DateField()
    maturity = models.DateField()
    payhols = models.CharField(max_length=20)
    paymarch = models.CharField(max_length=20)
    trade_id = models.CharField(max_length=20)
    product_type = models.CharField(max_length=50)
    trade_date = models.DateField()

    def __str__(self):
        return self.trade_id + " of type : " + self.product_type
