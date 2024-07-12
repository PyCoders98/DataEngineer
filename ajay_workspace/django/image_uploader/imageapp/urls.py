from django.urls import path
from .views import *
from django.urls import path
from .context_processor import *


urlpatterns = [
    path("", home, name="home_page"),
    path("image-portfolio/<int:id>", image_portfolio, name="image_portfolio"),
    path("comment-page/<int:id>/", comment_page, name="comment_page"),
    path("get_image/<int:id>/", get_image, name="get_image"),
    path("upload_page/", upload_image, name="upload_image"),
    path("all-images/", get_all_images, name="get_all_images"),
    path("profile/", profile, name="profile"),
    path("update-profile-picture/<int:id>",update_profile_picture,name="update_profile_picture"),
    path("confirmation-page/<int:id>", confirmation_page, name="confirmation_page"),
    path("delete-image/<int:id>/", delete_image, name="delete_image"),
    path("edit-image/<int:id>/", edit_image, name="edit_image"),
    path("signup/", sign_up, name="sign_up"),
    path("login/", login_fun, name="login"),
    path("logout/", logout_fun, name="logout"),
    path("logout_confirm/", logout_confirm, name="logout_confirm"),
   
]
