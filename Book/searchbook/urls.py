from django.urls import path
from . import views

app_name = 'book'
urlpatterns = [
    path('', views.main, name="main"),
    path('search', views.search, name="search"),
    path('bookdelete', views.delete_all_book, name="delete_all_book"),
    path('userdelete', views.delete_all_user, name="delete_all_user"),
    
    # 발표자 저장
    path('usersave', views.save_one_user, name="save_one_user"),
   
    path('save', views.save, name="save"),
    # html에서 보낸 name의 값을 가져온다
    path('<int:data_id>/delete', views.delete_one, name="delete_one", ),
    # db에 저장된 값을 모두 불러온다
    path('call', views.call, name="call", ),
]
