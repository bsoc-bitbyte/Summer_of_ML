# predictor/forms.py

from django import forms

class CodeforcesToCodechefForm(forms.Form):
    codeforces_rating = forms.IntegerField(label='Enter Codeforces Rating')

class CodechefToCodeforcesForm(forms.Form):
    codechef_rating = forms.IntegerField(label='Enter CodeChef Rating')
