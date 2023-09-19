from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from New_work import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('form/', views.form_1, name='login'),
    path('pet/', views.form_2, name='pet'),
    path('all-pets/', views.see_pets, name='all_pets'),
    path('third/', views.third, name='third'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
