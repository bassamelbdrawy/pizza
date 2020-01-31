from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse
from .models import Regular_pizza,Sicilian_pizza,Topping,Sub,Pasta,Salad,Dinner_platter,my_order
from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            context = {
                "Regular_pizza" : Regular_pizza.objects.all(),
                "Sicilian_pizza" : Sicilian_pizza.objects.all(),
                "Topping" : Topping.objects.all(),
                "Sub" : Sub.objects.all(),
                "Pasta" : Pasta.objects.all(),
                "Salad" : Salad.objects.all(),
                "Dinner_platter" : Dinner_platter.objects.all()
            }
            return render(request, "orders/index.html" , context)
        if request.method == "POST":
            item = request.POST['userPizza']
            orderArray = item.split("-")
            if orderArray[1] == 'Regular Pizza':
                result = Regular_pizza.objects.get(id=orderArray[0])
            elif orderArray[1] == 'Sicilian pizza':
                result = Sicilian_pizza.objects.get(id=orderArray[0])
            elif orderArray[1] == 'sub':
                result = Sub.objects.get(id=orderArray[0])
            elif orderArray[1] == 'Dinner_platter':
                result = Dinner_platter.objects.get(id=orderArray[0])
            elif orderArray[1] == 'Topping':
                result = Topping.objects.get(id=orderArray[0])
            elif orderArray[1] == 'Pasta':
                result = Pasta.objects.get(id=orderArray[0])
            elif orderArray[1] == 'Salad':
                result = Salad.objects.get(id=orderArray[0])
            if result:
                neworder = my_order()
                neworder.itemname = result.name
                if orderArray[2] == 's':
                    neworder.itemprice = result.small
                    neworder.groupname = orderArray[1]
                    neworder.size = "small"
                elif orderArray[2] == 'l':
                    neworder.itemprice = result.large
                    neworder.groupname = orderArray[1]
                    neworder.size = "large"
                else:
                    neworder.itemprice = result.price
                    neworder.groupname = orderArray[1]
                    neworder.size = "regular" 
                neworder.user_id = request.user.id
                neworder.save()
                
            context = {
                "Regular_pizza" : Regular_pizza.objects.all(),
                "Sicilian_pizza" : Sicilian_pizza.objects.all(),
                "Topping" : Topping.objects.all(),
                "Sub" : Sub.objects.all(),
                "Pasta" : Pasta.objects.all(),
                "Salad" : Salad.objects.all(),
                "Dinner_platter" : Dinner_platter.objects.all()
            }
            return render(request, "orders/index.html" , context)
    else:
        return HttpResponseRedirect(reverse("login"))

def login_user(request):
    if request.method == "GET":
        return render(request , "orders/login.html")
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request,user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/login.html", {"message": "Invalid credentials."})

def register_user(request):
    if request.method == "GET":
        return render(request , "orders/register.html")
    username = request.POST["username"]
    password = request.POST["password"]
    firstname = request.POST["firstname"]
    lastname = request.POST["lastname"]
    email = request.POST["email"]
    newuser = User.objects.create_user(username, email, password)
    newuser.first_name = firstname
    newuser.last_name = lastname
    newuser.save()
    return render(request, "orders/login.html")

def myorder(request):
    if request.method == "GET":
        sum = my_order.objects.filter(user_id = request.user).filter(is_complete = 0).aggregate(Sum('itemprice'))
        summ = sum['itemprice__sum']
        context = {
                "my_order" : my_order.objects.filter(user_id = request.user).filter(is_complete = 0),
                "summ" : summ
            }
        return render(request , "orders/myorder.html", context)
    if request.method == "POST":
        items = my_order.objects.filter(user_id = request.user).filter(is_complete = 0)
        for i in items:
            i.is_complete = 1
            i.save()
        return HttpResponseRedirect(reverse("myorder"))

def orders(request):
    if request.method == "GET":
        sum = my_order.objects.filter(is_complete = 1).aggregate(Sum('itemprice'))
        summ = sum['itemprice__sum']
        context = {
            "orders" : my_order.objects.filter(is_complete = 1),
            "summ" : summ
        }
        return render(request , "orders/orders.html", context)

    
    

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))
