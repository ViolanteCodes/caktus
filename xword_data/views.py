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

    if form.is_valid():
        if form.cleaned_data.answer.upper() == clue.entry.entry_text:
            return redirect('user-landing', user_identifier = user_identifier)
        else:
            return render (request, 'xword-drill.html', {'form':form})
    # if no valid user_identifier in GET, just display the form
    else: 
        return render (request, 'xword-drill.html', {'form': form})
    # If everything else fails, just render the form.
    return render (request, 'xword-drill.html', {'form':form})