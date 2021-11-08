
from django.contrib import admin
from django.urls import path,re_path,include
from django.conf import settings
from django.conf.urls.static import static
admin.site.site_header  =  "Custom bookstore admin"  
admin.site.site_title  =  "Custom bookstore admin site"
admin.site.index_title  =  "Custom Bookstore Admin"
urlpatterns = [
    path('jet/',include('jet.urls','jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    re_path('', include('applications.users.urls')),
    re_path('', include('applications.cliente.urls')),
    re_path('funcionario', include('applications.funcionario.urls')),
    re_path('',include('applications.reportesReserva.urls'))

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
