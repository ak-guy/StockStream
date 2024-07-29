from django.shortcuts import render
from yahoo_fin.stock_info import tickers_nifty50

# Create your views here.
def stockpicker(request):
    stock_picker = tickers_nifty50()
    # print(stock_picker, flush=True) # working fine
    context = {
        'stockpicker': stock_picker
    }
    return render(request, 'base/stockpicker.html', context=context)

def stocktracker(request):
    print(request.GET.getlist('stockpicker'))
    return render(request, 'base/stocktracker.html')