from django.conf.urls import url 
from .views.index import index,index_2
from .views.contact import email

urlpatterns = [   
    url(r'^$',index, name='index'), 
    url(r'^index',index, name='index'), 
    url(r'^test_index',index_2, name='index'), 
    url(r'^contact/email',email, name='email'),
] 