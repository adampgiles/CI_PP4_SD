from django.shortcuts import render
from .models import Developer

# Create your views here.
def all_developers(request):
    """ View to show all developers """

    developers = Developer.objects.all()

    context = {
        'developers': developers,
    }

    return render(request, 'developers/developers.html', context)