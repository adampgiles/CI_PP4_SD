from django.shortcuts import render
from developers.models import Developer

# Create your views here.
def index(request):
    """ View to return index page """
    if request.user.is_authenticated:
        developers = Developer.objects.filter(user=request.user)
        if developers:
            developer = developers[0]
            print(developer)
        else:
            developer = None  
    else:
        developer = None
    context = {
        'developer': developer,
    }

    return render(request, 'home/index.html', context)