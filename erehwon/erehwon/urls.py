"""erehwon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.contrib import admin

from core.views import HomepageView

from profiles.views import logout_view, CallForActionView, ProjectFormView, project_list, project_update, idea_list, call_list
from profiles.forms import ErehwonUserSignUpForm

from registration.backends.hmac.views import RegistrationView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomepageView.as_view(), name="index"),
    url(r'^accounts/register/$', RegistrationView.as_view(form_class=ErehwonUserSignUpForm), name="registration_register"),
    url(r'^accounts/', include('registration.backends.hmac.urls')),  # This line includes automatically all views and urls for registration/activation/password reset
    url(r'^accounts/logout', logout_view, name="logout_view"),
    # url(r'^dashboard', loggedin_view, name="dashboard"),
    url(r'^projects', project_list, name="project_list"),
    # url(r'^project', ProjectFormView.as_view(), name="project_form"),
    url(r'^ideas', idea_list, name="idea_list"),
    url(r'^callforaction', call_list, name="call_list")

]
