from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from netCDF4 import Dataset
import os

def index(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']

        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        file_relative_path = fs.url(filename)
        dataset = Dataset(settings.BASE_DIR + file_relative_path)
        fs.delete(filename)

        print(dataset.variables.keys())
        return render(request, 'lab3/index.html', {
            'uploaded_file_url': file_relative_path
        })
    return render(request, 'lab3/index.html')
