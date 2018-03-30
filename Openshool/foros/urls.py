from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:Pregunta_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:Pregunta_id>/results/', views.results, name='results'),

]
