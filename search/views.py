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

    return render(request, 'search/search.html', {
        'search_query': search_query,
        'search_results': search_results,
    })
