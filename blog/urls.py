from django.urls import path

from .views import *


urlpatterns = [
    path('', PostView.as_view(), name='PostList'),
    path('category/<int:cat_id>/', PostCategoryView.as_view(), name='PostListCategory'),
    path('detail/<slug:post_slug>/', PostDetail.as_view(), name='PostDetail'),
    path('update/<slug:post_slug>/', PostEdit.as_view(), name='PostEdit'),
    path('createpost/', AddPost.as_view(), name='AddPost'),
    path('createcategory/', AddCategory.as_view(), name='AddCategory'),
    path('register/', RegisterUser.as_view(), name='Register'),
    path('login/', LoginUser.as_view(), name='Login'),
    path('logout/', logOutUser, name='Logout'),
    path('movieList/', MovieList.as_view(), name='MovieList'),
    path('movieCategory/<int:genre_id>/', MovieCategoryView.as_view(), name='MovieCategory'),
]
