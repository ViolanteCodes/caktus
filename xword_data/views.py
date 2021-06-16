from django.shortcuts import render, redirect
from xword_data.forms import DrillForm
from xword_data.models import Clue
from random import choice

# Create your views here.

def xword_drill(request, clue_id=''):
    """Drill View"""
    # call get_clue function
    clue = get_clue(clue_id)

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DrillForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            if form.cleaned_data['answer'].upper() == clue.entry.entry_text:
                return redirect('xword-answer', clue.pk)
            else:
                message = "Sorry, that was not correct."
                return redirect('xword-drill', clue_id=clue.pk)
    else:
        form=DrillForm()
    return render(request, 'xword-drill.html', {'form': form, 'clue':clue})

def get_clue(clue_id):
    """Checks if there is a clue_id, if not, gets a random clue"""
    if clue_id == '':
        pks = Clue.objects.values_list('pk', flat=True)
        clue_id = choice(pks)
    clue=Clue.objects.get(pk=clue_id)
    return clue

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