from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Developer, Post
from accounts.models import UserAccount
from .forms import DeveloperProfileForm, PostForm


def all_developers(request):
    """ View to show all developers """
    developers = Developer.objects.all()
    query = ""
    sort = ""
    developers = developers.order_by('-count_sold')

    if request.GET:
        if 'search-query' in request.GET:
            query = request.GET['search-query']
            queries = (
                Q(profile_name__icontains=query) |
                Q(description__icontains=query)
                )
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

    paginator = Paginator(developers, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'developers': developers,
        'search': query,
        'sort': sort,
        'page_obj': page_obj,
    }

    return render(request, 'developers/developers.html', context)


def developer_profile(request, developer_id):
    """ View to show individual developer details """
    show_posts = False
    """ If User is logged in, retrieve the User's Account """
    if request.user.is_authenticated:
        current_user = request.user
        account = UserAccount.objects.filter(user=current_user)[0]

    """
    If the User has a Developer Profile, return that profile.
    Else redirect to the Add Developer page
    """
    if developer_id == "is_developer":
        if account.is_developer is True:
            developer_id = Developer.objects.all().filter(
                user=current_user)[0].pk
            return redirect('developer_profile', developer_id)
        else:
            return redirect('add_developer')
    else:
        developer = get_object_or_404(Developer, pk=developer_id)
        posts = Post.objects.all().filter(author=developer.id)
        """
        If the Current User has purchased access to this
        Developer Profile, Show Posts
        """
        if request.user.is_authenticated:
            current_user = request.user
            if current_user == developer.user:
                show_posts = True
            else:
                account = UserAccount.objects.filter(user=current_user)[0]
                developers = account.purchased_developers
                if developers.contains(developer):
                    show_posts = True
    posts = posts.order_by('-publish_date')

    paginator = Paginator(posts, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'developer': developer,
        'posts': posts,
        'show_posts': show_posts,
        'page_obj': page_obj,
    }

    return render(request, 'developers/developer_profile.html', context)


@login_required
def add_developer(request):
    """ Create a developer profile """
    if request.method == 'POST':
        form = DeveloperProfileForm(request.POST, request.FILES)
        if form.is_valid():
            developer = form.save(commit=False)
            developers = Developer.objects.all()
            current_developer = developers.filter(
                profile_name=developer.profile_name)
            if current_developer:
                messages.error(request,
                               ('Profile Name is already in use,'
                                'please use another Profile Name.'
                                )
                               )
                return redirect(reverse('add_developer'))
            developer.user = request.user
            developer.save()

            current_user = request.user
            account = UserAccount.objects.filter(user=current_user)[0]
            account.is_developer = True
            account.save()

            messages.success(request,
                             'Successfully created a Developer Profile!')
            return redirect(reverse('developer_profile', args=[developer.id]))
        else:
            messages.error(request,
                           ('Failed to create a Developer Profile.'
                            'Please ensure the form is valid.'
                            )
                           )
    else:
        form = DeveloperProfileForm()
    template = 'developers/add_developer.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_developer(request, developer_id):
    """ Edit a developer profile """
    developer = get_object_or_404(Developer, pk=developer_id)
    if request.method == 'POST':
        form = DeveloperProfileForm(request.POST, request.FILES,
                                    instance=developer)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Successfully updated your Developer Profile!')
            return redirect(reverse('developer_profile', args=[developer.id]))
        else:
            messages.error(request,
                           ('Failed to update your Developer Profile.'
                            'Please ensure the form is valid.'
                            )
                           )
        form = DeveloperProfileForm(instance=developer)
        messages.info(request, f'You are editing {developer.profile_name}')

    template = 'developers/edit_developer.html'
    context = {
        'form': form,
        'developer': developer,
    }

    return render(request, template, context)


@login_required
def confirm_delete_developer(request, developer_id):
    """ Confirm deletion of a developer profile """
    developer = get_object_or_404(Developer, pk=developer_id)
    if not request.user == developer.user:
        return redirect('home')
    template = 'developers/confirm_delete_developer.html'
    context = {
        'developer': developer,
    }
    return render(request, template, context)


@login_required
def delete_developer(request, developer_id):
    """ Delete a developer profile """
    developer = get_object_or_404(Developer, pk=developer_id)
    if not request.user == developer.user:
        return redirect('home')
    developer.delete()
    current_user = request.user
    account = UserAccount.objects.filter(user=current_user)[0]
    account.is_developer = False
    account.save()
    messages.success(request, 'Developer Profile deleted!')
    return redirect(reverse('developers'))


@login_required
def add_post(request, developer_id):
    """ Create a developer profile post """
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
            messages.error(request,
                           ('Failed to create a new Post.'
                            'Please ensure the form is valid.'
                            )
                           )
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
    """ Edit a developer profile post """
    developer = Developer.objects.filter(user=request.user)[0]
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated your Post!')
            return redirect(reverse('developer_profile', args=[developer.id]))
        else:
            messages.error(request,
                           ('Failed to update your Post.'
                            'Please ensure the form is valid.'
                            )
                           )
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
def confirm_delete_post(request, post_id):
    """ Confirm deletion of a developer profile post """
    developer = Developer.objects.filter(user=request.user)
    if developer:
        post = get_object_or_404(Post, pk=post_id)
        print(developer.profile_name)
        print(post.author)
        if not developer.profile_name != post.author:
            return redirect('home')
    else:
        return redirect('home')
    template = 'developers/confirm_delete_post.html'
    context = {
        'post': post,
    }
    return render(request, template, context)


@login_required
def delete_post(request, post_id):
    """ Delete a developer profile post """
    developer = Developer.objects.filter(user=request.user)[0]
    post = get_object_or_404(Post, pk=post_id)
    if not developer.user == post.author:
        return redirect('home')
    post.delete()
    messages.success(request, 'Post deleted!')
    return redirect(reverse('developer_profile', args=[developer.id]))
