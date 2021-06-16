from django.shortcuts import render, redirect
from xword_data.forms import DrillForm
from xword_data.models import Clue
from random import choice

# Create your views here.

def xword_drill(request, clue_id=None):
    """Drill View"""
    # call get_clue function
    clue = get_clue(clue_id)
    form = DrillForm()

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DrillForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            if form.cleaned_data['answer'].upper() == clue.entry.entry_text:
                return redirect('xword-answer', clue.id)
            else:
                message = "Sorry, that was not correct."
                return render(request, 'xword-drill.html', {
                    'form':form, 
                    'clue':clue, 
                    'clue_id': clue.id, 
                    'message':'Sorry, that is not correct.'})
    else:
        form = DrillForm()
    return render(request, 'xword-drill.html', {'form': form, 'clue':clue, "clue_id":clue.id})

def get_clue(clue_id):
    """Checks if there is a clue_id, if not, gets a random clue"""
    if not clue_id:
        ids = Clue.objects.values_list('id', flat=True)
        clue_id = int(choice(ids))
    clue = Clue.objects.get(id=clue_id)
    return clue

def xword_answer(request, clue_id):
    """View for clue answers"""
    clue_dict = check_only(clue_id)
    return render(request, 'xword-answer.html', {'clue':clue_dict})

def check_only(clue_id):
    """Checks to see if clue is unique"""
    clue = Clue.objects.get(id=clue_id)
    clue_text = clue.clue_text
    clue_list = Clue.objects.filter(clue_text=clue_text)
    clue_dict = {
        'clue': clue,
        'clue_list': clue_list,
        }
    return clue_dict