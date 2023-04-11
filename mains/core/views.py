from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins, viewsets
from rest_framework.filters import SearchFilter

# Create your views here.
class ModelPaginationViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter, DjangoFilterBackend]

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)
        if self.pagination_class is not None:
            page_size = request.query_params.get('page_size', 100)
            self.pagination_class.page_size = page_size

    def get_serializer_context(self):
        context = super().get_serializer_context()
        depth = 0
        try:
            depth = int(self.request.query_params.get('depth', 1))
        except ValueError:
            pass

        context['depth'] = depth
        return context