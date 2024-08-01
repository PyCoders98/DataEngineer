from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from .views import AuthorViewSet, BookViewSet

# Create the main router
router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='author')

# Create a nested router for books
nested_router = NestedDefaultRouter(router, r'authors', lookup='author')
nested_router.register(r'books', BookViewSet, basename='author-books')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(nested_router.urls)),
]