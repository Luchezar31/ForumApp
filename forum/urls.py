from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from forum import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('post/',include([
        path('add/',views.post_create_view,name='add-post'),
        path('edit/<int:pk>',views.post_edit_form,name='edit-post'),
        path('details/<int:pk>',views.post_details_view,name='detail-post'),
        path('delete/<int:pk>',views.post_delete_view,name='delete_post')
    ]))
]



