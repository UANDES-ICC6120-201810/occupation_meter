import os
import requests
import shutil

from .models import CountRequest



def download_image(count_request):
    r = requests.get(
        url=count_request.get_endpoint()
    )
    if r.status_code == 200:
        with open('image.png', 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
    #TODO: send GET request for image download
    #     https://{bucket}.{endpoint}/{location}/filename}
    pass
