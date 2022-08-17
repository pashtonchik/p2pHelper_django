from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from platform import python_version
from .html_email import email_text_message

from .models import *
from rest_framework import viewsets, permissions
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
import smtplib
from email.mime.text import MIMEText
from django.forms.models import model_to_dict


def send_email(recipient):
    server = 'smtp.gmail.com'
    user = 'p2phelper.confirmation@gmail.com'
    password = 'jppmenfwfbnbwnrj'

    recipients = recipient
    sender = 'p2phelper.confirmation@gmail.com'
    subject = 'Подтверждение адреса электронной почты'
    text = email_text_message
    html = '<html><head></head><body><p>' + text + '</p></body></html>'

    try:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = 'Python script <' + sender + '>'
        msg['To'] = ', '.join(recipients)
        msg['Reply-To'] = sender
        msg['Return-Path'] = sender
        msg['X-Mailer'] = 'Python/' + (python_version())

        part_text = MIMEText(text, 'plain')
        part_html = MIMEText(html, 'html')

        msg.attach(part_text)
        msg.attach(part_html)

        mail = smtplib.SMTP_SSL(server)
        mail.login(user, password)
        mail.sendmail(sender, recipients, msg.as_string())
        mail.quit()
        return Response({'ok': True}, status.HTTP_200_OK)

    except Exception as _ex:
        return Response({'ok': False}, status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_exchanges(request):
    exchanges = Exchange.objects.all()
    responce = []
    for e in exchanges:
        responce.append(
            {
                'fiat': e.fiat,
                'asset': e.asset,
                'payment_method': e.payment_method,
                'price_buy': e.price_buy,
                'price_sell': e.price_sell,
                'refresh_date': e.date_refresh.date
            }
        )
    return Response(responce, status=status.HTTP_200_OK)


@api_view(['POST'])
def post_exchanges(request):
    exchange_info = json.loads(request.body.decode("utf-8"))
    date = Date()
    date.save()
    for item in exchange_info:
        cur_item = Exchange(
            date_refresh=date,
            fiat=item['fiat'],
            asset=item['asset'],
            payment_method=item['payment_method'],
            price_sell=item['price_sell'],
            price_buy=item['price_buy']
        )
        cur_item.save()
    return Response({'ok': True}, status.HTTP_200_OK)


@api_view(['GET'])
def registration_user(request):
    client_info = json.loads(request.body.decode("utf-8"))
    client = User(
        email=client_info['email'],
        login=client_info['login'],
        password=client_info['password'],
    )
    client.save()







