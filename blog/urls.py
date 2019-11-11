# from django.conf.urls import url

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # path('',views.post_list,name = 'post_list'),
    path('',views.PostListView.as_view(),name = 'post_list'),
    path('blog/<int:year>/<int:month>/<int:day>/<str:post>/', views.post_detail,name='post_detail')

]
