from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User

import datetime

from .models import Part, Panel, Project, Band
from .forms import PartEntryForm


def entry(request):
    # TODO: we should separate each part with its project

    project = get_object_or_404(Project, id=1)
    new_part = None
    parts = Part.objects.all()
    if request.method == 'POST':
        part_form = PartEntryForm(data=request.POST)
        if part_form.is_valid():
            #new_part = part_form.save(commit=False)
            new_part = part_form.save()
            # cd = part_form.cleaned_data
            #part_form = PartEntryForm()
            return HttpResponseRedirect('')
    else:
        part_form = PartEntryForm()
            #new_part.project = project
    return render(request, 'calculates/entry.html', {'parts': parts,
                                                     'project': project,
                                                     'new_part': new_part,
                                                     'part_form': part_form})
