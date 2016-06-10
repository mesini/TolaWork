from django.core.mail import send_mail
from django.template.loader import render_to_string

def email(t,comment, status_text, send_to):

    txt_message = render_to_string('email/notify.txt', {'ticket': t, 'status': status_text, 'comment': comment })
    html_message = render_to_string('email/notify.html', {'ticket': t, 'status': status_text, 'comment': comment })

    send_mail('[TolaWork] ' + t.title, txt_message,'TolaData <toladatawork@gmail.com>',[send_to],fail_silently=False, html_message=html_message)

