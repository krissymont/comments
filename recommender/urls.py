from django.urls import include, path
from . import views

#app_name = 'recommender'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('best/', views.searchform_get, name='best'),
    path('recommender/bestp/', views.searchform_post, name='bestp'),
    path('info/<music_id>', views.info, name='info'),
    path(r'comments/', include('django_comments_xtd.urls')),
    ]
