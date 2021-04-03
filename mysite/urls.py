from django.contrib import admin
from django.urls import path, include
from polls.views import loginView, logoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('polls.urls')),
    path('login/', loginView, name="login"),
    path('logout/', logoutView, name="logout")
]
