from django.db import models
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from django.utils import translation

## Managers
class MaleManager(models.Manager):
    '''Manager to only give back people with male gender'''
    def get_queryset(self):
        return super(MaleManager, self).get_queryset().filter(gender='M')

class FemaleManager(models.Manager):
    '''Manager to only give back people with female gender'''
    def get_queryset(self):
        return super(FemaleManager, self).get_queryset().filter(gender='F')

## Models
class CommonInfo(models.Model):
    '''Provides fields that are information of people'''
    first_name = models.TextField('First Name', blank=False, null=False)
    middle_name = models.TextField('Middle Name', blank=True, null=True)
    last_name = models.TextField('Last Name', blank=False, null=False)
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))

    class Meta:
        abstract = True

class Parent(CommonInfo):
    '''Holds parent information'''
    people = models.Manager()
    fathers = MaleManager()
    mothers = FemaleManager()

    def __unicode__(self):
        return " ".join([self.first_name,self.middle_name,self.last_name])

class CommonInfoKid(CommonInfo):
    '''Provides fields that are information of kids'''
    date_of_birth = models.DateField(_('Date of Birth'), blank=False, null=False)
    date_of_leave = models.DateField('Leaving Date', blank=False, null=False)
    mother = models.ForeignKey(Parent, limit_choices_to={'gender': 'F'}, related_name="%(app_label)s_%(class)s_related_mother")
    father = models.ForeignKey(Parent, limit_choices_to={'gender': 'M'}, related_name="%(app_label)s_%(class)s_related_father")

    def calculate_age(self, born):
        from datetime import date
        today = date.today()
        try:
            birthday = born.replace(year=today.year)
        except ValueError: # raised when birth date is February 29 and the current year is not a leap year
            birthday = born.replace(year=today.year, day=born.day-1)
        if birthday > today:
            return today.year - born.year - 1
        else:
            return today.year - born.year

    @property
    def age(self):
        admin_order_field = self.date_of_birth
        short_description = _('Age')
        allow_tags = True
        return self.calculate_age(self.date_of_birth)

    def __unicode__(self):
        return " ".join([self.first_name,self.middle_name,self.last_name])

    class Meta:
        abstract = True

class Group(models.Model):
    '''Holds kindergarten group information'''
    name = models.TextField('Name', primary_key=True, blank=False, null=False)
    amount_of_kids = models.PositiveIntegerField('Amount of Kids')
    max_amount_of_kids = models.PositiveIntegerField('Maximum Amount of Kids')
    min_age = models.PositiveIntegerField('Minimum Age of Kids')
    max_age = models.PositiveIntegerField('Maximum Age of Kids')

    def free_spots(self):
        admin_order_field = self.amount_of_kids
        short_description = 'Free Spots'
        allow_tags = True
        return self.max_amount_of_kids - self.amount_of_kids

    @property
    def amount_of_kids(self):
        admin_order_field = self.max_amount_of_kids
        short_description = 'Amount of Kids'
        allow_tags = True
        return len(Kid.objects.filter(group=self))

    def __unicode__(self):
        return "%s [Age: %s - %s | Amount: %s] " % (self.name, self.min_age, self.max_age, self.amount_of_kids)

class Kid(CommonInfoKid):
    '''Holds kids information'''
    group =  models.ForeignKey(Group, blank=True, null=True)
    waitlisted = models.BooleanField('On Waitlist', default=True)



