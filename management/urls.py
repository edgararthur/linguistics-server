from django.urls import path
from .views import ConsultantsDetail, NewsList, NewsDetail, LeadershipList, CollaborationsList, CollaborationsDetail, ConsultantsList, MembersList
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('news/', NewsList.as_view(), name='news-list'),
    path('news/<int:pk>/', NewsDetail.as_view(), name='news-detail'),
    path('leadership/', LeadershipList.as_view(), name='leadership-list'),
    path('collaborations/', CollaborationsList.as_view(), name='collaborations-list'),
    path('collaborations/<int:pk>/', CollaborationsDetail.as_view(), name='collaborations-detail'),
    path('consultants/', ConsultantsList.as_view(), name='consultant-list'),
    path('consultant/<int:pk>/', ConsultantsDetail.as_view(), name='consultant-detail')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
