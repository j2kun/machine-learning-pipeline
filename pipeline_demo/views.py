from rest_framework.decorators import api_view

from pipeline_demo import settings
import pipeline_demo.models as models


@api_view(['GET', 'POST'])
def index(request):
    # return templated response
    pass
