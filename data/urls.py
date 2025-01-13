from django.urls import path
from data.views import PointDataAPI, PolygonDataAPI

urlpatterns = [
    path('points/', PointDataAPI.as_view(), name='point_data'),
    path('polygons/', PolygonDataAPI.as_view(), name='polygon_data'),
]
