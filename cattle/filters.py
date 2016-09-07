from django_filters import ChoiceFilter, FilterSet

from .models import Cattle


PERCENTILES = [1, 2, 3, 4, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90]

ANGUS_PERCENTILES = {
    'scrotal_circumference': [2.2, 1.99, 1.87, 1.8, 1.73, 1.5, 1.36, 1.24, 1.14,
                              1.05, 0.97, 0.9, 0.83, 0.76, 0.61, 0.46, 0.28, 0.28],
    'birth_weight': [-3.6, -3, -2.5, -2.3, -2, -1.2, -0.7, -0.4, -0.1,
                     0.2, 0.5, 0.7, 0.9, 1.2, 1.6, 2.1, 2.6, 3.4],
    'weaning_weight': [75, 71, 69, 67, 66, 62, 59, 57, 56,
                       54, 52, 51, 50, 49, 46, 43, 39, 33],
    'yearling_weight': [128, 123, 120, 117, 115, 109, 105, 101,
                        98, 96, 93, 91, 89, 87, 82, 77, 71, 61],
    'residual_average_daily_gain': [0.35, 0.33, 0.32, 0.31, 0.3, 0.28, 0.27, 0.25, 0.24,
                                    0.24, 0.23, 0.22, 0.21, 0.21, 0.19, 0.18, 0.16, 0.13],
    'heifer_pregnancy': [26.1, 24.5, 23.4, 22.6, 21.9, 19.4, 17.8, 16.4, 15.2,
                         14.1, 13.1, 12.2, 11.2, 10.2, 8.3, 6.3, 3.9, 0.1],
    'calving_ease_maternal': [16, 15, 15, 14, 14, 13, 12, 11,
                              11, 10, 10, 10, 9, 9, 8, 7, 6, 4],
    'maternal_milk': [36, 35, 34, 33, 32, 30, 29, 28, 27,
                      26, 26, 25, 24, 24, 22, 21, 19, 15],
    'mature_weight': [95, 86, 81, 77, 73, 62, 55, 49, 44,
                      40, 36, 33, 29, 25, 18, 10, 0, -15],
    'mature_height': [1.1, 1, 0.9, 0.9, 0.8, 0.7, 0.6, 0.6, 0.5,
                      0.5, 0.4, 0.4, 0.4, 0.3, 0.2, 0.1, 0, -0.1],
    'cow_energy_value': [41.82, 33.02, 28.46, 24.79, 22.29, 14.47, 10.09, 7.19, 4.79,
                         2.85, 1.14, -0.49, -2.04, -3.49, -6.3, -9.31, -12.78, -17.56],
    'carcass_weight': [67, 63, 61, 59, 57, 50, 46, 43, 41,
                       38, 36, 34, 32, 30, 27, 23, 18, 11],
    'marbling': [1.22, 1.11, 1.05, 1.01, 0.97, 0.84, 0.76, 0.71, 0.66,
                 0.62, 0.58, 0.55, 0.51, 0.48, 0.42, 0.35, 0.27, 0.16],
    'ribeye_area': [1.19, 1.1, 1.05, 1, 0.96, 0.84, 0.76, 0.7, 0.65,
                    0.6, 0.55, 0.51, 0.47, 0.43, 0.35, 0.26, 0.16, 0.03],
    'fat_thickness': [-0.065, -0.057, -0.051, -0.046, -0.042, -0.031,
                      -0.023, -0.017, -0.011, -0.006, -0.002, 0.003,
                      0.008, 0.013, 0.023, 0.034, 0.048, 0.067]
}


def get_percentile_range_queries(attr_percentiles, attr_name):
    range_queries = []
    if attr_percentiles[0] > 0:
        range_queries.append({'{}__gt'.format(attr_name): attr_percentiles[0]})
        for i, num in enumerate(attr_percentiles[:-2]):
            query = {'{}__gt'.format(attr_name): attr_percentiles[i + 1],
                     '{}__lte'.format(attr_name): num}
            range_queries.append(query)
        range_queries.append({'{}__lte'.format(attr_name): attr_percentiles[-2]})
    else:
        range_queries.append({'{}__lt'.format(attr_name): attr_percentiles[1]})
        for i, num in enumerate(attr_percentiles[2:]):
            query = {'{}__gte'.format(attr_name): attr_percentiles[i + 1],
                     '{}__lt'.format(attr_name): num}
            range_queries.append(query)
        range_queries.append({'{}__gte'.format(attr_name): attr_percentiles[-1]})
    return range_queries


def get_attr_query_map(attr_percentiles, attr_name):
    range_queries = get_percentile_range_queries(attr_percentiles, attr_name)
    query_dict = {'{}'.format(percent): query for percent, query in zip(PERCENTILES,
                                                                        range_queries)}
    return query_dict


def get_filter_function(percentile_queries):
    def filter_attr(queryset, value):
        query = percentile_queries.get(value, {})
        # TODO: Prefetch watchlist for user
        return queryset.filter(**query).select_related('producer').prefetch_related('photos')
    return filter_attr

PERCENTILE_CHOICES = [('', '-')] + [(percent, '{}%'.format(percent)) for percent in PERCENTILES]

SC_PERCENTILE_QUERY_MAP = get_attr_query_map(ANGUS_PERCENTILES['scrotal_circumference'],
                                             'scrotal_circumference')

BIRTH_WEIGHT_QUERY_MAP = get_attr_query_map(ANGUS_PERCENTILES['birth_weight'],
                                            'birth_weight')

WEANING_WEIGHT_QUERY_MAP = get_attr_query_map(ANGUS_PERCENTILES['weaning_weight'],
                                              'weaning_weight')

YEARLING_WEIGHT_QUERY_MAP = get_attr_query_map(ANGUS_PERCENTILES['yearling_weight'],
                                               'yearling_weight')

RADG_QUERY_MAP = get_attr_query_map(ANGUS_PERCENTILES['residual_average_daily_gain'],
                                    'residual_average_daily_gain')

HEIFER_PREGNANCY_QUERY_MAP = get_attr_query_map(ANGUS_PERCENTILES['heifer_pregnancy'],
                                                'heifer_pregnancy')

CEM_QUERY_MAP = get_attr_query_map(ANGUS_PERCENTILES['calving_ease_maternal'],
                                   'calving_ease_maternal')

MATERNAL_MILK_QUERY_MAP = get_attr_query_map(ANGUS_PERCENTILES['maternal_milk'],
                                             'maternal_milk')

MATURE_WEIGHT_QUERY_MAP = get_attr_query_map(ANGUS_PERCENTILES['mature_weight'],
                                             'mature_weight')

MATURE_HEIGHT_QUERY_MAP = get_attr_query_map(ANGUS_PERCENTILES['mature_height'],
                                             'mature_height')

COW_ENERGY_VALUE_QUERY_MAP = get_attr_query_map(ANGUS_PERCENTILES['cow_energy_value'],
                                                'cow_energy_value')

CARCASS_WEIGHT_QUERY_MAP = get_attr_query_map(ANGUS_PERCENTILES['carcass_weight'],
                                              'carcass_weight')

MARBLING_QUERY_MAP = get_attr_query_map(ANGUS_PERCENTILES['marbling'],
                                        'marbling')

RIBEYE_AREA_QUERY_MAP = get_attr_query_map(ANGUS_PERCENTILES['ribeye_area'],
                                           'ribeye_area')

FAT_THICKNESS_QUERY_MAP = get_attr_query_map(ANGUS_PERCENTILES['fat_thickness'],
                                             'fat_thickness')


class CattleFilter(FilterSet):
    scrotal_circumference = ChoiceFilter(choices=PERCENTILE_CHOICES,
                                         action=get_filter_function(SC_PERCENTILE_QUERY_MAP))
    birth_weight = ChoiceFilter(choices=PERCENTILE_CHOICES,
                                action=get_filter_function(BIRTH_WEIGHT_QUERY_MAP))
    weaning_weight = ChoiceFilter(choices=PERCENTILE_CHOICES,
                                  action=get_filter_function(WEANING_WEIGHT_QUERY_MAP))
    yearling_weight = ChoiceFilter(choices=PERCENTILE_CHOICES,
                                   action=get_filter_function(YEARLING_WEIGHT_QUERY_MAP))
    residual_average_daily_gain = ChoiceFilter(choices=PERCENTILE_CHOICES,
                                               action=get_filter_function(RADG_QUERY_MAP))
    heifer_pregnancy = ChoiceFilter(choices=PERCENTILE_CHOICES,
                                    action=get_filter_function(HEIFER_PREGNANCY_QUERY_MAP))
    calving_ease_maternal = ChoiceFilter(choices=PERCENTILE_CHOICES,
                                    action=get_filter_function(CEM_QUERY_MAP))
    maternal_milk = ChoiceFilter(choices=PERCENTILE_CHOICES,
                                 action=get_filter_function(MATERNAL_MILK_QUERY_MAP))
    mature_weight = ChoiceFilter(choices=PERCENTILE_CHOICES,
                                 action=get_filter_function(MATURE_WEIGHT_QUERY_MAP))
    mature_height = ChoiceFilter(choices=PERCENTILE_CHOICES,
                                 action=get_filter_function(MATURE_HEIGHT_QUERY_MAP))
    cow_energy_value = ChoiceFilter(choices=PERCENTILE_CHOICES,
                                    action=get_filter_function(COW_ENERGY_VALUE_QUERY_MAP))
    carcass_weight = ChoiceFilter(choices=PERCENTILE_CHOICES,
                                  action=get_filter_function(CARCASS_WEIGHT_QUERY_MAP))
    marbling = ChoiceFilter(choices=PERCENTILE_CHOICES,
                            action=get_filter_function(MARBLING_QUERY_MAP))
    ribeye_area = ChoiceFilter(choices=PERCENTILE_CHOICES,
                               action=get_filter_function(RIBEYE_AREA_QUERY_MAP))
    fat_thickness = ChoiceFilter(choices=PERCENTILE_CHOICES,
                                 action=get_filter_function(FAT_THICKNESS_QUERY_MAP))

    class Meta:
        model = Cattle
        fields = ['scrotal_circumference',
                  'birth_weight',
                  'weaning_weight',
                  'yearling_weight',
                  'residual_average_daily_gain',
                  'heifer_pregnancy',
                  'cow_energy_value',
                  'maternal_milk',
                  'mature_weight',
                  'mature_height',
                  'cow_energy_value',
                  'carcass_weight',
                  'marbling',
                  'ribeye_area',
                  'fat_thickness']
