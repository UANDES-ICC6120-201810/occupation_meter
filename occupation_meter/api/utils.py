import requests
from io import open as iopen


def download_image(count_request):
    r = requests.get(
        url=count_request.get_endpoint()
    )
    tmp_filename = '/tmp/{bus_stop_congestion_id}_{source_filename}'.format(
        bus_stop_congestion_id=count_request.bus_stop_congestion_id,
        source_filename=count_request.source_filename)
    with iopen(tmp_filename, 'wb') as file:
        file.write(r.content)
