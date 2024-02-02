
from django.urls import path
from .views import BinaryTreeApi,HomePageApi,ListTree,SearchApi
urlpatterns = [
    path('',HomePageApi.as_view()),
    path('add_binary_tree',BinaryTreeApi.as_view()),
    path('tree',ListTree.as_view()),
    # path('serch',SearchApi.as_view())
    
]
