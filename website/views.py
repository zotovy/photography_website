from django.shortcuts import render
from .models import Presets
from ._forms import MessageForm


def home_view(request):

    presets = Presets.objects.filter()
    contact_form = MessageForm(request.POST or None)

    if request.method == 'POST':
        if contact_form.is_valid():
            contact_form.save()
        else:
            print(contact_form.errors)

    context = {
        'presets': presets,
        'contact_form': contact_form,
    }
    return render(request, 'index.html', context)


def preset_view(request, slug):

    preset = Presets.objects.filter(slug=slug)[0]
    rating = range(int(preset.rating)//2)

    context = {
        'preset': preset,
        'rating': rating,
    }
    return render(request, 'work-single.html', context)
