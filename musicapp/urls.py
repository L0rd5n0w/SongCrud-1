from django.urls import path
from .views import artist_list, lyric_list, song_list
from .views import artist_prob, song_prob, lyric_prob
urlpatterns = [
    path('artist/', artist_list),
    path('artist/<str:first_name>/', artist_prob),
    path('lyric/', lyric_list),
    path('lyric/<str:song_id>/', lyric_prob),
    path('song/', song_list),
    path('song/<str:title>', song_prob)
]
