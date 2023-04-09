from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.conf import settings
from django.db.models import Q
from .models import Developer, Post
from checkout.models import Order, OrderLineItem

from django.contrib import messages
from .forms import DeveloperProfileForm  

# Create your views here.
def all_developers(request):
    """ View to show all developers """

    developers = Developer.objects.all()
    query = ""
    sort = ""

    if request.GET:
        if 'search-query' in request.GET:
            query = request.GET['search-query']            
                        
            queries = Q(profile_name__icontains=query) | Q(description__icontains=query)
            developers = developers.filter(queries)

        if 'sort-criteria' in request.GET:
            sort = request.GET['sort-criteria']

            if sort == 'Profile Name (ascending)':       
                developers = developers.order_by('profile_name')
            elif sort == 'Profile Name (descending)':       
                developers = developers.order_by('-profile_name')
            elif sort == 'Price (ascending)':       
                developers = developers.order_by('price')
            elif sort == 'Price (descending)':       
                developers = developers.order_by('-price')
            elif sort == 'Purchase Count (ascending)':       
                developers = developers.order_by('count_sold')
            elif sort == 'Purchase Count (descending)':       
                developers = developers.order_by('-count_sold')

        if 'sort-clear' in request.GET:
            sort = ""
            developers = Developer.objects.all()

    context = {
        'developers': developers,
        'search': query,
        'sort': sort,
    }

    return render(request, 'developers/developers.html', context)

def developer_profile(request, developer_id):
    """ View to show individual developer details """

    developer = get_object_or_404(Developer, pk=developer_id)
    posts = Post.objects.all().filter(author=developer_id)
    show_posts = False

    user = request.user

    query = Q(username__icontains=user)
    orders = Order.objects.filter(query)

    order_lines = OrderLineItem.objects.all()
    for order in orders:
        for order_line in order_lines:
            if str(order.order_number) == str(order_line.order):
                    if str(order_line.developer) == str(developer.profile_name):
                        show_posts = True
                        break

    context = {
        'developer': developer,
        'posts': posts,
        'show_posts': show_posts,
    }

    return render(request, 'developers/developer_profile.html', context)


def add_developer(request):
    """ Add a developer """    
    if request.method == 'POST':
        form = DeveloperProfileForm(request.POST, request.FILES)
        if form.is_valid(): 
            developer = form.save(commit=False)
            developer.user = request.user
            developer.save()
            messages.success(request, 'Successfully created a Developer Profile!')
            return redirect(reverse('developer_profile', args=[developer.id]))
        else:
            messages.error(request, 'Failed to create a Developer Profile. Please ensure the form is valid.')
    else:
        form = DeveloperProfileForm()
        
    template = 'developers/add_developer.html'
    context = {
        'form': form,
    }

    return render(request, template, context)