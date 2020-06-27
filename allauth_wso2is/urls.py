# -*- coding: utf-8 -*-
from allauth_wso2is.provider import Wso2isProvider
from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns


urlpatterns = default_urlpatterns(Wso2isProvider)
