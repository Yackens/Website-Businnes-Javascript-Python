from .models import Link

def context_dic(request):
    dic = {}
    links = Link.objects.all()
    for link in links:
        dic[link.key] = link.url
    return dic