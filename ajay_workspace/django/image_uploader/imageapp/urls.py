from django.urls import path
from .views import *
urlpatterns=[
    path('',home,name='home_page'),
    path('admin_page/',upload_image,name='upload_image'),
    path('all-images/',get_all_images,name="get_all_images"),
    path('confirmation-page/<int:id>',confirmation_page,name="confirmation_page"),
    path('delete-image/<int:id>/',delete_image,name='delete_image'),
    path('edit-image/<int:id>/',edit_image,name='edit_image'),
]