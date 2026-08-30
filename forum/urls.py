
from django.urls import path, include

from forum import views

urlpatterns = [
    path('',views.DashboardView.as_view(),name='dashboard'),
    path('post/',include([
        path('add/',views.PostCreateView.as_view(),name='add-post'),
        path('approve/<int:pk>',views.approve_view,name='approve'),
        path('edit/<int:pk>',views.EditPostView.as_view(),name='edit-post'),
        path('details/<int:pk>',views.PostDetailView.as_view(),name='detail-post'),
        path('delete/<int:pk>',views.DeletePostView.as_view(),name='delete_post')
    ]))
]



