from django.db import models

class StaffManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_staff=True)


class UsersManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_staff=False)
    
class IssuedBookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()