from django_filters import FilterSet, DateTimeFilter, CharFilter, ModelChoiceFilter
from .models import Post, Message, User
from django.forms import DateInput


# Фильтрация записей по параметрам
class PostFilter(FilterSet):

    search_heading = CharFilter(
        field_name='heading',
        label='Заголовок',
        lookup_expr='icontains',
    )

    search_author = ModelChoiceFilter(
        field_name='author__user',
        queryset=User.objects.all(),
        label='Автор',
        empty_label='Все авторы',
    )

    search_time = DateTimeFilter(
        field_name='create_at',
        label='Дата',
        lookup_expr='date__gte',
        widget=DateInput(attrs={'type': 'date'})
    )


class MessageFilter(FilterSet):

    search_post = CharFilter(
        field_name='on_post__heading',
        label='Название поста',
        lookup_expr='iconteins',
    )

    search_sender = CharFilter(
        field_name='User__username',
        label='Отправитель'
    )