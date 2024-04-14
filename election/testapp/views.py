from django.shortcuts import render

# Create your views here.

from .models import VoterModel
from .forms import VoterForm
from django.db.models import Q


def Voter(request):
    if request.method=='POST':
        form=VoterForm(request.POST)
        if form.is_valid():
            search_vote=form.cleaned_data['search_vote']

            result=VoterModel.objects.filter(
                Q(epic__icontains=search_vote) |
                Q(phone__icontains=search_vote)|
                Q(name__icontains=search_vote) |
                Q(addr__icontains=search_vote)
            )
            return render(request,'testapp/vote_result.html',{'result':result,'form':form})
    else:
        form=VoterForm()
    return render(request,'testapp/vote_find.html',{'form':form})

