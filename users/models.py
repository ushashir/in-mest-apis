from django.db import models

# Create your models here.
class InMestUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    USER_TYPE = {
        'EIT': 'Eit',
        'FELLOW': 'Fellow',
        'STAFF': 'Staff',
        'ADMIN': 'Admin',
    }
    user_type = models.CharField(
        max_length=2,
        choices=USER_TYPE,
        default='EIT',
    )
    date_created = models.DateField(auto_now=True)
    date_modified = models.DateField(auto_now=True)

    def is_upperclass(self):
        return self.user_type in {self.ADMIN, self.EIT}
class Cohort(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    date_created = models.DateField(auto_now=True)
    start_date = models.DateTimeField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    author = models.ForeignKey(InMestUser, on_delete=models.CASCADE)
class CohortMember(models.Model):
    member = models.ForeignKey(InMestUser, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    date_created = models.DateField(auto_now=True)
    date_modified = models.DateTimeField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    author = models.ForeignKey(InMestUser, on_delete=models.CASCADE)
