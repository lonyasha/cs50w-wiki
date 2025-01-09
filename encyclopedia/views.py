from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
import markdown2
from random import choice

from . import util


class NewEntryForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(widget=forms.Textarea(), label="Content")


class EditEntryForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(), label="Content")


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def get_entry(request, title):
    markdown_content = util.get_entry(title)
    if markdown_content is None:
        return HttpResponse("<h1>Page does not exist.</h1>", status=404)
    entry_content = markdown2.markdown(markdown_content)
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": entry_content
    })


def search_entry(request):
    query = request.GET.get('q', '').lower()
    entries = util.list_entries()
    for entry in entries:
        if query == entry.lower():
            return redirect('get_entry', title=entry)
    search_results = [entry for entry in entries if query in entry.lower()]
    return render(request, "encyclopedia/search_results.html", {
        "search_results": search_results,
        "query": query
    })


def create_entry(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if util.get_entry(title) is not None:
                return HttpResponse("<h1>Page with this title already exists.</h1>", status=400)
            else:
                util.save_entry(title, content)
                return redirect('get_entry', title=title)
    return render(request, "encyclopedia/create_entry.html", {"form": NewEntryForm()})


def edit_entry(request, title):
    if request.method == "POST":
        form = EditEntryForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return redirect("get_entry", title=title)
    else:
        content = util.get_entry(title)
        if content is None:
            return HttpResponse("<h1>The requested page was not found.</h1>", status=404)
        form = EditEntryForm(initial={'content': content})
        return render(request, "encyclopedia/edit_entry.html", {
            "form": form,
            "title": title
        })


def random_entry(request):
    entries = util.list_entries()
    random_title = choice(entries)
    markdown_content = util.get_entry(random_title)
    if markdown_content is None:
        return HttpResponse("<h1>Page does not exist.</h1>", status=404)
    entry_content = markdown2.markdown(markdown_content)
    return render(request, "encyclopedia/entry.html", {
        "title": random_title,
        "content": entry_content
    })
