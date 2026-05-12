from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import customUser, userProfile

@receiver(post_save, sender=customUser)
def create_user_profile(sender, instance, created, **kwargs):
    print('created')
    if created:
        userProfile.objects.create(user = instance)
        print('User Profile is Created')



@receiver(post_save, sender=customUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    print('This user is being saved')