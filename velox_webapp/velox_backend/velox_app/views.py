import logging

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Horse, MLModelMetadata, ScoreBins, Measure


@csrf_exempt
def update_stats(request):
    """Goes through all horses and updates/calculates stats"""
    logging.info('starting with updating stats')
    horses = Horse.objects.all()
    for horse in horses:
        horse.update_status_new()
    logging.info('updating stats completed')
    return HttpResponse('ok')


@csrf_exempt
def set_live(request):
    """Sets live status for horses with tf_reg"""
    logging.info('starting with updating stats')
    horses = Horse.objects.all()
    for horse in horses:
        horse.status = 'Unnamed'
        horse.save()
    logging.info('updating status completed')
    return HttpResponse('ok')


@csrf_exempt
def calculate_batch_elite(request):
    """For all horses, calculate race_rating and elite"""

    horses = Horse.objects.all()
    for horse in horses:
        starts_country = horse.starts_country
        if starts_country and horse.cpi_rating is not None:
            country_weight = starts_country.country_weight
            race_rating = country_weight * horse.cpi_rating
            horse.race_rating = race_rating
            horse.save()
    return HttpResponse('ok')


@csrf_exempt
def reset_stats(request):
    """"Resets stats for all horse"""
    horses = Horse.objects.all()
    for horse in horses:
        horse.starts = 0
        horse.race_rating = None
        horse.active = 'No'
        horse.elite = 'No'
        horse.status = 'Unnamed'
        horse.cpi_rating = None
        horse.save()
    return HttpResponse('ok')


@csrf_exempt
def sync_ml_models(request):
    """Load Model from Vertex AI"""
    from .vertex_ai import get_all_ml_models_metadata

    no_models = 10  # default number to get
    if request.GET:
        no_models = request.GET.get('number_of_models', no_models)
    ml_models = get_all_ml_models_metadata(no_models)
    for ml_model_data in ml_models:
        resource_name = ml_model_data['resource_name']
        try:
            MLModelMetadata.objects.get(resource_name=resource_name)
        except MLModelMetadata.DoesNotExist:
            logging.info(f'creating MLModelMetadata object {ml_model_data}')
            MLModelMetadata.objects.create(**ml_model_data)
    return HttpResponse('ok')


@csrf_exempt
def calculate_score_bins(request):
    """Recalculates Score Bins"""

    for _, prob_field in Measure.score_prob_fields:
        ScoreBins.create_bins(prob_field)

    return HttpResponse('ok')


@csrf_exempt
def save_measures(request):
    measures = Measure.objects.all()
    for measure in measures:
        measure.save()
    return HttpResponse('ok')
