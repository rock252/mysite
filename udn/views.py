from django.shortcuts import render
from django.shortcuts import render,redirect
from api.models import *
from udn.forms import ContactForm, adv
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages

def home(request):

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            Name = form.cleaned_data['Name']
            message =  'Hi'+'  '+ Name +'  ' +'here,'+'  ' +'\n'+ 'Email:' +' ' +from_email+'    ' +'\n'+ message

            try:
                send_mail(subject, message, 'gshivam252@gmail.com', ['udnkhatola@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Submitted Successfully')
    return render(request, "udn/home.html", {'form': form})

def service(request):
    
    return redirect('/#service-page')

def features(request):
    
    return redirect('/#feature-page')

def pricing(request):
    
    return redirect('/#price-page')

def team(request):
    
    return redirect('/#team-page')

def faq(request):
    
    return redirect('/#faq-page')

def blog (request):
    
    return redirect('/#blog-page')

def customer_portal1(request):
    username = None
    if request.user.is_authenticated():
        username =request.user.username
        informations=Information.objects.filter(advertiser_name=username).order_by('android_id', '-time')
        a=0
        v=0
        for i in informations:
           if a!= int(i.android_id):
             a= int(i.android_id)
             v=v+int(i.video_count)
    return render(request, 'udn/customer_portal1.html',{'v': v})
    


def maps(request):

    informations=Information.objects.order_by('android_id', '-time')
    a=0
    m = []

    for i in informations:
       if a!= int(i.android_id):
         a= int(i.android_id)
         m.append([i.latitude, i.longitude ])

    return render(request, 'udn/maps.html', {'m': m})


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            Name = form.cleaned_data['Name']

            try:
                send_mail(subject, message, from_email, ['udnkhatola@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Submitted Successfully')
    return redirect('/#contact-page')



def advertiser_details(request):
    if request.method == 'POST':
        obj = advertiser_data()
        form = adv(request.POST)
        if form.is_valid():
            obj.customer_id = form.cleaned_data['customer_id']
            obj.latitude = form.cleaned_data['latitude']
            obj.longitude = form.cleaned_data['longitude']
            obj.radius = form.cleaned_data['radius']
            obj.video_id = form.cleaned_data['video_id']
            obj.save()
            messages.success(request, 'Submitted Successfully')



        return render(request, "udn/advdetail.html")
    else:
        form = adv()
    return render(request, 'udn/advdetail.html', {'form': form})