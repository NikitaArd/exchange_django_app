from django.shortcuts import render


def page_not_found(reqeust, exception):
    return render(reqeust, 'exchange/404.html', status=404)
