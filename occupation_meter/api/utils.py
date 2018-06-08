import os
import requests
import boto3

from .models import CountRequest



def download_image(count_request):
    r = requests.get(
        url='https://zapo-storage.nyc3.digitaloceanspaces.com/occupation_images/'
    )
    #TODO: send GET request for image download
    #     https://{bucket}.{endpoint}/{location}/filename}
    pass
