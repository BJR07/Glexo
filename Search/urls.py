from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('history/',views.history,name='history'),
    path('delete-history/<int:id>/',views.delete_history,name='delete_history'),
    path(
    'document/<int:id>/',
    views.document_detail,
    name='document_detail'
),
    



]