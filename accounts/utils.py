from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib.staticfiles import finders
from django.template.loader import render_to_string
from django.utils import six
from django.utils import timezone
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

import datetime
from email.mime.image import MIMEImage

from post_office import mail

from accounts.models import Account

FROM_EMAIL = "info@digifracktechnologies.com"


def get_username_for_auth(input_username):
    # Account owner may want to signin with phone
    username = input_username
    if not input_username.__contains__("@"):
        # Check if a phone number exists
        if Account.objects.filter(phone=username).exists():
            account = Account.objects.get(phone=input_username)
            username = account.user.username
    else:
        if Account.objects.filter(email=input_username).exists():
            account = Account.objects.get(email=input_username)
            username = account.user.username
    return username


def send_activation_mail(new_user, current_site):
    subject = "Activate your NAPNHA account"
    message = "Please, click on the link to confirm your email"
    html_message = render_to_string('accounts/activate_email.html', {
        "user": new_user,
        "domain": current_site.domain,
        "uid": urlsafe_base64_encode(force_bytes(new_user.pk)),
        "token": account_activation_token.make_token(new_user)
    })
    # msg = EmailMultiAlternatives(
    #     subject,
    #     message,
    #     FROM_EMAIL,
    #     [new_user.username]
    # )
    # msg.attach_alternative(html_message, 'text/html')
    # msg.attach_file(acct.certificate.path)
    # constitution_path = os.path.join(settings.STATIC_ROOT, 'constitution.pdf')
    # msg.attach_file(constitution_path)
    # msg.attach(logo_data())
    # result = msg.send()
    # print(result)
    mail.send(
        new_user.username,
        FROM_EMAIL,
        subject='This is heading',
        message='This is message',
        html_message='This is the HTML message <strong>NAPNHA</strong>',
    )


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.is_active))


account_activation_token = TokenGenerator()


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


def get_time_constants():
    weekDays = ("Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday")
    timeNow = datetime.datetime.now()
    dateNow = timeNow.date()
    dayNow = dateNow.weekday()
    day_of_week = weekDays[dayNow]

    today = timezone.now()
    hour = today.hour
    if hour < 12:
        daytime = 'AM'
        greeting = 'Good morning'
    elif hour < 18:
        daytime = 'PM'
        greeting = 'Good afternoon'
    else:
        daytime = 'PM'
        greeting = 'Good evening'

    return (day_of_week, daytime, greeting)
