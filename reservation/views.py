from django.shortcuts import render
from reservation.models import Instrument, Instru
from reservation.bing_search import run_query
# Create your views here.

def index(request):
    #anouncement = Anouncement.objects.order_by('pub_date')[0]
    instrument = Instrument.objects.all()[:3]
    context_dict = {'instrument': instrument}
    instru = Instru.objects.all()[:5]
    context_dict['instru'] =  instru
    
    return render(request, 'reservation/index.html', context_dict)

def search(request):
    result_list = []
    if request.method == 'POST':
        query = request.POST['query'].strip()

        if query:
            # Run our Bing function to get the results list!
            request_list = run_query(query)

    return render(request, 'reservation/search.html', {'result_list': result_list})
