from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from wagtail.core.models import Page
from wagtail.search.models import Query


def search(request):
    search_query = request.GET.get('query', None)

    # Search
    if search_query:
        search_results = Page.objects.live().search(search_query)
        query = Query.get(search_query)

        # Record hit
        query.add_hit()
    else:
        search_results = Page.objects.none()

    paginator = Paginator(search_results, 10)
    try:
        pagination = paginator.page(search_query)
    except PageNotAnInteger:
        pagination = paginator.page(1)
    except EmptyPage:
        pagination = paginator.page(paginator.num_pages)

    return render(request, 'search/search.html', {
        'search_query': search_query,
        'search_results': search_results,
        'pagination': pagination,
    })
