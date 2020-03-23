from django.urls import path
from . import views

# second app에서 사용할 모든 views를 가져온다.

# mainpage라는 views가 루트url에 할당된다.
# 웹사이트에 http://127.0.0.1:8000/으로 들어가면
# views.mainpage를 보여주라고함.
# name= 은 url에 이름을 붙여서 views를 식별함. 뷰의이름과 다를수도있음.
urlpatterns = [
    path('', views.mainpage, name='mainpage'),  #조회페이지
    #path('', views.mainpage, name='mainpage'),     #지도 페이지
    path('second/new', views.map_new, name='map_new'),
    # path('second/maplist', views.map_new, name='maplist'),
    path('second/maplist', views.maplist, name='maplist'),
    path('second/mainpage', views.mainpage, name='mainpage'),
    # path('second/success', views.success, name='success'),
]
