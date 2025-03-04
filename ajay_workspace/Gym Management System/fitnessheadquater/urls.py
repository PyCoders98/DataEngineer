from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", home, name="home_page"),
    path("login/", user_login, name="login_page"),
    path("signup/", signup, name="signup_page"),
    path("logout/", logout_page, name="logout_page"),
    path("buy-pack/<int:id>", buy_pack, name="buy_page"),
    path("buy-pack-confirm/<int:id>", buy_pack_confirm, name="buy_pack_confirm"),
    path("buy-pack/greeting-page/", greeting_page, name="greeting_page"),
    path("offer/", offer, name="offer_page"),
    path("membership/", membership, name="membership_page"),
    path("career/", career, name="career_page"),
    path("about/", about, name="aboutus_page"),
    path("contact-us/", contactus, name="contactus_page"),
    path("personnel-info/<int:id>", personnel_info, name="personnel_info"),
    path("update-personnel-info/<int:id>", update_personnel_info, name="update_personnel_info"),
    path("admin-home/", admin_home, name="admin_page"),
    path("admin-home/memberships/", admin_memberships, name="admin_memberships"),
    path("admin-home/memberships/update/<int:id>", update_memberships, name="update_memberships"),
    path("admin-home/memberships/delete/<int:id>", delete_memberships, name="delete_memberships"),
    path("admin-home/offers/", admin_offers, name="admin_offers"),
    path("admin-home/offers/update/<int:id>", update_offers, name="update_offers"),
    path("admin-home/offers/delete/<int:id>", delete_offers, name="delete_offers"),
    path("admin-home/members/", members, name="members_page"),
    path("admin-home/careers/", admin_career, name="careers_page"),
    path("admin-home/contact-us/", admin_contactus, name="admin_contactus_page"),

    # Password Reset
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="PasswordReset/password_reset_form.html"), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="PasswordReset/password_reset_done.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="PasswordReset/password_reset_confirm.html"), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(template_name="PasswordReset/password_reset_complete.html"), name="password_reset_complete"),
    
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
