from django.shortcuts import render
from xword_data.forms import DrillForm
from xword_data.models import Clue
from random import choice

# Create your views here.

def xword_drill(request):
    """Generate a login form. Note that most processing for this view is in forms.py"""

    pks = Clue.objects.values_list('pk', flat=True)
    clue_id = choice(pks)
    clue = Clue.objects.get(pk=clue_id)
    form = DrillForm(request.GET)

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DrillForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DrillForm()

    return render(request, 'xword-drill.html', {'form': form, 'clue':clue})