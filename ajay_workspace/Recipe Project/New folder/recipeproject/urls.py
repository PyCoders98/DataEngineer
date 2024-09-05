
from django.contrib import admin
from django.urls import path
from recipeapp.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
# from registration import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("add-receipes",receipes,name="add-receipe"),
    path("receipes/", receipes, name="add-receipe"),
    path("all-receipes/", show_all, name="show-all"),
    path("", index, name="index"),
    path("delete-receipe/<int:id>/", delete_receipe, name="delete"),
    path("update-receipe/<int:id>/", update_receipe, name="update"),
    path("login-page/", login_page, name="login"),
    path("register-page/", register_page, name="register"),
    path("logout-page/", logout_page, name="logout"),
    path("view-receipe/<int:id>", view_receipe, name="view-receipe"),

    # password reset urls

    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="password_reset_form.html"), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name="password_reset_complete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()  # for serving_
