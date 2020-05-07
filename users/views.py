from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def logout_view(request):
    """Ends the work session"""
    logout(request)
    return HttpResponseRedirect(reverse('feed:index'))


def register(request):
    """Registers new user"""
    if request.method != 'POST':
        """Display blank registration form"""
        form = UserCreationForm()
    else:
        """Processing of existing form"""
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            """Log in and redirect to the home page"""
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('feed:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)