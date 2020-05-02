import webbrowser, sys, bs4, requests, time, numpy as np, re
from django.shortcuts import render

# Create your views here.
def index(request):
    url = 'https://cifraclub.com.br'

    header = {'Accept-Encoding': 'gzip, deflate, sdch',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',}

    res = requests.get(url)

    bs4res = bs4.BeautifulSoup(res.text, "html.parser")

    all_letter = []
    for link in bs4res.find_all(href=re.compile('/letra/')):
        all_letter.append(url + link.get('href'))

    return render(request, 'scrapy/index.html', {'result': all_letter})
