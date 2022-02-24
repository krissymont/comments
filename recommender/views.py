from re import A
from recommender.forms import SearchForm
from django.shortcuts import render
from django.http import Http404, JsonResponse
from .models import *
from .forms import *
from django.views.decorators.http import require_POST, require_GET
import random



def find_albums(artist, from_year = None, to_year = None):
    query = Musicdata.objects.filter(artists__contains = artist)
    if from_year is not None:
        query = query.filter(year__gte = from_year)
    if to_year is not None:
        query = query.filter(year__lte = to_year)
    return list(query.order_by('-popularity').values('id','name','year'))
    

@require_POST
def searchform_post(request):
    # create a form instance and populate it with data from the request:
    form = SearchForm(request.POST)
    # check whether it's valid:
    if form.is_valid():
        # process the data in form.cleaned_data as required
        from_year = None if form.cleaned_data['from_year'] == None else int(form.cleaned_data['from_year'])
        to_year = None if form.cleaned_data['to_year'] == None else int(form.cleaned_data['to_year'])
        albums = find_albums(
                form.cleaned_data['artist'],
                from_year,
                to_year
            )
        
        # Random 3 of top 10 popular albums
        answer = albums[:10]
        random.shuffle(answer)
        answer = list(answer)[:5] 
        return render(request, 'recommender/searchform.html', {'form': form, 'albums': answer })
    else:
        raise Http404('Something went wrong')


@require_GET
def searchform_get(request):
    form = SearchForm()
    return render(request, 'recommender/searchform.html', {'form': form})


def about(request):
	context = {'first_name': 'Krissy', 'last_name': 'Montalbano'}
	return render(request, 'about.html', context)

def home(request):
    return render(request, 'home.html', {})

def info(request, music_id):
    if request.method == 'POST':
        name = Musicdata.objects.get(pk=music_id)
        form = MusicForm(request.POST or None, instance=name)

    else:
        name = Musicdata.objects.get(pk=music_id)
        return render(request, 'info.html', {'name': name })

