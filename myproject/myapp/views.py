from django.shortcuts import render

# Create your views here.

def layout(request):
    return render(request,'myapp/layout.html')

def layout2(request):
    return render(request,'myapp/layout2.html')