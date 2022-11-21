from rest_framework import routers
from django.urls import path, include
from django.contrib.admin.views.decorators import staff_member_required

from . import views
from . import views_api
from . import admin_views

router = routers.DefaultRouter()
router.register(r'upload', views_api.GCSUploadView, basename='upload')
router.register(r'horses', views_api.HorseAPIView)
router.register(r'measures', views_api.MeasureAPIView)
router.register(r'mlmodels', views_api.MLModelMetadataAPIView)
router.register(r'users', views_api.UserAPIView)
router.register(r'image-measurements', views_api.ImageMeasurementAPIView)
router.register(r'country-weights', views_api.CountryWeightAPIView)


urlpatterns = [
    path('api/', include(router.urls)),
    # path('', views.MainHandler.as_view(), name='index'),

    path('upload-horses', staff_member_required(admin_views.UploadHorsesHandler.as_view()), name='upload-horses'),
    path('upload-horses-success', staff_member_required(admin_views.UploadHorsesSuccessHandler.as_view()),
         name='upload-horses-success'),
    path('tasks/calculate-elite', views.calculate_batch_elite, name='task-calculate-batch-elite'),
    path('tasks/update-stats', views.update_stats, name='task-update-stats'),
    path('tasks/reset-stats', views.reset_stats, name='task-reset-stats'),
    path('tasks/set-live', views.set_live, name='task-set-live'),
    path('tasks/sync-ml-models', views.sync_ml_models, name='sync-ml-models'),
    path('tasks/calculate-score-bins', views.calculate_score_bins, name='calculate-score-bins'),
    path('tasks/save-measures', views.save_measures, name='save-measures'),

]
