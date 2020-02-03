from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crossroad/', views.crossroad, name='crossroad'),
    path('createpost/', views.createpost, name='createpost'),
    path('<int:posts_id>/<int:liker_id>/like', views.like, name='like'),
    path('<int:posts_id>/<int:commenter_id>/comment', views.comment, name='comment'),
]