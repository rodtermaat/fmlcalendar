from django.shortcuts import render
from django.db.models import Sum
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django import forms
from datetime import date
from .models import Check, Category

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_checks=Check.objects.all().count()
    tot_bal=Check.objects.all().aggregate(Sum('amount'))
    today_bal=Check.objects.filter(date__lte=date.today()).aggregate(Sum('amount'))
    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_checks':num_checks,'tot_bal':tot_bal, 'today_bal':today_bal,
            'num_visits':num_visits},
    )

def checkbookList(request):
    checks = Check.objects.all()
    balance = 0
    for chk in checks:
        balance += chk.amount
        chk.balance = balance

    return render(request, 'checkbook.html', {'checks': checks})



from django.views import generic

class CheckListView(generic.ListView):
    model = Check
    paginate_by = 10

    def get_context_data(self, **kwargs):
        #context = super(CheckListView, self).get_context_data(**kwargs)
        context = super().get_context_data(**kwargs)
        context['balance'] = '12'
        return context
        print(context)
        #balance = 0
        #for chk in Check:
        #    balance += chk.amount
        #    chk.balance = balance
        #    print (balance)

class CheckDetailView(generic.DetailView):
    model = Check

class CategoryListView(generic.ListView):
    model = Category
    paginate_by = 10

class CategoryDetailView(generic.DetailView):
    model = Category

class CheckForm(forms.ModelForm):
    class Meta:
        model = Check
        fields = ['date', 'type', 'category', 'name', 'amount', 'cleared']
        widgets = {
            'date': forms.TextInput(attrs={'class':'datepicker'})
        }

class CheckCreate(CreateView):
    form_class = CheckForm
    model = Check
    success_url = reverse_lazy('check-list')
    #fields = ['date', 'type', 'category', 'name', 'amount', 'cleared']

class CheckUpdate(UpdateView):
    model = Check
    success_url = reverse_lazy('check-list')
    fields = ['date', 'type', 'category', 'name', 'amount', 'cleared']
    #template_name_suffix = '_update_form'

class CheckDelete(DeleteView):
    model = Check
    success_url = reverse_lazy('check-list')
