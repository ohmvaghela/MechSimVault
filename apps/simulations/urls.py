from django.urls import path
from . import views

urlpatterns = [
  path("add_sim/",views.AddSimulation.as_view(),name="add-simulation"),
  path("update_sim/<int:pk>",views.UpdateSimulation.as_view(),name="update-sim"),
  path("delete_sim/<int:pk>",views.DeleteSimulation.as_view(),name="delte-sim"),
  path("get_sim/",views.GetSims.as_view(),name="get-sim"),
  path("get_sim_by_id/<int:pk>",views.GetSimsByID.as_view(),name="get-sim-by-id"),
  path("get_sim_by_simid/<int:pk>",views.GetSimBySimId.as_view(),name="get-sim-by-simid"),
  path("add_likes/<int:user_id>/<int:sim_id>/",views.AddLike.as_view(),name="add-likes"),
  path("get_likes_by_sim/<int:sim_id>/",views.GetLikesBySim.as_view(),name="get-likes-by-sim"),
]
