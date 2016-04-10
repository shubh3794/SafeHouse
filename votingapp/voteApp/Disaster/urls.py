from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'disaster',
                views.DisasterView)
router.register(r'help',
                views.HelpViewSet)

urlpatterns = [
	url(r'^sys/', include(router.urls)),
	url(r'^mobhelp/$',
                views.GetCurrUserList.as_view()),
	url(r'^mobhelp/unsafeuser/$',
                views.GetSafeCurrUserList.as_view()),

]
