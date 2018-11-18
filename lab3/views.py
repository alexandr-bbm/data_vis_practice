from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from netCDF4 import Dataset
from datetime import date, timedelta
import time

from lab3.models import Latitude, Longitude, Temperature, MeasureDate


def index(request):
    if request.method == 'POST' and request.FILES['myfile']:
        uploaded_file = request.FILES['myfile']

        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_relative_path = fs.url(filename)
        dataset = Dataset(settings.BASE_DIR + file_relative_path)
        fs.delete(filename)

        times = dataset.variables['time'][:]
        lats = dataset.variables['latitude'][:]
        longs = dataset.variables['longitude'][:]
        t2m = dataset.variables['t2m'][:]

        measure_date_objects = []
        lat_objects = []
        lon_objects = []
        temp_objects = []

        for time_item in times:
            parsed_date = parse_date(time_item)
            item = MeasureDate.objects.create(value=parsed_date)
            measure_date_objects.append(item)

        for lat in lats:
            item = Latitude.objects.create(value=lat)
            lat_objects.append(item)

        for lon in longs:
            item = Longitude.objects.create(value=lon)
            lon_objects.append(item)

        start = time.time()
        for date_key, lats_arr in enumerate(t2m):
            if len(temp_objects) > 0:
                Temperature.objects.bulk_create(temp_objects)
                temp_objects = []
            mins_passed = (time.time() - start) // 60
            print('date_key iteration {date_key}, mins={mins}'.format(date_key=date_key, mins=mins_passed))
            for lat_key, longs_arr in enumerate(lats_arr):
                for long_key, temp in enumerate(longs_arr):
                    temp_objects.append(Temperature(
                        value=temp,
                        date=measure_date_objects[date_key],
                        lat=lat_objects[lat_key],
                        lon=lon_objects[long_key],
                    ))

        if len(temp_objects) > 0:
            Temperature.objects.bulk_create(temp_objects)

        return render(request, 'lab3/index.html', {
            'uploaded_file_url': file_relative_path
        })
    return render(request, 'lab3/index.html')

# hours since 1900-01-01 00:00:0.0
def parse_date(hours):
    days = hours.item() // 24 # convert numpy int to native int
    delta = timedelta(days)
    return date(1900, 1, 1) + delta
