from django.urls import path ,include
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('artikel/',artikel, name='tabel_artikel'),
    path('artikel/tambah_artikel',tambah_artikel, name='tambah_artikel'),
    path('artikel/lihat/<str:id>',lihat_artikel, name='lihat_artikel'),
    path('artikel/edit/<str:id>',edit_artikel, name='edit_artikel'),
    path('artikel/hapus/<str:id>',hapus_artikel, name='hapus_artikel'),
    path('users/',users, name='tabel_users'),
]
