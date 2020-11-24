from django.shortcuts import render

# Create your views here.
@login_required
def post_comment_create_and_list_view(request):
    qs = Post.objects.all()
    profile = Profile.objects.get(user=request.user)

  


   
    context = {
        'qs': qs,
        'profile': profile,
       
    }

    return render(request, 'posts/main.html', context)