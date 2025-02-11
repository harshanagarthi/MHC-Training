from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("employee", views.EmployeeViewSet, basename="employees")

urlpatterns = [
    path('students/', views.studentView),
    path('student/<int:pk>/', views.studentDetailView),

    # path('employees/', views.EmployeeView.as_view()),
    # path('employee/<int:pk>/', views.EmployeeDetailView.as_view()),
    path('', include(router.urls)),

    path('blogs/', views.BlogsView.as_view()),
    path('comments/', views.CommentsView.as_view()),

    path('blogs/<int:pk>/', views.BlogDetialView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view())
]