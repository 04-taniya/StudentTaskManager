from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import Task_form
from .models import Task_details

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confrim_password = request.POST['confrim_password' ]
        if password == confrim_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username already exists")
            else:
                User.objects.create_user(username=username,email=email,password=password)
                messages.success(request, "Account created successfully")
                return redirect('login') 
    else:
        messages.success(request,"Password do not match")
    return render(request,'signup.html')



def login_page(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username,password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username and password")
    return render(request, 'login.html')



@login_required
def dashboard(request):
    if request.user.is_superuser:
        tasks = Task_details.objects.all()
    else:
        tasks = Task_details.objects.filter(user= request.user)
    total_task = tasks.count()
    complete_task = tasks.filter(isCompelete=True).count()
    pending_task = tasks.filter(isCompelete=False).count()
    high_priority = tasks.filter(priority="High").count()
    
    task_content ={
        'tasks' : tasks,
        'total_task' : total_task,
        'pending_task':pending_task,
        'complete_task': complete_task,
        'high_priority':high_priority 
    }
    return render(request, 'dashboard.html',task_content)

   

@login_required
def add_task(request):
    if request.method =='POST':
        form = Task_form(request.POST)
    
        if form.is_valid():
            task =form.save(commit = False)
            task.user = request.user
            task.save()
            return redirect('dashboard') #redirect() means send user to another page (URL)
    else:
        form = Task_form()
    return render(request, 'add_task.html',{'form':form})


@login_required
def done_btn (request, id):
    if request.user.is_superuser:
        task = get_object_or_404(Task_details, id=id)
    else:
         task = Task_details.objects.get(id=id, user = request.user)
    task.isCompelete=True
    task.save()
    return redirect('dashboard')


@login_required
def delete_btn (request, id):
    if request.user.is_superuser:
        task = get_object_or_404(Task_details, id=id)
    else:
        task = Task_details.objects.get(id=id, user = request.user)
    task.delete()
    return redirect('dashboard')


@login_required
def edit_btn(request, id):
    if request.user.is_superuser:
        task = get_object_or_404(Task_details, id=id)
    else:    
        task = get_object_or_404(Task_details, id=id, user=request.user)

    if request.method == "POST":
        form = Task_form(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = Task_form(instance=task)

    return render(request, 'add_task.html', {'form': form})