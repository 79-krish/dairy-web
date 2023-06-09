from django.urls import path,include
from .import views 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm ,mypasswordResetForm

urlpatterns= [
    path("",views.first),
    path("category/<slug:val>",views.Categoriview.as_view(),name="category"),
    path("product-detail/<int:pk>",views.ProductDetial.as_view(),name="product-detail"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    path('profile/',views.profileView.as_view(),name='profile'),
    path('address/',views.profileView.as_view(),name='address'),
    #login and resgitration authentication
    path('reset-password',auth_view.PasswordResetView.as_view (template_name='app/password_reset.html',form_class=mypasswordResetForm), name='password_reset'),
    path('regestration/',views.CustomerRegistrationView.as_view(),name='custmoerregestration'),
    path('accounts/login/',auth_view.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm),name='login')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)