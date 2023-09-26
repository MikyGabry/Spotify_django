from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='About'),
    path('artists/', views.ArtistList.as_view(), name='artist_list'),
    path('songs/', views.SongList.as_view(), name='songs'),
    path('artists/new/', views.ArtistCreate.as_view(), name="artist_create"),
    path('artists/<int:pk>/', views.ArtistDetail.as_view(), name="artist_detail"),
]