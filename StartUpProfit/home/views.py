from django.shortcuts import render,HttpResponse
import joblib
# Create your views here.
def index(request):
    return(render(request,'index.html'))

def result(request):
    cls=joblib.load('startups.sav')
    li=[]
    lis=[]
    g=request.GET['r']
    a=request.GET['a']
    m=request.GET['m']
    g=int(g)
    a=int(a)
    m=int(m)
    #Applying standard scaler
    lis.append(g)
    lis.append(a)
    lis.append(m)
    li.append(lis)
    ans=cls.predict(li)
    res=ans[0]
    return(render(request,'result.html',{'ans':res}))


