import os

def run():
    clear_db()


def clear_db():
    models = [Temperature, MeasureDate, Longitude, Latitude]
    for model in models:
        model.objects.all().delete()

if __name__ == '__main__':
    print('\n' + ('=' * 80) + '\n')
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'data_vis_practice.settings')
    django.setup()
    from lab3.models import Temperature, MeasureDate, Longitude, Latitude

    run()
