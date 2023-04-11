from django.shortcuts import render
from accounts.models import UserAccount

# Create your views here.
def index(request):
    """ View to return index page """
    if request.user.is_authenticated:
        current_user = request.user
        account = UserAccount.objects.filter(user=current_user)
        if not account:
              UserAccount.objects.create(user=current_user)

    return render(request, 'home/index.html')