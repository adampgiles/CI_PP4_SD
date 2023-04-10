from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Developer, Post
from checkout.models import Order, OrderLineItem

from django.contrib import messages
from .forms import DeveloperProfileForm, PostForm

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

@login_required
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
        'developer': developer,
    }

    return render(request, template, context)


@login_required
def edit_developer(request, developer_id):
    developer = get_object_or_404(Developer, pk=developer_id)
    if request.method == 'POST':
        form = DeveloperProfileForm(request.POST, request.FILES, instance=developer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated your Developer Profile!')
            return redirect(reverse('developer_profile', args=[developer.id]))
        else:
            messages.error(request, 'Failed to update your Developer Profile. Please ensure the form is valid.')
    else:
        form = DeveloperProfileForm(instance=developer)
        messages.info(request, f'You are editing {developer.profile_name}')

    template = 'developers/edit_developer.html'
    context = {
        'form': form,
        'developer': developer,
    }

    return render(request, template, context)


@login_required
def delete_developer(request, developer_id):
    developer = get_object_or_404(Developer, pk=developer_id)
    developer.delete()
    messages.success(request, 'Developer Profile deleted!')
    return redirect(reverse('developers'))


@login_required
def add_post(request, developer_id):
    developer = get_object_or_404(Developer, pk=developer_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid(): 
            post = form.save(commit=False)
            post.author = developer
            post.save()
            messages.success(request, 'Successfully created a new Post!')
            return redirect(reverse('developer_profile', args=[developer.id]))
        else:
            messages.error(request, 'Failed to create a new Post. Please ensure the form is valid.')
    else:
        form = PostForm()
        
    template = 'developers/add_post.html'
    context = {
        'form': form,
        'developer': developer,
    }

    return render(request, template, context)


@login_required
def edit_post(request, post_id):
    developer = Developer.objects.filter(user=request.user)[0]
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated your Post!')
            return redirect(reverse('developer_profile', args=[developer.id]))
        else:
            messages.error(request, 'Failed to update your Post. Please ensure the form is valid.')
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are editing {post.title}')

    template = 'developers/edit_post.html'
    context = {
        'form': form,
        'developer': developer,
        'post': post,
    }

    return render(request, template, context)


@login_required
def delete_post(request, post_id):
    developer = Developer.objects.filter(user=request.user)[0]
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    messages.success(request, 'Post deleted!')
    return redirect(reverse('developer_profile', args=[developer.id]))