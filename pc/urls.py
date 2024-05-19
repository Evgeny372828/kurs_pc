from django.contrib import admin
from django.urls.conf import path, include
from django.conf import settings
from django.conf.urls.static import static
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('', index,name='glavn'),
    path('katalog/', katalog,name='kstslog'),
    path('katalog/<int:id>/', kateg, name='tovar'),
    path('katalog-filter/<int:stat_id>/',filter,name='stat'),
    path('katalog-inform-tovar/<int:pk>/',inform,name='inform'),
    path('new',new),
    path('poisk',sarch,name='search'),
    path('reg',reg,name='reg'),
    path('prof',prof,name='profile'),
    path('login/',LoginUser.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('about_us/',about,name='us'),
    path('politik/',politik,name='polit'),
    path('servis/',servis,name='servis'),
    path('social/',social,name='social')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
