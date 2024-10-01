from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.http import JsonResponse,HttpResponse



# Create your views here.
@login_required(login_url='/login/')# decorator for inbuilt login required function
def admin(request):

    if request.user.username != 'admin':
        return HttpResponse('<h1>access_denied.html</h1>')  # Render an access denied page or redirect

    if request.method == 'POST':
        data=request.POST
        app_name=    data.get('app name')
        app_link=    data.get('app link')
        app_points=  data.get('app points')
        app_image=   request.FILES.get('app image')
        app_category= data.get('app category')
        app_types=   data.get('app types')

        App.objects.create(
           app_name= app_name,
           app_link= app_link,
           app_points= app_points,
           app_image=   app_image,
           app_category= app_category,
           app_types= app_types
        )
    
        return redirect('/admin/')
    
    queryset = App.objects.all()
    users= User.objects.all()
    context = {'App': queryset, 'users':users}
 
    return render(request, 'index.html', context)


    


@login_required(login_url='/login/')# decorator for inbuilt login required function
def delete_app(request, id):
    queryset = App.objects.get(id=id)
    queryset.delete()
    messages.success(request, 'App deleted successfully.')

    return redirect('/admin/')


def signup(request):
    if request.method == 'POST':
        data=request.POST
        username=data.get('username')
        email=data.get('email')
        password=data.get('password')
        confirm_password=data.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('signup')
      
        user=User.objects.filter(username=username)
        if user.exists():
         messages.info(request, "Username already taken")
         return redirect('signup')
    
        user=User.objects.create(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()
        
        messages.success(request, "Account created succesfully")
        return redirect('signup')

    return render(request, 'signup.html')
    
    

def user_login(request):
    if request.method == 'POST':
        data=request.POST
        username=data.get('username')
        password=data.get('password')

        if not User.objects.filter(username=username).exists():
         messages.error(request, 'invalid username')
         return redirect('/login/')
    
        user= authenticate(username=username, password=password)
        if user is None:
         messages.error(request, 'invalid password')
         return redirect('/login/')
        else: 
            login(request, user)
            return redirect('home')
    

    
    return render(request, 'login.html')


@login_required(login_url='login')# decorator for inbuilt login required function
def home(request):
   queryset=App.objects.all()
   context= {'App': queryset}

   return render(request, 'home.html', context)

@login_required(login_url='/login/')
def logout_page(request):
   logout(request)
   return redirect('/login/')

class MainView(TemplateView):
   template_name = 'home.html'

@login_required(login_url='/login/')# decorator for inbuilt login required function
def file_upload_view(request):
   #print(request.FILES)
   if request.method == 'POST':
     my_file = request.FILES.get('file')
     Doc.objects.create(upload=my_file)
   return JsonResponse({'post': 'false'})