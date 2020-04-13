from django.shortcuts import render, redirect

from .models import User
from .forms import UserRegistration

def register(request):
    if request.method == 'POST':
        user_form = UserRegistration(request.POST)
        if user_form.is_valid():
            # create a new user object but do not save it
            new_user = user_form.save(commit=false)
            # set the password
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            new_user.save()
            # TODO: send email to confirm account
            # return render(request, 'accounts/register_done.html', {'new_user': new_user})
            return redirect('login')
    else:
        user_form = UserRegistration()
        return render(request, 'accounts/register.html', {'form': user_form})


