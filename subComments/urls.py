from django.urls import path
from . import views

urlpatterns = [
  path('get_subcomments/',views.getSubComments.as_view(),name='get-subcomments'),
  path('get_subcomments_by_id/<int:pk>/',views.getSubCommentById.as_view(),name='get-subcomments-by-id'),
  path('create_subComment/<int:pk>/',views.createSubComment.as_view(),name='create-subcomments'),
  path('delete_subcomment/<int:pk>/',views.deleteSubComment.as_view(),name='delete-subcomments'),
]
