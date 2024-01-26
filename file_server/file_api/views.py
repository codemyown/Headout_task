from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import File
from .serializers import FileSerializer

@api_view(['GET'])
def get_file_content(request):
    file_name = request.query_params.get('n')
    line_number = request.query_params.get('m')

    try:
        file_obj = File.objects.get(name=file_name)
    except File.DoesNotExist:
        return Response({'error': 'File not found'}, status=404)

    if line_number:
        try:
            content_line = file_obj.content.split('\n')[int(line_number) - 1]
        except IndexError:
            return Response({'error': 'Line number out of range'}, status=400)
        return Response({'content': content_line})

    serializer = FileSerializer(file_obj)
    return Response(serializer.data)
