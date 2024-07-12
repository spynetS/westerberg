#!/usr/bin/env python3

from django.contrib.auth.models import Group
from accounts.models import CustomUser
from django.core.mail import EmailMessage
from westerberg import settings


def sendmail(subject,body,name,email,to,content_subtype="text/plain"):

    # Assuming 'mail' is the name of the group you're interested in
    group_name = "Mail"

    # Get the group object
    mail_group = Group.objects.get(name=group_name)

    # Filter users who are in the 'mail' group
    users = CustomUser.objects.filter(groups=mail_group)
    reply = [email]
    to = [to]

    for user in users:
        print(user.email)
        reply.append(user.email)
        to.append(user.email)

    mail = EmailMessage(
        subject=f"Info {subject}",
        body=body,
        from_email=(name+settings.EMAIL_HOST_USER),
        to=to,
        reply_to=reply
        # headers={'Reply-To': f" {request.POST['name']} {request.POST['email']}, Info {settings.INFO_EMAIL}"}
    )
    mail.content_subtype = content_subtype

    # Send the email
    return mail.send()