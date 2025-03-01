from django.urls import path, include
from baseapp import views

app_name = "baseapp"

urlpatterns = [
    path("", views.home, name="HomePage"),
    path("register-user", views.register, name="register_user"),
    path("login-user", views.login_user, name="login_user"),
    path("login-user", views.logout_user, name="logout_user"),
    path("check-pet-health", views.check_pet_health, name="get_pet_health"),
    path("pet-adoption-status", views.pet_adoption_status, name="pet_adoption_status"),
    path("querytest", views.query_test, name="querytest"),
    path("faq-page", views.faq_page, name="faq_page"),
    path("pet-adoption-page", views.pet_adoption_page, name="pet_adoption_page"),
    path("pet-adoption-form", views.pet_adoption_form, name="pet_adoption_form"),
]
