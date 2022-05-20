from django.shortcuts import render
import requests


def index(request):
    curr_table = requests.get('https://api.exchangerate-api.com/v4/latest/usd').json()
    curr_table = curr_table['rates']
    if request.method == 'POST':
        amount = float(request.POST.get('amount') or 0)
        curr_from = request.POST.get('curr_from')
        curr_to = request.POST.get('curr_to')
        total = round((curr_table[curr_to]/curr_table[curr_from])*amount, 2)

        context = {
            'amount': amount,
            'curr_from': curr_from,
            'curr_to': curr_to,
            'total': total,
            'curr_table': curr_table,
        }
        return render(request, 'exchange/index.html', context)
    else:
        return render(request, 'exchange/index.html', {'curr_table': curr_table})
