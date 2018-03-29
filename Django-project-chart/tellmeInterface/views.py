# importing required packages
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import requests
from django.http import JsonResponse
from django.shortcuts import render


def search(dictionary, substr):
    result = []
    for key in dictionary:
        if substr in key:
            result.append(dictionary[key])
    return result
def searchKey(dictionary, substr):
    result = []
    for key in dictionary:
        if substr in key:
            result.append(key)
    return result
@csrf_exempt
def index(request):
    if request.method == 'POST':
        review = request.POST.get('review')
        r = requests.get('http://ec2-54-246-194-119.eu-west-1.compute.amazonaws.com:5000/report?review=' + review)
        json = r.json()
        polaritepositive=False;
        polaritenegative=False;
        if(json["Polarity"]=="positive"):
            polaritepositive = json["Polarity"]
        else:
            polaritenegative = json["Polarity"]
        key_feature_positive = searchKey(json["key_feature"],"positive")
        key_feature_negative = searchKey(json["key_feature"],"negative")
        sentence_positive = search(json["key_feature"],"positive")
        sentence_negative = search(json["key_feature"],"negative")
        therender = {"review": json[" Review"],
                     "polaritepositive":polaritepositive,
                     "polaritenegative":polaritenegative,
                     "Topic":json["Topic"],
                     "key_feature_positive":key_feature_positive,
                     "key_feature_negative":key_feature_negative,
                     "sentence_positive":sentence_positive,
                     "sentence_negative":sentence_negative,}
        return render(request, 'showdata.html',therender)
    else:
        template = loader.get_template('index.html')
        return HttpResponse(template.render())
