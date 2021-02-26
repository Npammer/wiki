from django.http import HttpResponse
from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def show(request, title): 
    return render(request, "encyclopedia/show.html", {
        "content": util.get_entry(title),
        "title": title,
    })