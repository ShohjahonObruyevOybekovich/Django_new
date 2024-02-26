from audioop import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from account.form import AccountForm


# Create your views here.


@login_required(login_url='/login/')
def account_site(request):
    form = AccountForm()
    if form.is_valid():
        blog=form.save()
        return redirect(reverse('account:account_site',{'blog':blog}))
