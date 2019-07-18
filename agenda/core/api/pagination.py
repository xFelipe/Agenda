from rest_framework import pagination


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10 #  Default
    page_size_query_param = 'size' #  Parameter name


