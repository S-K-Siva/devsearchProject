from django.dispatch import receiver
from django.db.models.signals import post_save,post_delete
from django.contrib.auth.models import User
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings
def createProfile(sender,instance,created,**kwargs):
    profile = None
    if created:
        user = instance
        profile = Profile.objects.create(
            author = user,
            name = user.username,
            email = user.email,
        )

        send_mail(
            subject="Congratulations! Eccommerce-website",
            message="Hey "+profile.author.username+", congratulations on successfull registeration on our platform",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[profile.email],
            fail_silently=False,
        )

post_save.connect(createProfile,sender=User)
