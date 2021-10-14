from rest_framework.generics import ListAPIView
from sample.settings import ALLOWED_HOSTS
from .serializers import AuthorSerializer
from ..models import Author
from ..service import parse_search_phrase

class AuthorsListView(ListAPIView):
    
    serializer_class = AuthorSerializer
    http_method_names = ['get']	 # allow only get
    allowed_fields = ['name','age']
    def get_queryset(self):
        # get keyword query and pass it to querysite
        query = self.request.query_params.get('query',None)
        print(query)
        if query:
            #TODO catch error here with appropiate response message if bad query
            q = parse_search_phrase(self.allowed_fields, query)
            q
            print(q)
            queryset = Author.objects.filter(q)
            return queryset
        else:
            queryset = Author.objects.none()
            return queryset

