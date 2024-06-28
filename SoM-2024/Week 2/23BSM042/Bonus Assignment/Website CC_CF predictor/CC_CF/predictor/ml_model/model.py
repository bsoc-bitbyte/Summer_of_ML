# predictor/ml_model/model.py
B = 1.0298705017160635e-16
M = 0.6245876122997068
def predict_codechef_rating(codeforces_rating):
    
    return round((codeforces_rating * M) +B )

def predict_codeforces_rating(codechef_rating):
   
    return round((codechef_rating -B)/M ) 
