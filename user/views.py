from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from django.contrib.auth import login, logout, authenticate
from .forms import customUserCreationForm, customUserChangeForm, passwordresetForm
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.contrib.auth.forms import SetPasswordForm
# Create your views here.

def gretting(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = customUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Your account is created successfully.')
            return redirect('index')
        else:
            print('Form validation failed')
            print(form.errors)
    else:
        form = customUserCreationForm()
        
    context = {
        'form':form
        }
    return render(request, 'user/signup.html', context)

def login_view(request):
    if request.user.is_authenticated:
        messages.error(request,'You are already logged in')
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'you logged in successfully')
            return redirect('index')
        else:
            messages.error(request, 'Invalid Login credentials')
            return redirect('login')
               

    return render(request, 'user/login.html')


def logout_view(request):
    logout(request)
    messages.info(request, 'You are logged out')
    return redirect('index')


def reset_password_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        #checking if the user exists
        User = get_user_model()
        user = User.objects.filter(email=email)
        if user.exists():
            for existed_user in user:
                #generating the secure token and uid
                uid = urlsafe_base64_encode(force_bytes(existed_user.pk))
                token = default_token_generator.make_token(existed_user)

                #building the email context
                context = {
                    'email':existed_user.email,
                    'domain': request.META['HTTP_HOST'],
                    'uid': uid,
                    'token':token,
                    'protocol': 'http'if request.is_secure() == False else 'https',

                }

                #render the email text and send it
                html_email_content = render_to_string('user/password_reset_email.html', context)

                #automatically generate the plain text of the html file
                plain_text_email = strip_tags(html_email_content)
                send_mail(
                    subject='Password Reset Requested',
                    message=plain_text_email,
                    from_email='adanshahid.engineer@gmail.com',
                    recipient_list=[existed_user.email],
                    fail_silently=False,
                    html_message=html_email_content
                )
        return redirect('password_reset_done')

    return render(request, 'user/forgot_password.html')


#once the email is send, this view will triggered
def custom_password_reset_done(request):
    return render(request, 'user/password_reset_done.html')


#view to verify the token and reset the password
def custom_password_reset_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        User = get_user_model()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    
    #verifying that user exists and its token is valid for this specific user
    if user is not None and default_token_generator.check_token(user,token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                return redirect('password_reset_complete')
        else:
            form = SetPasswordForm(user)
        context = {
            'form':form,
            'validlink':True,
        }
        return render(request, 'user/password_reset_confirm.html', context)
    else:
        return render(request, 'user/password_reset_confirm.html', {'validlink':False})
    
def password_reset_complete(request):
    return render(request, 'user/password_reset_complete.html')