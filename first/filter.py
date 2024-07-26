from django.db.models import QuerySet
from django.http import QueryDict
from rest_framework.exceptions import ValidationError

from first.models import CarModel
from first.serializers import CarSerializer


def car_filter(query: QueryDict) -> QuerySet:
    qs = CarModel.objects.all()

    for key, v in query.items():
        match key:
            case 'price_gt':
                qs = qs.filter(price__gt=v)
            case 'price_lt':
                qs = qs.filter(price__lt=v)
            case 'price_eq':
                qs = qs.filter(price=v)
            case 'price_gte':
                qs = qs.filter(price__gte=v)
            case 'price_lte':
                qs = qs.filter(price__lte=v)

            case 'year_eq':
                qs = qs.filter(year=v)
            case 'year_lte':
                qs = qs.filter(year__lte=v)
            case 'year_gte':
                qs = qs.filter(year__gte=v)
            case 'year_lt':
                qs = qs.filter(year__lt=v)
            case 'year_gt':
                qs = qs.filter(year__gt=v)

            case 'brand_start':
                qs = qs.filter(brand__istartswith=v)
            case 'brand_endswith':
                qs = qs.filter(brand__istartswith=v)
            case 'brand_contains':
                qs = qs.filter(brand__istartswith=v)

            case 'order':
                fields = CarSerializer.Meta.fields
                fields = [*fields, *[f'-{field}' for field in fields]]

                if v not in fields:
                    raise ValidationError({"details":f'Please choice order from {",".join(fields)}'})

                qs = qs.order_by(v)

            case _:
                raise ValidationError(f"Filter {key} not supported")
    return qs
