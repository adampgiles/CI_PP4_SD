from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from .models import Developer
from .models import Post

# Create your views here.
def all_developers(request):
    """ View to show all developers """

    developers = Developer.objects.all()
    query = None

    if request.GET:
        if 'search-query' in request.GET:
            query = request.GET['search-query']
                        
            queries = Q(profile_name__icontains=query) | Q(description__icontains=query)
            developers = developers.filter(queries)


    context = {
        'developers': developers,
        'search': query,
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