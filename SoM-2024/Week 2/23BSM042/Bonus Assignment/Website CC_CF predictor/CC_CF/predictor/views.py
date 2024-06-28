# predictor/views.py

from django.shortcuts import render
from .forms import CodeforcesToCodechefForm, CodechefToCodeforcesForm
from .ml_model.model import predict_codechef_rating, predict_codeforces_rating

def home(request):
    return render(request, 'predictor/home.html')

def predict_codechef_from_codeforces(request):
    if request.method == 'POST':
        form = CodeforcesToCodechefForm(request.POST)
        if form.is_valid():
            codeforces_rating = form.cleaned_data['codeforces_rating']
            predicted_rating = predict_codechef_rating(codeforces_rating)
            return render(request, 'predictor/result.html', {'predicted_rating': predicted_rating})
    else:
        form = CodeforcesToCodechefForm()
    return render(request, 'predictor/predict_form.html', {'form': form})

def predict_codeforces_from_codechef(request):
    if request.method == 'POST':
        form = CodechefToCodeforcesForm(request.POST)
        if form.is_valid():
            codechef_rating = form.cleaned_data['codechef_rating']
            predicted_rating = predict_codeforces_rating(codechef_rating)
            return render(request, 'predictor/result.html', {'predicted_rating': predicted_rating})
    else:
        form = CodechefToCodeforcesForm()
    return render(request, 'predictor/predict_form.html', {'form': form})
