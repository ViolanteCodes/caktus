from django.shortcuts import render, redirect
from xword_data.forms import DrillForm
from xword_data.models import Clue
from random import choice

# Create your views here.

def xword_drill(request, clue_id=None, message=None):
    """Generate a login form. Note that most processing for this view is in forms.py"""
    if clue_id:
        clue = Clue.objects.get(pk=clue_id)
        message="I'm sorry, that clue wasn't correct. Try again."
    else:
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
            if form.cleaned_data['answer'] == clue.entry.entry_text:
                return HttpResponseRedirect('/thanks/')
            else:
                return redirect('xword-drill-clue', clue_id=clue_id)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = DrillForm()
    return render(request, 'xword-drill.html', {'form': form, 'clue':clue, 'message':message})

def xword_answer(request, clue_id):
    """View for clue answers"""
    clue_dict = check_only(clue_id)
    return render(request, 'xword-answer.html', {'clue':clue_dict})

def check_only(clue_id):
    """Checks to see if clue is unique"""
    clue = Clue.objects.get(pk=clue_id)
    clue_text = clue.clue_text
    clue_list = Clue.objects.filter(clue_text=clue_text)
    clue_dict = {
        'clue': clue,
        'clue_list': clue_list,
        }
    return clue_dict