"""mvp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.views.generic import RedirectView
from rest_framework import routers
from rest_framework_extensions.routers import NestedRouterMixin

from api.views import Comments, Posts, Upvotes


class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
    """Class for nested routing."""


urlpatterns = [
    path("api/posts/<int:post_id>/upvote/", Upvotes.as_view()),
    path(
        r"favicon\.ico",
        RedirectView.as_view(url="/static/img/favicon.ico", permanent=True),
    ),
]

router = NestedDefaultRouter()

new_posts_router = router.register("api/posts", Posts)
new_posts_router.register(
    "comments",
    Comments,
    basename="posts-comments",
    parents_query_lookups=["post"],
)

urlpatterns += router.urls
