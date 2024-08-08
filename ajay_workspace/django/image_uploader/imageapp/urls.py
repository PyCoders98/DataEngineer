from django.urls import path
from .views import *
from .views import Home
from django.urls import path
from .context_processor import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("home/", Home.as_view(), name="home_page"),
    path("", Explore.as_view(), name="explore_page"),
    path("image-portfolio/<int:id>", image_portfolio, name="image_portfolio"),
    path("comment-page/<int:id>/", comment_page, name="comment_page"),
    path("get_image/<int:id>/", get_image, name="get_image"),
    path("upload_page/", upload_image, name="upload_image"),
    path(
        "getlikedislikecount/<int:id>",
        get_like_dislike_count,
        name="get_like_dislike_count",
    ),
    path("profile/", profile, name="profile"),
    path("view-profile-image/<int:id>", view_profile_image, name="view_profile_image"),
    path(
        "update-profile-image/",
        UpdateProfileImageView.as_view(),
        name="updateprofileimage",
    ),
    path(
        "delete-profile-image/",
        DeleteProfileImageView.as_view(),
        name="delete_profile_image",
    ),
    path("confirmation-page/<int:id>", confirmation_page, name="confirmation_page"),
    path("delete-image/<int:id>/", delete_image, name="delete_image"),
    path("edit-image/<int:id>/", edit_image, name="edit_image"),
    path("follow/<int:id>/", follow_request, name="follow_request"),
    path("all-requests/", all_requests, name="all_requests"),
    path("accept-request/<int:id>/", accept_request, name="accept_request"),
    path("signup/", sign_up, name="sign_up"),
    path("login/", login_fun, name="login"),
    path("logout/", logout_fun, name="logout"),
    path("logout_confirm/", logout_confirm, name="logout_confirm"),
    # password reset urls
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(template_name="password_reset_form.html"),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
