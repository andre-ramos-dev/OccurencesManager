from django.core.management import BaseCommand

from occurrences.models import Category

CATEGORIES_SET = (
    {
        'type': 'CONSTRUCTION',
        'description': 'Planned RoadWork Events'
    },
    {
        'type': 'SPECIAL_EVENT',
        'description': 'Especial Events (Concerts, Markets, etc)'
    },
    {
        'type': 'INCIDENT',
        'description': 'Car Accidents or Similar'
    },
    {
        'type': 'WEATHER_CONDITION',
        'description': 'Meteorologic events that affects the roads'
    },
    {
        'type': 'ROAD_CONDITION',
        'description': 'Roads State that affects those who drives on them (degraded pavement, holes, etc)'
    }
)


class Command(BaseCommand):
    def handle(self, *args, **options):
        lst_category_to_create = list()
        for category in CATEGORIES_SET:
            lst_category_to_create.append(Category(**category))
        Category.objects.bulk_create(lst_category_to_create)
        print('Categories Created with Success')