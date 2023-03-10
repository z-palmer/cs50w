from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# Entry page: /wiki/TITLE should take user to an entry with that TITLE
# Rework index page to have links to entries


def entry(request, name):
    util.convert(name, 'encyclopedia/templates/encyclopedia/entry.html')
    return render(request, "encyclopedia/entry.html")

# Search feature that takes into account partial strings by listing entries with that partial string

# New page: Enter markdown data in a textarea field with a save button at the bottom,
# check to make sure the entry does not already exist, then save to disk as a new markdown entry


def new_entry(request):
    return render(request, 'encyclopedia/new_entry.html')

# Edit page that pulls up existing data and has a save button

# Random page button

# Markdown to HTML conversion, making sure to support headings, bold text,
# unordered lists, links, and paragraphs. Look into the re module
