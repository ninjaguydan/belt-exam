from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('add_quote', views.add_quote),
    path('<int:quote_id>/delete_quote', views.delete_quote),
    path('myaccount', views.edit),
    path('update', views.update_account),
    path('user/<int:profile_id>', views.profile),
    path('<int:quote_id>/like', views.like),
    path('<int:quote_id>/unlike', views.unlike),
]
