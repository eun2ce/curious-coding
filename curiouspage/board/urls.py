from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name ='board'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),    #main page
    path('<int:pk>/',views.DetailView.as_view(),name='detail'), #detail page
    path('write_form', views.write_form, name = 'write_form'), #write board
    path('<int:pk>/write_eidt',views.write_eidt, name = 'write_eidt'),  #w edit write
    path('board/<int:pk>/comment/new',views.commnet_new, name ='comment_new'), #new comment
    path('<int:board_pk>/comment/<int:pk>/edit',views.comment_edit, name ='comment_edit'), # edit comment
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)