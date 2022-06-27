# from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path, include



urlpatterns = [

    path ('parent/', views.ParentViewSet.as_view() , name = "parent"),
    path ('parent/<int:pk>/', views.ParentDetailView.as_view() , name = "parent-detail"),
    path ('children/', views.ChildrenViewSet.as_view() , name = "children"),
    path ('children/<int:pk>/', views.ChildrenDetailView.as_view() , name = "children-detail")
    # path('api/',include(router.urls))
]