from django.shortcuts import render,HttpResponse
import joblib
# Create your views here.
def index(request):
    return(render(request,'index.html'))

def result(request):
    cls=joblib.load('social_network_model.sav')
    li=[]
    lis=[]
    #gender=request.POST.get['gender']
    #age=request.POST.get['age']
    #salary=request.POST.get['salary']
    gender=request.GET['gender']
    age=request.GET['age']
    salary=request.GET['salary']
    gender=int(gender)
    age=int(age)
    salary=int(salary)
    #Applying standard scaler
    standard_deviation_age=10.4697
    standard_deviation_salary=34054.3124
    mean_age=37.655
    mean_salary=69742.5
    lis.append(gender)
    lis.append((age-mean_age)/standard_deviation_age)
    lis.append((salary-mean_salary)/standard_deviation_salary)
    li.append(lis)
    ans=cls.predict(li)
    string=" "
    if ans==1:
        string="This person will buy our product"
    else:
        string="This person will not buy our product"
    return(render(request,'result.html',{'ans':string}))


