from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Rango still  says here is the about page')

def index_name(request):
    context_dict = {'variable_name':'Lifengmei','boldmessage':"Crunchy,creamy,cookie,candy,cupcake",}
    return render(request,'rango/index.html',context_dict)

def about(request):
    return render(request,'rango/about.html',)
