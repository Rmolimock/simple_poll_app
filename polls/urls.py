from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>', views.answers, name='answers'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('draft/', views.draft, name='draft'),
    path('create_question/', views.create_question, name='create_question'),
    path('add_answer/', views.add_answer, name='add_answer'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
