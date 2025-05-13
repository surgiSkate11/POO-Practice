from django.urls import path
from empleados.views import signup, signout, signin, empleado_create, empleado_list, empleado_update, empleado_delete, cargo_list, cargo_create, cargo_update, cargo_delete, departamento_list, departamento_create, departamento_update, departamento_delete, contrato_list, contrato_create, contrato_update, contrato_delete, rol_list, rol_create, rol_update, rol_delete

app_name = 'empleados'  # Nombre de la aplicación para el espacio de nombres

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('logout/', signout, name='logout'),
    path('signin/', signin, name='signin'),
    path('empleado_list/', empleado_list, name='empleado_list'),  # URL para la vista empleados
    path('empleado_create/', empleado_create, name='empleado_create'),  # URL para crear empleado
    path('empleado_update/<int:id>/', empleado_update, name='empleado_update'),  # URL para actualizar empleado
    path('empleado_delete/<int:id>/', empleado_delete, name='empleado_delete'),  # URL para eliminar empleado
    path('cargo_list/', cargo_list, name='cargo_list'),  # URL para la vista cargos
    path('cargo_create/', cargo_create, name='cargo_create'),
    path('cargo_update/<int:id>/', cargo_update, name='cargo_update'),
    path('cargo_delete/<int:id>/', cargo_delete, name='cargo_delete'),
    path('departamento_list/', departamento_list, name='departamento_list'),  # URL para la vista departamento
    path('departamento_create/', departamento_create, name='departamento_create'),
    path('departamento_update/<int:id>/', departamento_update, name='departamento_update'),
    path('departamento_delete/<int:id>/', departamento_delete, name='departamento_delete'),
    path('contrato_list/', contrato_list, name='contrato_list'),  # URL para la vista contrato
    path('contrato_create/', contrato_create, name='contrato_create'),
    path('contrato_update/<int:id>/', contrato_update, name='contrato_update'),
    path('contrato_delete/<int:id>/', contrato_delete, name='contrato_delete'),
    path('rol_list/', rol_list, name='rol_list'),  # URL para la vista rol
    path('rol_create/', rol_create, name='rol_create'),
    path('rol_update/<int:id>/', rol_update, name='rol_update'),
    path('rol_delete/<int:id>/', rol_delete, name='rol_delete'),
]
