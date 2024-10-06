from django.urls import path
from . import views
urlpatterns = [
  path('get_comments/',views.GetComments.as_view(),name="get-comments"),
  path('get_comments_by_sim/<int:pk>/',views.GetCommentsBySim.as_view(),name="get-comments-by-sim"),
  path('add_comment/<int:pk>/',views.CreateComment.as_view(),name="create-comment"),
  path('delete_comment/<int:pk>/',views.DeleteComment.as_view(),name="delete-comment"),
]
