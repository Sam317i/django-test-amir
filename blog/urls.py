from django.urls import path

from . import views

urlpatterns = [

    # Delete post url : '/post/ID NUMBER FOR EACH VIEW/delete/'
    path('post/<int:pk>/delete/', views.BlogDeleteView.as_view(), name = 'post_delete'),

    # Edit post url : '/post/ID NUMBER FOR EACH VIEW/edit/'
    path('post/<int:pk>/edit/', views.BlogUpdateView.as_view(), name = 'post_edit'),

    # New post url : '/post/new/'
    path('post/new/', views.BlogCreateView.as_view() , name = 'post_new'),

    # Urls of our detail view : '/post/ID NUMBER FOR EACH VIEW/'
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name = 'post_detail'),

    # Homepage url(blank)
    path('', views.BlogListView.as_view(), name = 'home'),

]