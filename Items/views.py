
from tempfile import template
from django.shortcuts import render
from django.urls import reverse_lazy
from Items.models import Items
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.

class ItemsListView(ListView):
    model = Items
    paginate_by = 10
    ordering = ['-created_date']
    context_object_name = 'item'
    template_name = "items_list.html"


class ItemsCreateView(CreateView):
    model = Items
    fields = ['title', 'description', 'deadline']
    template_name = "items_create.html"
    success_url = reverse_lazy('item:item-list')


class ItemsDetailView(DetailView):
    model = Items
    template_name = 'items_detail.html'
    context_object_name = 'items'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super(ItemsDetailView, self).get_context_data(**kwargs)
        context['items'] = Items.objects.all()
        return context

class ItemsUpdateView(UpdateView):
    model = Items
    fields = ['title', 'description', 'deadline']
    template_name = "items_update.html"
    success_url = reverse_lazy('item:item-list')

class ItemsDeleteView(DeleteView):
    model = Items
    template_name = "items_delete.html"
    success_url = reverse_lazy('item:item-list')
