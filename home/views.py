from django.shortcuts import render
from accounts.models import UserAccount
from developers.models import Developer

# Create your views here.
def index(request):
    """ View to return index page """
    if request.user.is_authenticated:
        current_user = request.user
        account = UserAccount.objects.filter(user=current_user)
        if not account:
              UserAccount.objects.create(user=current_user)

        developers = Developer.objects.filter(user=current_user)
        print(developers)
        if developers:
            is_developer = True
        else:
            is_developer = False

    else:
            is_developer = False

    context = {
        'is_developer': is_developer,
    }
    return render(request, 'home/index.html', context)