from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, SearchView,
)

from .filters import NewsFilter
from .forms import NewsForm
from .models import News

class NewsList(ListView):
    model = News
    ordering = 'name'
    template_name = 'id_новости.html'
    context_object_name = 'id_новости'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewsDetail(DetailView):
    model = News
    template_name = 'news.html'
    context_object_name = 'news'


class NewsCreate(CreateView):
    form_class = NewsForm
    model = News
    template_name = 'news_edit.html'


class NewsUpdate(UpdateView):
    form_class = NewsForm
    model = News
    template_name = 'news_edit.html'

# Представление удаляющее товар.
class NewsDelete(DeleteView):
    model = News
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')


class NewsSearch(ListView):
    model = News
    ordering = 'name'
    template_name = 'news_search.html'
    context_object_name = 'id_новости'
    paginate_by = 2

