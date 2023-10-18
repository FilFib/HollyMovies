from django.shortcuts import render
# from django.http import HttpResponse
from viewer.models import Movie
from django.views.generic import ListView, FormView, CreateView, UpdateView, DeleteView
# from django.views import View
from viewer.forms import MovieForm
from logging import getLogger
from django.urls import reverse_lazy

# Create your views here.

LOGGER = getLogger()

class MovieCreateView(CreateView):

  template_name = 'form.html'
  form_class = MovieForm
  success_url = reverse_lazy('movie_create')

#   def form_valid(self, form):
#     result = super().form_valid(form)
#     cleaned_data = form.cleaned_data
#     Movie.objects.create(
#       title=cleaned_data['title'],
#       genre=cleaned_data['genre'],
#       rating=cleaned_data['rating'],
#       released=cleaned_data['released'],
#         description=cleaned_data['description']
#     )
#     return result

  def form_invalid(self, form):
    LOGGER.warning('User provided invalid data.')
    return super().form_invalid(form)


class MovieUpdateView(UpdateView):

  template_name = 'form.html'
  model = Movie
  form_class = MovieForm
  success_url = reverse_lazy('index')

  def form_invalid(self, form):
    LOGGER.warning('User provided invalid data while updating a movie.')
    return super().form_invalid(form)


class MovieDeleteView(DeleteView):
  template_name = 'movie_confirm_delete.html'
  model = Movie
  success_url = reverse_lazy('index')


def hello(request, s0):
  s1 = request.GET.get('s1', '')
  return render(
    request, template_name='hello.html',
    context={'adjectives': [s0, s1, 'beautiful', 'wonderful']}
  )


class MoviesView(ListView):
  template_name = 'movies.html'
  model = Movie



# def movies(request):
#   return render(
#     request, template_name='movies.html',
#     context={'movies': Movie.objects.all()}
#   )


# class MoviesView(View):
#     def get(self, request):
#         return render(
#         request, template_name='movies.html',
#         context={'movies': Movie.objects.all()}
#         )