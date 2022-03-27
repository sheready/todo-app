from django.urls import path
from Items.views import ItemsCreateView, ItemsDeleteView,ItemsUpdateView,ItemsListView,ItemsDetailView

app_name = 'item'
urlpatterns = [
    path('', ItemsListView.as_view(), name='item-list'),
    path('create/', ItemsCreateView.as_view(), name='item-create'),
    path('delete/<int:pk>', ItemsDeleteView.as_view(), name='item-delete'),
    path('update/<int:pk>', ItemsUpdateView.as_view(), name='item-update'),
    path('detail/<int:pk>', ItemsDetailView.as_view(), name='item-detail'),
]