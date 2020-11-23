from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.
def index(request):
    return render(request,'profiles/myprofile.html')
@login_required
def my_profile_view(request):
    profile = Profile.objects.get(user=request.user)


    context = {
        'profile': profile,
      
    }

    return render(request, 'profiles/myprofile.html', context)    