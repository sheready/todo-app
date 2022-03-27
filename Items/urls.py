from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from Items.views import ItemsCreateView, ItemsDeleteView,ItemsUpdateView,ItemsListView,ItemsDetailView

app_name = 'item'
urlpatterns = [
    path('', ItemsListView.as_view(), name='item-list'),
    path('create/', login_required(ItemsCreateView.as_view()), name='item-create'),
    path('delete/<int:pk>', login_required(ItemsDeleteView.as_view()), name='item-delete'),
    path('update/<int:pk>', login_required(ItemsUpdateView.as_view()), name='item-update'),
    path('detail/<int:pk>', login_required(ItemsDetailView.as_view()), name='item-detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
