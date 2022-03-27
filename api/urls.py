from django.urls import path
from api import views

app_name = 'api'
urlpatterns = [
    path("",views.ListItemAPIView.as_view(),name="item-list"),
    path("create/", views.CreateItemAPIView.as_view(),name="item-create"),
    path("update/<int:pk>/",views.UpdateItemAPIView.as_view(),name="update-item"),
    path("delete/<int:pk>/",views.DeleteItemAPIView.as_view(),name="delete-item"),
]