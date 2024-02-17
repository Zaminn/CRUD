from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentResgisteration
from .models import User
# Create your views here.


def add_show(request):
    if request.method=='POST':
        fm=StudentResgisteration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            ps=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=ps)
            reg.save()
            fm=StudentResgisteration()
            
    else:
        fm=StudentResgisteration()  
    stud=User.objects.all()  
    return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud })


def del_data(request,id):
    if request.method=='POST':
     pi=User.objects.get(pk=id)
     pi.delete()
     return HttpResponseRedirect('/')
    

def update_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=StudentResgisteration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=StudentResgisteration(instance=pi)

    return render(request,'enroll/updatestudent.html',{'form':fm})
