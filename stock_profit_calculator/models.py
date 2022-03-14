from django.db import models

# Create your models here.
class stock(models.Model):    
    stocksym = models.CharField(max_length=100, unique =  True)
    allot = models.CharField(max_length=100)
    fshare = models.CharField(max_length=100)
    scomm = models.CharField(max_length = 250)
    ishare = models.DateField(auto_now=False, auto_now_add=False)
    bcomm = models.CharField(max_length=150, null = True, blank = True)
    cgtaxrate = models.CharField(max_length=150, null = True, blank = True)

class profitReturns(models.Model):
    proceeds = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    net_profit = models.CharField(max_length=100)
    return_on_investment = models.CharField(max_length=100)
    break_even_price = models.CharField(max_length=100)