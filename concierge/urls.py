from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from concierge import views

app_name = 'ads'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard_view, name='dashboard'),
    path('api/generate-task/', views.trigger_task_generation, name='api_generate_task'),
    path('api/concierge/plan/', views.ai_concierge_plan, name='api_concierge_plan'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)