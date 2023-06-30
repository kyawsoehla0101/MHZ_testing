# index.py

import algoliasearch_django as algoliasearch

from .models import Coffee

algoliasearch.register(Coffee)


# index.py

# from algoliasearch_django import AlgoliaIndex
# from algoliasearch_django.decorators import register

# from .models import YourModel

# @register(YourModel)
# class YourModelIndex(AlgoliaIndex):
#     fields = ('name', 'date')
#     geo_field = 'location'
#     settings = {'searchableAttributes': ['name']}
#     index_name = 'my_index'

