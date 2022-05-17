import random
from django.shortcuts import render

from .forms import PasswordGeneratorForm

def home(request):
    if request.method == 'POST':
        form = PasswordGeneratorForm(request.POST)
        if form.is_valid():
            characters = list('abcdefghijklmnopqrstuvwxyz')
            generated_password = ''

            if form.cleaned_data['uppercase']:
                characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

            if form.cleaned_data['numbers']:
                characters.extend(list('0123456789'))

            if form.cleaned_data['symbols']:
                characters.extend(list('@#$%'))

            for _ in range(form.cleaned_data['length']):
                generated_password += random.choice(characters)

            return render(request, 'generator/home.html', {'form': form, 'generated_password': generated_password})
    else:
        form = PasswordGeneratorForm(initial={'length': 8})
    return render(request, 'generator/home.html', {'form': form})
