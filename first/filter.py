from django.db.models import QuerySet
from django.http import QueryDict
from rest_framework.exceptions import ValidationError

from first.models import CarModel


def car_filter(query: QueryDict) -> QuerySet:
    qs = CarModel.objects.all()

    for key, v in query.items():
        match key:
            case 'price_gt':
                qs = qs.filter(price__gt=v)
            case 'price_lt':
                qs = qs.filter(price__lt=v)
            case _:
                raise ValidationError(f"Filter {key} not supported")
    return qs
