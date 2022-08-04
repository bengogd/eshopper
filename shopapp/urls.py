from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='home'),
    path('<int:listing_id>', views.detail_view, name='detail'),
    path('product/create/', views.create_product_view, name='create-product'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)