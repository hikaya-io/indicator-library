"""indicatorlibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework import routers
from indicatorlibrary.quickstart import views
import django.contrib.admin as admin

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'indicator', views.IndicatorViewSet)
router.register(r'source', views.SourceViewSet)
router.register(r'frequency',views.FrequencyViewSet)
router.register(r'additional_fields', views.AdditionalFieldsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^catalog/$', views.search, name = 'catalog'),
    url(r'^catalog/(?P<pk>\d+)$', views.IndicatorDetailView.as_view(), name='Indicator-view'),
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^about/$', views.about, name='about'),
    url(r'^add/$', views.add_indicator, name='add')
]