from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from contactus.forms import ContactForm

# Create your views here.
@login_required
def contact_us(request):
    """ Submit a Contact Form """    
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid(): 
            contact_form = form.save(commit=False)
            contact_form.user = request.user
            contact_form.save()

            messages.success(request, 'Contact Form submitted successfully!')
            return redirect(reverse('contact_us'))
        else:
            messages.error(request, 'Failed to submit Contact Form. Please ensure the form is valid.')
    else:
        form = ContactForm()
        
    template = 'contactus/contact_us.html'
    context = {
        'form': form,
    }

    return render(request, template, context)