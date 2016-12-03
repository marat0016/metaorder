from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView

class ExtraContext(object):
    extra_context = {}

    def get_context_data(self, **kwargs):
        context = super(ExtraContext, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

class ExtraListView(ExtraContext, ListView):
    pass

class ExtraDetailView(ExtraContext, DetailView):
    pass

class ExtraUpdateView(ExtraContext, UpdateView):
    pass

class ExtraCreateView(ExtraContext, CreateView):
    pass 

class ExtraDeleteView(ExtraContext, DeleteView):
    pass