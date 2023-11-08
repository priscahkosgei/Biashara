from django.shortcuts import render,redirect
from BiasharaApp.models import Member,Products
from BiasharaApp.forms import ProductsForm
# create your views here.
def register(request):
    if request.method == 'POST':
        member = Member(firstname=request.POST['firstname'],lastname=request.POST['lastname'],email=request.POST['email'],
                        username=request.POST['username'],password=request.POST['password'])
        member.save()
        return redirect('/')
    else:
        return render(request,'register.html')
def login(request):
    return render(request,'login.html')

def index(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'],
                                 password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'],
                                        password=request.POST['password'])
            return render(request,'index.html', context={'member':Member})
        else:
            return render(request,'login.html')
    else:
            return render(request,'login.html')

def inner(request):
    return render(request,'inner-page.html')

def about(request):
    return render(request,'about.html')

def doctors(request):
    return render(request,'doctors.html')

def add(request):
    if request.method=="POST":
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = ProductsForm()
        return render(request,'addproducts.html',context={'form':form})


def aboutUs(request):
    return render(request, 'About-Us.html')

def services(request):
    return render(request,'services.html')

def show(request):
    products = Products.objects.all()
    return render (request,'show.html',{'products':products})

def delete(request,id):
    product = Products.objects.get(id = id )
    product.delete()
    return redirect('/show')

def edit(request,id):
    product = Products.objects.get(id=id)
    return render(request,'edit.html',{'product':product})

def update(request,id):
    product = Products.objects.get(id=id)
    form = ProductsForm(request.POST,instance=product)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        return render(request,'edit.html',{'product':product})