from django.urls import path

from . import views

app_name = "check_arrangement"
urlpatterns = [
    path('', views.index, name='index'),
    path('add_apartment/', views.add_apartment, name='add_apartment'),
    path('delete_apartment/<int:apartment_id>', views.delete_apartment, name='delete_apartment'),
    path('delete_issue/<int:apartmentissues_id>/', views.delete_issue, name='delete_issue'),
    path('add_issue/<int:apartment_id>/', views.add_issue, name="add_issue"),
    path('sheets/<int:apartment_id>/', views.sheets, name='sheets'),
    path('sheets/to_delivery/<int:apartment_id>/', views.to_delivery, name='to_delivery'),
    path('sheets/delivery/<int:sheet_id>/', views.delivery, name='delivery'),
    path('sheets/handled/<int:sheet_id>/', views.handled, name='handled'),
    path('sheets/unavailable/<int:sheet_id>/', views.unavailable, name='unavailable'),
    path('sheets/update_to_not_handled/<int:apartment_sheet_handled_id>/', views.update_to_not_handled, name='update_to_not_handled'),
    path('<int:apartment_id>/results/', views.results, name="results"),
]
