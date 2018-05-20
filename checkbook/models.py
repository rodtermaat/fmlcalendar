from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Check(models.Model):

    """
    Model representing a checkbook transaction.
    """
    check_type = (
        ('CR', 'credit'),
        ('DR', 'debit'),
    )
    #theuser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(help_text='Enter the date of the transaction')
    type = models.CharField(max_length=2, choices=check_type, help_text='Enter credit or debit')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because a transaction can only have one category,
    # but categories can have multiple transactions
    # category as a string rather than object because it hasn't been
    # declared yet in the file.
    name = models.CharField(max_length=100, help_text='Enter description')
    amount = models.IntegerField(default=0, help_text='Enter amount')
    cleared = models.BooleanField(default=False, help_text='Is transaction cleared with the bank?')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return f'{self.date} {self.name} {self.amount}'

    def short_description(self):
        return self.name[:25]

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this transaction.
        """
        return reverse('check-detail', kwargs={'pk': self.pk})

class Category(models.Model):

    """
    Model representing a Category.
    """
    name = models.CharField(max_length=100, help_text='Enter a category name')
    frequency = models.CharField(max_length=10, null=True, blank=True, help_text='Enter M(monthly) or W(weekly)')
    budget = models.IntegerField(default=0, help_text='Enter budgeted amount by frequency' )

    class Meta:
        ordering = ["name"]

    def get_absolute_url(self):
        """
        Returns the url to access a particular category instance.
        """
        #return reverse('category-detail', args=[str(self.id)])
        return reverse('category-detail', kwargs={'pk': self.pk})

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0}'.format(self.name)
