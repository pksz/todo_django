from django.urls import path,include
from . import views
#app urls here


urlpatterns = [
   path("",views.TaskList.as_view(),name='task'),
   path("task/<int:pk>/",views.TaskDetail.as_view(),name='task-detail'),
   path("task-create/",views.TaskCreate.as_view(),name='task-create'),
   path("task-update/<int:pk>/",views.TaskUpdate.as_view(),name='task-update'),
   path("task-delete/<int:pk>/",views.TaskDelete.as_view(),name='task-delete'),
   path("login/",views.UserLogin.as_view(),name='login'),
   path("logout/",views.UserLogout.as_view(),name='logout'),
   path("register/",views.UserRegister.as_view(),name='register'),

]