from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from .models import Developer
from .models import Post

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

    context = {
        'developer': developer,
        'posts': posts,
    }

    return render(request, 'developers/developer_profile.html', context)