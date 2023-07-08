from kandidat import views
from django.urls import path, re_path
from kandidat.views import home,kandidat_add,kandidat_update,kandidat_all,kandidat_home,kandidat_delete,kandidat_delete_all,signin,register,signout

urlpatterns = [
    re_path(r'^api/kandidaten$', views.kandidaten_list,name="api-kandidat-list"),
    re_path(r'^api/kandidaten/(?P<pk>[0-9]+)$', views.kandidaten_detail,name="api-kandidat-detail"),
    re_path(r'^api/kandidaten/erwachsene$', views.kandidaten_list_erwachsene,name="api-kandidat-list_erwachsene"),
    path('',kandidat_home,name='kandidat-home'),
    path('kandidat/',kandidat_home,name='kandidat-home'),
    path('kandidat/<int:id>',kandidat_all,name='kandidat-all'),
    path('kandidat/add',kandidat_add,name='kandidat-add'),
    path('kandidat/update/<int:id>',kandidat_update,name='kandidat-update'),
    path('kandidat/delete/<int:id>',kandidat_delete,name="kandidat-delete"),
    path('kandidat/all/delete',kandidat_delete_all,name="kandidat-delete-all"),
    path('login',signin,name='login'),
    path('register',register,name='register'),
    path('logout',signout,name='logout'),

]
