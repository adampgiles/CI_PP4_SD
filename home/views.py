from django.shortcuts import render
from developers.models import Developer

# Create your views here.
def index(request):
    """ View to return index page """
    developer = Developer.objects.filter(user=request.user)

    context = {
        'developer': developer,
    }

    return render(request, 'home/index.html', context)