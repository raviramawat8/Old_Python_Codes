from django.conf.urls import url,include

from . import views

urlpatterns = [

            url(r'^$',views.index,name='index'),
            url(r'^index',views.page,name='page'),
#            url(r'^myindex',views.myindex,name='myindex'),
                ]
