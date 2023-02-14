from django.shortcuts import render,redirect
from django.contrib import messages
from portfolio.models import Contact
# Create your views here.
def home(request):
    return render(request,'home.html')

def myresume(request):
    return render(request,'myresume.html')

def handleblog(request):
    posts=Blogs.objects.all()
    context={"posts":posts}
    return render(request,'handleblog.html',context)


def about(request):
    return render(request,'about.html')



def contact(request):
    if request.method=="POST":
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fphoneno=request.POST.get('num')
        fdesc=request.POST.get('desc')
        query=Contact(name=fname,email=femail,phonenumber=fphoneno,description=fdesc)
        query.save()
        messages.success(request,"Thanks for contacting us. We will get by you Soon!")

        return redirect('/contact')

    return render(request,'contact.html')