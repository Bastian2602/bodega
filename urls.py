from django.urls import include, path

from biblioteca import admin
from . import views
from .routes import viewsData
from .routes import viewsAdmin
from .views import SolicitudView
from .views import lista_solicitudes, nueva_solicitud
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Tu API",
      default_version='v1',
      description="Descripción de tu API",
      terms_of_service="https://www.tuapi.com/terms/",
      contact=openapi.Contact(email="contact@tuapi.com"),
      license=openapi.License(name="Tu Licencia"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
  path('', views.index, name='index'),
  path('auth/login', views.inicio_sesion, name='login'),
  path('auth/registrar', views.registar, name='registrar'),
  path('auth/recuperar', views.recuperar, name='recuperar'),
  path('auth/logout', views.cerrar_sesion, name='logout'),
  path('', lista_solicitudes, name='lista_solicitudes'),
  path('nueva/', nueva_solicitud, name='nueva_solicitud'),
  path('solicitudes/', lista_solicitudes, name='lista_solicitudes'),
  path('solicitudes/nueva/', nueva_solicitud, name='nueva_solicitud'),


  # pagina cliente
  path('home', views.home, name='home'),
  path('home/categoria/<url>', views.home_categoria, name='home_categoria'),
  path('home/libro/<codigo>', views.home_libro, name='home_libro'),
  path('home/producto/<id>', views.home_producto, name='home_producto'),

  # pagina administrador
  path('administrador', viewsAdmin.index, name='admin_index'),
  path('administrador/libro', viewsAdmin.admin_lista_libro, name='admin_lista_libro'),
  path('administrador/libro/create', viewsAdmin.admin_create_libro, name='admin_create_libro'),
  path('administrador/libro/<id>', viewsAdmin.admin_vista_libro, name='admin_vista_libro'),
  path('administrador/categoria', viewsAdmin.admin_lista_categoria, name='admin_lista_categoria'),
  path('administrador/categoria/create', viewsAdmin.admin_create_categoria, name='admin_create_categoria'),
  path('administrador/solicitudes/', SolicitudView.as_view(), name='solicitud'),
  path('admin/', views.admin_page, name='admin_page'),
  # path('administrador/categoria/<id>', viewsAdmin.admin_vista_categoria, name='admin_vista_categoria'),

  # LIBRO
  # path('libro', views.lista_libro, name='lista_libro'),
  # CATEGORIA
  # path('categoria', views.lista_categoria, name='lista_categoria'),

  # path('libro/<nombre>', views.vista_libro, name='vista_libro'),

  path('data', viewsData.data, name='data'),
  path('vista_api', views.vista_api, name='data'),
  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
