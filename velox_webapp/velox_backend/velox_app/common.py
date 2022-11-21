import logging
import time

import requests

from google.cloud import storage
from django.conf import settings

gcs = storage.Client(project=settings.GCP_PROJECT).from_service_account_json(settings.GCP_SERVICE_ACCOUNT_FILE)


def score_tabular_prediction(service_url: str, input_data: dict) -> str:
    """Making request to a service that serves tabular model
    :param service_url - full url for the service
    :param input_data - dictionary of input data, corresponding to the prediction service
    """
    data = {'instances': [input_data]}
    logging.info(f'sending prediction data {data}')
    while True:
        r = requests.post(service_url, json=data)
        response_data = r.json()
        logging.info(f'prediction input data {data} response {r.text}')
        if r.status_code == 200:
            predictions = response_data.get('predictions', [])
            probability = None
            if len(predictions):
                result = predictions[0]
                classes = result['classes']
                scores = result['scores']
                index = classes.index('Yes')
                probability = scores[index]
                probability = str(probability)[0:11]
                return probability
            else:
                logging.error('no predictions')
                break
        elif r.status_code == 400:
            error = response_data.get('error', '')
            if error == "failed to connect to all addresses":
                time.sleep(1)
            else:
                break
        else:
            logging.error(f'error from prediction service {service_url} {r.status_code} {r.text}')
            break


def score_tabular_classification_prediction(service_url: str, input_data: dict) -> str:
    """Making request to a service that serves tabular classification model
    :param service_url - full url for the service
    :param input_data - dictionary of input data, corresponding to the prediction service
    """
    data = {'instances': [input_data]}
    logging.info(f'sending prediction data {data}')
    while True:
        r = requests.post(service_url, json=data)
        response_data = r.json()
        logging.info(f'prediction input data {data} response {r.text}')
        if r.status_code == 200:
            predictions = response_data.get('predictions', [])
            if len(predictions):
                result = predictions[0]
                classes = result['classes']
                scores = result['scores']
                max_val = max(scores)
                max_index = scores.index(max_val)
                res = classes[max_index]
                return res
            else:
                logging.error('no predictions')
                break
        elif r.status_code == 400:
            error = response_data.get('error', '')
            if error == "failed to connect to all addresses":
                time.sleep(1)
            else:
                break
        else:
            logging.error(f'error from prediction service {service_url} {r.status_code} {r.text}')
            break