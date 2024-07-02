from django.urls import path,include
from myApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('',views.home,name="home"),
  path('register/',views.registrationView,name="register"),
  path('login/',views.loginView,name="login"),
  path('logout/',views.logoutView,name='logout')
]+static(settings.STATIC_URL,
          document_root=settings.STATIC_ROOT)
