from django.db import models


class Profile(models.Model):
    first_name = models.CharField('First name', max_length=200)
    last_name = models.CharField('Last name', max_length=200)
    date_of_birth = models.DateField('Date of birth')
    biography = models.TextField('Biography')
    contacts = models.ManyToManyField('Profile', blank=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f'{self.id}. {self.first_name} {self.last_name}'
