from django.shortcuts import render, redirect
from App.forms import ContactForm
from django.contrib import messages
from App.models import Photo
# Create your views here.
def home(request):
    return render(request, 'App/index.html')

def about(request):
    return render(request, 'App/about-yumyum.html')

def why_yumyum(request):
    return render(request, 'App/why-yumyum.html')

def photo(request):
    dict_photo = {
        'photos': Photo.objects.all()
    }
    return render(request, 'App/photo.html', dict_photo)

def team(request):
    return render(request, 'App/team.html')

def catering(request):
    return render(request, 'App/catering.html')

def menu(request):
    return render(request, 'App/menu.html')

def outlets(request):
    return render(request, 'App/outlets.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            mobile_number = form.cleaned_data['mobile_number']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            if len(str(mobile_number)) < 10:
                messages.warning(request, 'Please Enter a Valid Mobile Number !')
                return redirect('contact-us')

            elif len(str(message)) < 5:
                messages.warning(request, 'Please Enter Some Message !')
                return redirect('contact-us')
            elif '.com' not in email:
                messages.warning(request, "Please Provide a Valid Email Address")
                return redirect('contact-us')
            else:
                form.save()
                messages.success(request, 'Thank You ! Your Response Has Been Recorded 😊')
                return redirect('contact-us')
    else:
        form = ContactForm()
        context = {'form': form}
    return render(request, 'App/contact.html', context)
