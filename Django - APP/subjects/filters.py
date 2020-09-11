import django_filters
from django_filters import CharFilter
from subjects.models import Subject

class OrderFilter(django_filters.FilterSet):
    bookName = CharFilter(field_name='bookName',lookup_expr="icontains")
    class Meta:
        model = Subject  # name of the model has to be filtered
        exclude = ['bookDescription', 'bookImage', 'bookPro']