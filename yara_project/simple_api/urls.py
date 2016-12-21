from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^purchase/$', views.PurchaseView.as_view(), name="Post purchases"),
    url(r'^purchase/(?P<pk>[0-9]+)$', views.PurchaseDetailView.as_view(), name="CRUD access for all purchases"),
]
