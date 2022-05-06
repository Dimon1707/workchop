from django.urls import path


from core.views import index, index1

urlpatterns = [
    path('', index, name='index'),
    path('mainpage/', index1, name='index'),
]
