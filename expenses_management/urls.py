
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', include('expenses.urls')),
    path('', include('user_authentication.urls')),
    path('settings/', include('settings_app.urls')),
    path('income/', include('income.urls'))
    
]
