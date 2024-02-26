from django.urls import path

from .views import login_view, logout_view, signup_view, detail_blog, edit_blog
from .views_cbv import CreateBlogView, HomePageView

app_name = 'app'

urlpatterns = [
    # path('', home, name='home'),
    # path('create/', create_blog, name='create'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('blog/<int:id>', detail_blog, name='detail'),
    path('blog/<slug:slug>', edit_blog, name='edit'),

]

urlpatterns_cbv = [
    path('', HomePageView.as_view(), name='home'),
    path('create', CreateBlogView.as_view(), name='create'),
]
urlpatterns += urlpatterns_cbv