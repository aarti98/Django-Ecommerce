from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LogoutView, LoginView
from addresses.views import checkout_address_create_view, checkout_address_reuse_view
from accounts.views import LoginView, RegisterView, guest_register_view
from .views import home_page, about_page, contact_page
from carts.views import cart_detail_api_view
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_page, name='home'),
    url(r'^about/$', about_page, name='about'),
    url(r'^contact/$', contact_page, name='contact'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^checkout/address/create/$', checkout_address_create_view, name='checkout_address_create'),
    url(r'^checkout/address/reuse/$', checkout_address_reuse_view, name='checkout_address_reuse'),
    url(r'^register/guest/$', guest_register_view, name='guest_register'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^api/cart/$', cart_detail_api_view, name='api-cart'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^products/', include(("products.urls", 'products'), namespace='products')),
    url(r'^cart/', include(("carts.urls", 'carts'), namespace='cart')),
    url(r'^search/', include(("search.urls", 'search'), namespace='search')),
    url(r'^bootstrap/', TemplateView.as_view(template_name='bootstrap/example.html')),

]


if settings.DEBUG:

    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
