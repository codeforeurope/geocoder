from django.conf.urls import patterns, include, url
from django.conf import settings
from tastypie.api import Api
from geo.api import *
from geo.views import *
from demo.views import DemoView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

v1_api = Api(api_name='v1')
# geo
v1_api.register(MunicipalityResource())
v1_api.register(MunicipalityBoundaryResource())
v1_api.register(AddressResource())
v1_api.register(POICategoryResource())
v1_api.register(POIResource())

base_urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'geocoder.views.home', name='home'),
    # url(r'^geocoder/', include('geocoder.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r"^", include(v1_api.urls)),
    url(r"^demo/$", DemoView.as_view()),
    url(r"^google/autocomplete/$", google_autocomplete),
    url(r"^google/details/$", google_details),
)

prefix = getattr(settings, 'URL_PREFIX', '')
urlpatterns = patterns('',
    url("^" + prefix, include(base_urlpatterns))
)
