import json
from data.models import PointData, PolygonData
from data.serializers import PointDataSerializer, PolygonDataSerializer
from rest_framework.views import APIView
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

RES = {
    'status': False,
    'msg': 'Invalid Request',
    'data': []
}

class PointDataAPI(APIView):
    def post(self, request):
        res = RES.copy()
        try:
            data = json.loads(request.body)
            serializer = PointDataSerializer(data=data)
            if not serializer.is_valid():
                res['data'] = serializer.errors
                res['msg'] = 'Validation Failed'
                return JsonResponse(res, status=400)
            
            point = serializer.save()
            res['status'] = True
            res['msg'] = 'Point data created successfully'
            res['data'] = {'id': point.id, 'name': point.name}
            return JsonResponse(res, status=201)
        except Exception as e:
            res['msg'] = str(e)
            return JsonResponse(res, status=500)

    def get(self, request):
        res = RES.copy()
        try:
            name = request.GET.get('name')
            if name:
                point = get_object_or_404(PointData, name=name)
                serializer = PointDataSerializer(point)
                res['data'] = serializer.data
            else:
                points = PointData.objects.all()
                serializer = PointDataSerializer(points, many=True)
                res['data'] = serializer.data
            
            res['status'] = True
            res['msg'] = 'Point data retrieved successfully'
            return JsonResponse(res, status=200)
        except Exception as e:
            res['msg'] = str(e)
            return JsonResponse(res, status=500)

    def patch(self, request):
        res = RES.copy()
        try:
            data = json.loads(request.body)
            point = get_object_or_404(PointData, id=data.get('id'))
            serializer = PointDataSerializer(point, data=data, partial=True)
            if not serializer.is_valid():
                res['data'] = serializer.errors
                res['msg'] = 'Validation Failed'
                return JsonResponse(res, status=400)
            
            updated_point = serializer.save()
            res['status'] = True
            res['msg'] = 'Point data updated successfully'
            res['data'] = {'id': updated_point.id, 'name': updated_point.name}
            return JsonResponse(res, status=200)
        except Exception as e:
            res['msg'] = str(e)
            return JsonResponse(res, status=500)


class PolygonDataAPI(APIView):
    def post(self, request):
        res = RES.copy()
        try:
            data = json.loads(request.body)
            serializer = PolygonDataSerializer(data=data)
            if not serializer.is_valid():
                res['data'] = serializer.errors
                res['msg'] = 'Validation Failed'
                return JsonResponse(res, status=400)
            
            polygon = serializer.save()
            res['status'] = True
            res['msg'] = 'Polygon data created successfully'
            res['data'] = {'id': polygon.id, 'name': polygon.name}
            return JsonResponse(res, status=201)
        except Exception as e:
            res['msg'] = str(e)
            return JsonResponse(res, status=500)

    def get(self, request):
        res = RES.copy()
        try:
            name = request.GET.get('name')
            if name:
                polygon = get_object_or_404(PolygonData, name=name)
                serializer = PolygonDataSerializer(polygon)
                res['data'] = serializer.data
            else:
                polygons = PolygonData.objects.all()
                serializer = PolygonDataSerializer(polygons, many=True)
                res['data'] = serializer.data
            
            res['status'] = True
            res['msg'] = 'Polygon data retrieved successfully'
            return JsonResponse(res, status=200)
        except Exception as e:
            res['msg'] = str(e)
            return JsonResponse(res, status=500)

    def patch(self, request):
        res = RES.copy()
        try:
            data = json.loads(request.body)
            polygon = get_object_or_404(PolygonData, id=data.get('id'))
            serializer = PolygonDataSerializer(polygon, data=data, partial=True)
            if not serializer.is_valid():
                res['data'] = serializer.errors
                res['msg'] = 'Validation Failed'
                return JsonResponse(res, status=400)
            
            updated_polygon = serializer.save()
            res['status'] = True
            res['msg'] = 'Polygon data updated successfully'
            res['data'] = {'id': updated_polygon.id, 'name': updated_polygon.name}
            return JsonResponse(res, status=200)
        except Exception as e:
            res['msg'] = str(e)
            return JsonResponse(res, status=500)
