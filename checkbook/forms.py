from django import forms
from .models import Check, Category
#from django.core.exceptions import ValidationError
#from django.utils.translation import ugettext_lazy as _
#import datetime #for checking renewal date range.

class AddCheckForm(forms.Form):

    """
    Add checkbook transaction.
    """
    check_type = (
        ('CR', 'credit'),
        ('DR', 'debit'),
    )
    date = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}),
        help_text='Enter the date of the transaction')
    type = forms.ChoiceField(choices=check_type, help_text='Enter credit or debit')
    category= forms.ModelChoiceField(queryset = Category.objects.all() )
    #a_category = forms.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    name = forms.CharField(help_text='Enter description')
    amount = forms.IntegerField(help_text='Enter amount')
    cleared = forms.BooleanField(help_text='Is transaction cleared with the bank?')

    #renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    # def clean_renewal_date(self):
    #     data = self.cleaned_data['renewal_date']
    #
    #     #Check date is not in past.
    #     if data < datetime.date.today():
    #         raise ValidationError(_('Invalid date - renewal in past'))
    #
    #     #Check date is in range librarian allowed to change (+4 weeks).
    #     if data > datetime.date.today() + datetime.timedelta(weeks=4):
    #         raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))
    #
    #     # Remember to always return the cleaned data.
    #     return data
