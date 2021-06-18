from django.views import generic
from django.urls import reverse_lazy
from .models import Testdata

class IndexView(generic.ListView):
    template_name = 'testapp/index.html'
    context_object_name = 'testdata_list'
    def get_queryset(self):
        """Return the all testdata."""
        return Testdata.objects.all()

class CreateView(generic.edit.CreateView):
    template_name = 'testapp/create.html'
    model = Testdata
    fields = ['name','age']
    success_url = reverse_lazy('testapp:index') 

class UpdateView(generic.edit.UpdateView):
    template_name = 'testapp/update.html'
    model = Testdata
    fields = ['name', 'age']
    success_url = reverse_lazy('testapp:index')


class DeleteView(generic.edit.DeleteView):
    template_name = 'testapp/delete.html' 
    model = Testdata
    success_url = reverse_lazy('testapp:index')