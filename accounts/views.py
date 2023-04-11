from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserAccount

@login_required
def user_account(request):
    """ View to show the current user's account details """

    current_user = request.user
    account = UserAccount.objects.filter(user=current_user)[0] 
    developers = account.purchased_developers

    context = {
        'developers': developers,
    }

    return render(request, 'accounts/user_account.html', context)