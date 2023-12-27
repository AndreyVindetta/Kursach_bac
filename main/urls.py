from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.ClientDetailView.as_view(), name='client-detail'),
    path('<int:pk>/update', views.ClientUpdateView.as_view(), name='client-update'),
    path('<int:pk>/delete', views.ClientDeleteView.as_view(), name='client-delete')
]