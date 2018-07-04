from django.urls import path
from . import views

app_name ='board'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('<int:pk>/',views.DetailView.as_view(),name='detail'),
    path('board/<int:pk>/comment/new',views.commnet_new, name ='comment_new'),
    path('<int:board_pk>/comment/<int:pk>/edit',views.comment_edit, name ='comment_edit'),
    path('write_form', views.write_form, name = 'write_form'),
]