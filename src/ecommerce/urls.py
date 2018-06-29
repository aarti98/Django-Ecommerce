from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
# from products.views import product_list_view, product_detail_view, ProductListView, ProductDetailView, ProductFeaturedListView, ProductFeaturedDetailView, ProductDetailSlugView
from .views import home_page, about_page, contact_page, login_page, register_page
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_page, name='home'),
    url(r'^about/$', about_page, name='about'),
    url(r'^contact/$', contact_page, name='contact'),
    url(r'^login/$', login_page, name='login'),
    url(r'^register/$', register_page, name='register'),
    url(r'^products/', include("products.urls", namespace='products')),
url(r'^search/', include("search.urls", namespace='search')),
    url(r'^bootstrap/', TemplateView.as_view(template_name='bootstrap/example.html')),
    # url(r'^products/$', ProductListView.as_view()),
    # url(r'^products-fbv/$', product_list_view),
    # url(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view()),
    # url(r'^products/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
    # url(r'^products-fbv/(?P<pk>\d+)/$', product_detail_view),
    # url(r'^featured/$', ProductFeaturedListView.as_view()),
    # url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),

]


if settings.DEBUG:

    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)