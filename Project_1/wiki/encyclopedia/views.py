from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.files.storage import default_storage
from django.urls import reverse
from django.contrib import messages
import random

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# Entry page: /wiki/TITLE should take user to an entry with that TITLE
# Rework index page to have links to entries


def entry(request, name):
    if name not in util.list_entries():
        messages.error(request, 'Entry does not exist.')
        return HttpResponseRedirect(reverse('encyclopedia:index'))
    util.convert(name, 'encyclopedia/templates/encyclopedia/entry.html')
    return render(request, "encyclopedia/entry.html", {'name': name})

# New page: Enter markdown data in a textarea field with a save button at the bottom,
# check to make sure the entry does not already exist, then save to disk as a new markdown entry


def new_entry(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        if title in util.list_entries():
            messages.error(request, 'Entry already exists')
            return HttpResponseRedirect(reverse('encyclopedia:new'))
        f = default_storage.open(f'entries/{title}.md', 'w+')
        f.write(content)
        return HttpResponseRedirect(reverse('encyclopedia:entry', args=[title]))
    else:
        return render(request, 'encyclopedia/new_entry.html')

# Edit page that pulls up existing data and has a save button


def edit(request, name):
    f = default_storage.open(f'entries/{name}.md', 'r+')
    content = f.read()
    if request.method == 'POST':
        edited = request.POST['edited']
        f.seek(0)
        f.write(edited)
        f.truncate()
        return HttpResponseRedirect(reverse('encyclopedia:entry', args=[name]))
    elif request.method == 'GET':
        return render(request, 'encyclopedia/edit.html', {
            'name': name, 'content': content
        })

# Random page button


def random_entry(request):
    entries = util.list_entries()
    number = random.randint(0, len(entries))
    page = entries[(number - 1)]
    return HttpResponseRedirect(reverse('encyclopedia:entry', args=[page]))

# Search feature that takes into account partial strings by listing entries with that partial string


def search(request):
    q = request.GET['q']
    if q in util.list_entries():
        return HttpResponseRedirect(reverse('encyclopedia:entry', args=[q]))
    else:
        possibles = []
        for page in util.list_entries():
            if q in page:
                possibles.append(page)
            else:
                continue
        if possibles == []:
            messages.error(request, 'No entries match your search.')
            return HttpResponseRedirect(reverse('encyclopedia:index'))
        else:
            return render(request, 'encyclopedia/search.html', {
                'results': possibles
            })
