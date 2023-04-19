from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns= [
    path("",views.first),
    path("category/<slug:val>",views.Categoriview.as_view(),name="category"),
    path("product-detail/<int:pk>",views.ProductDetial.as_view(),name="product-detail")
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)