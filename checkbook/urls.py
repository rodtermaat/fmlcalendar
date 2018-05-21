from django.urls import path
from .views import CheckCreate, CheckDelete, CheckUpdate, CategoryCreate, CategoryDelete, CategoryUpdate
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('checkbookList', views.checkbookList, name='checkbook'),
    path('checks/', views.CheckListView.as_view(), name='check-list'),
    path('check/add/', views.CheckCreate.as_view(), name='check-add'),
    path('check/<int:pk>/', views.CheckUpdate.as_view(), name='check-detail'),
    path('check/<int:pk>/delete/', CheckDelete.as_view(), name='check-delete'),
    #path('check_form/', views.CheckCreate.as_view(), name='addcheck'),
    #path('check_update_form/<int:pk>', views.CheckUpdate.as_view(), name='updcheck'),
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    #path('category/<int:pk>', views.CategoryDetailView.as_view(), name='category-detail'),
    path('category/add/', views.CategoryCreate.as_view(), name='category-add'),
    path('category/<int:pk>/', views.CategoryUpdate.as_view(), name='category-detail'),
    path('category/<int:pk>/delete/', CategoryDelete.as_view(), name='category-delete'),

]
