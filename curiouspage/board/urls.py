from django.urls import path
from . import views

app_name ='board'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('<int:pk>/',views.DetailView.as_view(),name='detail'),
    path('board/<int:pk>/comment/new',views.commnet_new, name ='comment_new'),
    path('write_form', views.write_form),
    path('do_write_board',views.do_write_board),
  #  path('write', views.Write_Board_Crate.as_view(), name='write'),
]