import re
from django.http import JsonResponse
from django.core import serializers
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.db import models
from .forms import StockForm
from .models import stock
from .models import profitReturns

def hello_there(request, name):
    return render(
        request,
        'stocks/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

# Replace the existing home function with the one below
def home(request):
    form = StockForm()
    stocks = stock.objects.all()
    return render(request, "stocks/home.html", {"form": form, "stocks": stocks})

def postStock(request):
    # request should be ajax and method should be POST.
    posts = stock.objects.all()
    response_data = {}
    req = request.method

    if request.method == "POST":
        stocksym = request.POST.get('stocksym')
        allotment = request.POST.get('allotment')
        final_share_price = request.POST.get('final_share_price')
        sell_comm = request.POST.get('sell_comm')
        initial_share_price = request.POST.get('initial_share_price')
        buy_comm = request.POST.get('buy_comm')
        capital_gain_tax_rate = request.POST.get('capital_gain_tax_rate')
        
        pr = profitReturns.objects.all()
        proceeds= int(allotment)*float(final_share_price)
        cost=(int(allotment)*float(initial_share_price))+float(sell_comm)+float(buy_comm)+(0.15*((float(final_share_price)-float(initial_share_price))*int(allotment)-float(buy_comm)-float(sell_comm)))
        net_profit=(float(final_share_price)*float(allotment))-float(cost)
        roi=(float(net_profit/cost)*100)
        bep=(int(allotment) * float(initial_share_price) + float(buy_comm) + float(sell_comm)) / int(allotment)
        response_data['proceeds'] = proceeds
        response_data['cost'] = cost
        response_data['net_profit'] = net_profit
        response_data['return_on_investment'] = roi
        response_data['break_even_price'] = bep
              
        
    return JsonResponse({"instance": response_data}, status=200)   

    
     


