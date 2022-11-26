from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os




# @receiver(models.signals.post_delete, sender=Banner)
# def auto_delete_file_on_delete(sender, instance, **kwargs):
#     """
#     Deletes file from filesystem
#     when corresponding `MediaFile` object is deleted.
#     """

#     if instance.image:
#         if os.path.isfile(instance.image.path):
#             os.remove(instance.image.path)

# @receiver(models.signals.pre_save, sender=Banner)
# def auto_delete_file_on_change(sender, instance, **kwargs):
#     """
#     Deletes old file from filesystem
#     when corresponding `MediaFile` object is updated
#     with new file.
#     """
#     if not instance.pk:
#         return False

#     try:
#         old_file = Banner.objects.get(pk=instance.pk).image
#     except Banner.DoesNotExist:
#         return False

#     new_file = instance.image
#     if not old_file == new_file:
#         if os.path.isfile(old_file.path):
#             os.remove(old_file.path)
    

    
