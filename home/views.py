from django.db.models import query
from django.shortcuts import render, HttpResponse, redirect
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from blog.models import Post

# Create your views here.

def handleLogin(request):
    if request.method=="POST":
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user = authenticate(username = loginusername, password = loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged In Successfully")
            return redirect("home")
        
        else:
            messages.error(request, "Wrong Credentials! Try Again")
            return redirect("home")
    
    else:
        return HttpResponse("<h1> 404 - Not Found </h1>")

def handleLogout(request):
    logout(request)
    messages.success(request,"Logged Out Succesfully")
    return redirect("home")


def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input

        if len(username)<10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')

        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('home')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your iCoder has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")

def search(request):
    query = request.GET['query']
    allPostsTitle = Post.objects.filter(title__icontains=query)
    allPostsContent = Post.objects.filter(content__icontains=query)
    allPosts = allPostsTitle.union(allPostsContent)
    params = {'allPosts':allPosts}
    return render(request, 'home/search.html', params)



def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name, email, phone, content)

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please Fill The Form Correctly")

        
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your Message Has Been Sent")

    return render(request, 'home/contact.html')



def home(request): 
    
    # post = Post.objects.all()
    # unsorted = []
    # for i in post:
    #     print(post[i])
    # for count, ps in enumerate(post):
    #     current_post = post[count]
    #     views = current_post.views
    #     unsorted.append(views)
    
    # sorte = sorted(unsorted,reverse=True)
    # context = {'list':sorte}

    return render(request, 'home/home.html')


def about(request): 
    return render(request, 'home/about.html')



