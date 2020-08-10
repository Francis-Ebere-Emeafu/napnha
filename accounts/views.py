from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.contrib.staticfiles import finders
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import PermissionDenied
from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives
from email.mime.image import MIMEImage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
# from django.utils.functional import lru_cache
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic.edit import UpdateView

from accounts.models import Account
from accounts.forms import RegForm, LoginForm
from accounts.utils import (
    get_username_for_auth,
    account_activation_token,
    send_activation_mail,
    get_time_constants,
)


def register(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            username = form.cleaned_data['email']

            new_user = User.objects.create_user(
                username=username, password=password)
            new_user.is_active = False
            new_user.save()

            account = form.save(commit=False)
            account.user = new_user
            account.email = username
            account.save()

            current_site = get_current_site(request)

            # send_activation_mail(new_user, current_site)
            subject = "Activate your NAPNHA account"
            message = "Please, click on the link to confirm your email"
            html_message = render_to_string('accounts/activate_email.html', {
                "user": "{} {}".format(account.first_name, account.surname),
                "domain": current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(new_user.pk)),
                "token": account_activation_token.make_token(new_user)
            })

            from_email = 'registration@napnha.org'
            to_email = username
            send_mail(
                subject,
                message,
                from_email,
                [to_email, ],
                fail_silently=False,
                html_message=html_message
            )

            # email = EmailMultiAlternatives(
            #     subject,
            #     message,
            #     from_email,
            #     to=[to_email],
            # )
            # email.content_subtype = "html"
            # email.mixed_subtype = "related"
            # email.attach_alternative(html_message, "text/html")
            # email.attach(logo_data())
            # email.send()
            request.session['full_name'] = "{} {}".format(
                account.first_name, account.surname)
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
                return redirect('profile')
            else:
                messages.warning(
                    request, "You have entered an invalid username or password")
                return redirect('login')

    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {"form": form})


def logout_user(request):
    logout(request)
    return redirect('home')


@login_required
def profile(request, pk=None):
    if pk:
        try:
            account = Account.objects.get(pk=pk)
        except Account.DoesNotExist:
            return redirect("login")
        else:
            if account.user != request.user:
                return redirect("login")
    else:
        try:
            account = Account.objects.get(user=request.user)
        except Account.DoesNotExist:
            return redirect("login")
    day_of_week, daytime, greeting = get_time_constants()
    context = {
        "account": account,
        "day_of_week": day_of_week,
        "daytime": daytime,
        "greeting": greeting,
    }

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


def sampletemp(request):
    new = logo_data()
    print(new)
    context = {}
    return render(request, "sampletemp.html", context)


# @lru_cache()
def logo_data():
    with open(finders.find('images/email/slider3.jpeg'), 'rb') as f:
        slider_data = f.read()
    slider_image = MIMEImage(slider_data)
    slider_image.add_header('Content-ID', '<slider_image>')
    with open(finders.find('images/email/napnha_logo.png'), 'rb') as f:
        napnha_data = f.read()
    napnha_image = MIMEImage(napnha_data)
    napnha_image.add_header('Content-ID', '<slider_image>')
    print("-------------here I am-------------")
    print("slider")
    print(slider_image)
    print("napnha")
    print(napnha_image)
    return slider_image, napnha_image


class AccountView(UpdateView):
    model = Account

    def get(self, request, pk):
        try:
            _account = Account.objects.get(pk=pk)
        except Account.DoesNotExist:
            return redirect("login")

        if _account.user != request.user:
            raise PermissionDenied

        else:
            return super().get(request, pk)


class PersonalDetailsView(AccountView):
    fields = ["middle_name", "whatsapp_phone"]
    template_name = "accounts/personal_details.html"


class OriginDetailsView(AccountView):
    fields = ["state_of_origin", "lga_of_origin", "gender", "dob", "bio"]
    template_name = "accounts/origin_details.html"


class NYSCDetailsView(AccountView):
    fields = ["state_code", "call_up_num", "certificate"]
    template_name = "accounts/nysc_details.html"


class PhotosView(AccountView):
    fields = ["picture"]
    template_name = "accounts/picture.html"


class ProfessionalDetailsView(AccountView):
    fields = ["profession", "ministry", "level", "office_address"]
    template_name = "accounts/professional_details.html"
