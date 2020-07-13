from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives
from django.contrib.sites.shortcuts import get_current_site
from email.mime.image import MIMEImage
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from accounts.models import Account
from accounts.forms import RegForm, LoginForm
from accounts.utils import get_username_for_auth, account_activation_token


def register(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            username = form.cleaned_data['email']

            new_user =User.objects.create_user(username=username, password=password)
            new_user.is_active = False
            new_user.save()

            account = form.save(commit=False)
            account.user = new_user
            account.email = username
            account.save()

            current_site = get_current_site(request)
            mail_subject = "Activate your NAPNHA account"
            message = "Please, click on the link to confirm your email"
            html_message = render_to_string('accounts/activate_email.html', {
                "user": new_user,
                "domain": current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(new_user.pk)),
                "token": account_activation_token.make_token(new_user)
            })
            to_email = username
            # email = EmailMessage(mail_subject, message, to=[to_email])
            # email.send()

            send_mail(
                mail_subject,
                message,
                'info@digifracktechnologies.com',
                [to_email,],
                fail_silently=False,
                html_message=html_message
            )
            request.session['full_name'] = "{} {}".format(account.first_name, account.surname)
            return redirect("activation_message")
    else:
        form = RegForm()
    return render(request, "accounts/register.html", {"form": form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            phone_email = get_username_for_auth(username)
            user = authenticate(username=phone_email, password=password)
            if user is not None:
                login(request, user)
                print('I am logged in!')
                return redirect('home')
            else:
                messages.warning(request, "You have entered an invalid username or password")
                return redirect('login')

    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {"form": form})


def logout_user(request):
    print('I am here')
    logout(request)
    print('logout request is done')
    return redirect('home')


def profile(request):
    context = {}
    return render(request, 'accounts/profile.html', context)


def activation_message(request):
    return render(request, 'accounts/activation_message.html')


def activate_email(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        # user.account.confirm_email = True
        user.save()
        login(request, user)
        return redirect("profile")
    else:
        return render(request, "invalid_account_activation.html")