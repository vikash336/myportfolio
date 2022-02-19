from portfolio import views
from django.conf.urls import url
urlpatterns=[
    url('vik',views.vik),
    url('contact',views.gus),
    url('test',views.emaill),
    url('download',views.download),


]
