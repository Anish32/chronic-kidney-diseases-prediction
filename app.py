import streamlit as st
import pandas as pd
import pickle

with open('ckd_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Chronic Kidney Disease Prediction")

age = st.number_input("Age")
bp = st.number_input("Blood Pressure")
sg = st.number_input("Specific Gravity")
al = st.number_input("Albumin")
su = st.number_input("Sugar")
rbc = st.selectbox("Red Blood Cells", [0, 1])  
pc = st.selectbox("Pus Cell", [0, 1])  
pcc = st.selectbox("Pus Cell Clumps", [0, 1]) 
ba = st.selectbox("Bacteria", [0, 1]) 
bgr = st.number_input("Blood Glucose Random")
bu = st.number_input("Blood Urea")
sc = st.number_input("Serum Creatinine")
sod = st.number_input("Sodium")
pot = st.number_input("Potassium")
hemo = st.number_input("Hemoglobin")
pcv = st.number_input("Packed Cell Volume")
wc = st.number_input("White Blood Cell Count")
rc = st.number_input("Red Blood Cell Count")
htn = st.selectbox("Hypertension", [0, 1]) 
dm = st.selectbox("Diabetes Mellitus", [0, 1])  
cad = st.selectbox("Coronary Artery Disease", [0, 1])  
appet = st.selectbox("Appetite", [0, 1])  
pe = st.selectbox("Pedal Edema", [0, 1])  
ane = st.selectbox("Anemia", [0, 1]) 



if st.button("Predict"):

    input_data = pd.DataFrame([[age, bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc, htn, dm, cad, appet, pe, ane]],
                             columns=['age', 'blood_pressure', 'specific_gravity', 'albumin', 'sugar', 'red_blood_cells', 'pus_cell',
                                      'pus_cell_clumps', 'bacteria', 'blood_glucose_random', 'blood_urea', 'serum_creatinine',
                                      'sodium', 'potassium', 'hemoglobin', 'packed_cell_volume', 'white_blood_cell_count',
                                      'red_blood_cell_count', 'hypertension', 'diabetes_mellitus', 'coronary_artery_disease',
                                      'appetite', 'pedal_edema', 'anemia'])


    prediction = model.predict(input_data)

    if prediction[0] == 0:
        st.success("The patient is predicted to not have Chronic Kidney Disease.")
    else:
        st.error("The patient is predicted to have Chronic Kidney Disease.")
