
from django.views.generic import DetailView

from account.models import CustomUser


class Account_PageView(DetailView):
    model = CustomUser
    template_name = 'account_site.html'
    context_object_name = 'blog'
    def get_context_data(self, **kwargs):
        cd = super().get_context_data(**kwargs)
        cd['text'] = "Account"
        return cd