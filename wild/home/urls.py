
from django.urls import path

from . import views


urlpatterns = [
    path('adp',views.addpost,name='adp'),
    path("cart",views.addtocart,name="addtocart"),
                path("",views.index,name='index'),
                path("index.html",views.index,name='index.html'),
                path("ci/<int:pk>", views.cmnt,name="comment"),
                path("faq",views.faq,name='faq.html'),
                path("know",views.know,name='know'),
                path("plan",views.plan,name='plan.html'),
                path("lk/<int:pk>", views.likeview,name="like_pst"),
                path("wild",views.wildopedia,name='wild'),
                path("rules",views.rules,name='rules'),
                path("serv",views.services,name='services.html'),
                path("det",views.details,name='details.html'),
                path("spon",views.sponser,name='sponser.html'),
                path("ser",views.search,name="ser"),
                path("cont",views.contact,name="cont"),
                path("<int:pid>",views.wild,name='wil'),
                 path("price",views.price,name="price"),
                  path("get_cart_data",views.get_cart_data,name="get_cart_data"),
    path("remove_package",views.remove_package,name="remove_package"),
    path("process_payment",views.process_payment,name="process_payment"),
    path("success_payment",views.success_payment,name="success_payment"),
    path("cancel_payment",views.cancel_payment,name="cancel_payment"),
                  path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path("chat", views.chat, name="chat"),
    path('chat/<str:room_name>/', views.room, name='room'),
    path('send-message/s/', views.send_message_view, name='send_message'),
          
               
   
    
    ]
