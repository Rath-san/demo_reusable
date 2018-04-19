# encoding=utf-8
import re

from django.template import Context
from django.template.loader import get_template, render_to_string
from django.conf import settings
from django.core.mail import EmailMultiAlternatives, send_mail
from django.utils.html import strip_tags


def send_html_email(title, content, replay_to, to=settings.EMAIL_SEND_TO, from_address=settings.EMAIL_HOST_USER):
    if type(to) is not list:
        to = [to, ]
    # t = get_template("mail/email.html")
    c = {"content": content}
    content = render_to_string("mail/email.html", c)
    text_content = strip_tags(content)
    title = "%s - %s" % (settings.EMAIL_FIXED_TITLE, title)
    if not replay_to:
        replay_to = [settings.EMAIL_SEND_TO, ]
    msg = EmailMultiAlternatives(title, text_content, "%s <%s>" % (settings.EMAIL_FIXED_TITLE, from_address), to, reply_to=replay_to)
    msg.attach_alternative(content, "text/html")
    msg.send()


def send_email(title, content, to=settings.EMAIL_SEND_TO, from_address=settings.EMAIL_HOST_USER):
    if type(to) != list:
        to = [to]
    send_mail(title, content, from_address, to, fail_silently=True)


def send_form_email(title, content, form, to):
    string = ''
    replay_to = []
    for k in form.fields.keys():
        match = re.search(r'[\w\.-]+@[\w\.-]+', form[k].data)
        if match:
            replay_to.append(match.group(0))
        string += '%s:<br>%s<br><br>' % (k, form[k].data)
    message = "%s<br>%s<br>%s<br>" % (content, '-' * 50, string)
    send_html_email(title, message, replay_to, to)
