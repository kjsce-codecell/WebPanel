from .models import Urls
import random

def searchdb(request):
    query=request.GET.get('query','')
    print(query)
    query=query.strip()
    if query is not '':
        data=Urls.objects.filter(name__startswith=query)
    else:
        data=Urls.objects.all()

    return data,query

