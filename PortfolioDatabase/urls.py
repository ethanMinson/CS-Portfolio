from django.urls import path, include

from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from .views import AddPortfolio

urlpatterns = [
    path("index", views.index, name="index"),
    path("", views.home, name="home"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path("hobbies/", views.hobbies_detailed, name="hobbies"),
    path("portfolio/detailed", views.portfolio_detailed, name="portfolio_detailed"),
    path("portfolio/add", csrf_protect(AddPortfolio.as_view()), name="portfolio_add"),
    path("portfolio/edit/<slug:slug>", views.portfolio_edit, name="portfolio_edit"),
    path("portfolio/delete/<slug:slug>", views.portfolio_delete, name="portfolio_delete"),
    path("login", views.login_page, name="login"),
    path("logout", views.logout_user, name="logout"),
    path("create_account/", views.create_account, name="create_account"),
    path("portfolio/<slug:slug>", views.portfolio_view, name="portfolio_view"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)