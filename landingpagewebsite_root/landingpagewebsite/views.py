from django.http import HttpResponse
from django.shortcuts import render


def first_page(request) -> HttpResponse:
    some_item = ['<h1>Wrong', 'value</h1>']
    text = 'New text'
    # return HttpResponse(f"""{'<br>'.join(some_item)}""")
    return render(request, './index.html', {
        'a': '<br>'.join(some_item),
        'text': text
    })
