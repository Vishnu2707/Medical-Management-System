from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record
from django.db.models import Q

# Create your views here.

def home(request):
    query = request.GET.get('q')
    if query:
        # Search for records matching the query
        records = Record.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(email__icontains=query) |
            Q(phone__icontains=query) |
            Q(city__icontains=query) |
            Q(state__icontains=query)
        )
    else:
        records = Record.objects.all()

        # Check to see if logging in!
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            # Authenticate
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have logged in!!")
                return redirect('home')
            else:
                messages.success(request, "There was an error logging in, Please try again...")
                return redirect('home')
        else:
            return render(request, 'home.html', {'records':records})
    return render(request, 'home.html', {'records': records})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out....")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Check if employee ID is authorized
            employee_id = form.cleaned_data['employee_id']
            authorized_ids = ['id1', 'id2', 'id3']  # Update with your list of authorized IDs
            if employee_id not in authorized_ids:
                messages.error(request, "You're not authorized.")
                return redirect('register')

            form.save()
            # Authenticate and log in!
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration is complete! Please log in!")
            return redirect('home')
    else:
        form = SignUpForm()
    
    return render(request, 'register.html', {'form': form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        #Look up records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You need to login to view the records!")
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        #Delete records
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record has been deleted!")
        return redirect('home')
    else:
        messages.success(request, "You need to login to delete the records!")
        return redirect('home')
    
def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record Added...")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')

def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')