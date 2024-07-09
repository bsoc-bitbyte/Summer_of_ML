

###DEPLOYMENT 
## run "https://chitra2445-ml-stream-ma-uzsnz2.streamlit.app/""




import streamlit as st
import numpy as np
import pandas as pd
df=pd.read_csv("final_cccf.csv")
data=df.dropna()
x=data["cc_rating"]
y=data["cf_rating"]
x_mean = np.mean(x) 
y_mean = np.mean(y)

n = len(x)

num = 0
den = 0
for idx in x.index:
    num += (x[idx] - x_mean) * (y[idx] - y_mean)
    den += (x[idx] - x_mean) ** 2

b1 = num / den
b0 = y_mean - (b1*x_mean)

print("Calculated coefficients are:")
print("Slope is : ",b1,"and ","constant is",b0)

y_pred = x*b1 + b0 

def predict_codeforces_rating(codechef_rating):
    codeforces_rating = (codechef_rating *b1) + b0
    return codeforces_rating

def predict_codechef_rating(codeforces_rating):
    codechef_rating = (codeforces_rating -b0 )/ b1
    return codechef_rating



st.title("Rating Predictor")
st.markdown("""
    <div style='background-color: white;color: black;'>
        <h3 style='text-align: center;'>Choose Your CP Platform</h3>
    </div>
""", unsafe_allow_html=True)


option = st.sidebar.selectbox("Select an option", ["CodeChef Rating", "CodeForces Rating"])

if option == "CodeChef Rating":
    codeforces_rating = st.number_input("Enter your CodeForces rating", min_value=0, step=1)
    if st.button("Predict"):
        predicted_codechef_rating = predict_codechef_rating(codeforces_rating)
        st.write(f"Your predicted CodeChef rating is: {predicted_codechef_rating:.0f}")

elif option == "CodeForces Rating":
    codechef_rating = st.number_input("Enter your CodeChef rating", min_value=0, step=1)
    if st.button("Predict"):
        predicted_codeforces_rating = predict_codeforces_rating(codechef_rating)
        st.write(f"Your predicted CodeForces rating is: {predicted_codeforces_rating:.0f}")


st.markdown("""
    <div style='background-color: black; color: white; text-align: center;'>
        <p>Made by Chitra</p>
    </div>
""", unsafe_allow_html=True)

