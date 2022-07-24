
from django.contrib import admin
from django.urls import path
from .views import home_view, main_view, main_view_async, sync_view_v2, async_view_v2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home-view'),
    path('sync/', main_view, name='sync-main-view'),
    path('async/', main_view_async, name='async-main-view'),
    path('v2/sync/', sync_view_v2, name='sync_view_v2'),
    path('v2/async/', async_view_v2, name='async_view_v2'),

]
