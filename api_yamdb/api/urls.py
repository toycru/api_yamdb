from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet, UsersViewSet, create_token,
                    signup_user)

router_v1 = DefaultRouter()

# http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/
# http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/
router_v1.register(
    'titles/(?P<title_id>\\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)

# http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/
# http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
router_v1.register(
    'titles/(?P<title_id>\\d+)/reviews/(?P<review_id>\\d+)/comments',
    CommentViewSet,
    basename='reviews'
)
router_v1.register('titles', TitleViewSet)
router_v1.register('users', UsersViewSet, basename='users')
router_v1.register('categories', CategoryViewSet, basename='categories')
router_v1.register('genres', GenreViewSet, basename='genres')
router_v1.register('titles', TitleViewSet, basename='titles')

urlpatterns = [
    path('v1/auth/signup/', signup_user, name='signup'),
    path('v1/auth/token/', create_token, name='token'),
    path('v1/', include(router_v1.urls)),
]
