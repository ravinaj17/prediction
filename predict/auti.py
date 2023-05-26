import pickle
import streamlit as st
from streamlit_option_menu import option_menu
autism_model = pickle.load(open('autism_model.sav', "rb"))
parks_model = pickle.load(open('parks_model.sav', "rb"))

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                                    
                          ['Autism Prediction',
                           'Parkinsons Prediction'],
                          icons=['activity','person'],

                          default_index=0,
                          orientation="horizontal",
                          styles={
                            "container":{"background-color":"mistyrose",},
                            "nav-link":{
                                "--hover-color":"#eee"},
                                "nav-link-selected":{"background-color":"green"},
                          }
                          )

# Autism Prediction Page
if (selected == "Autism Prediction"):
    
    # page title
    st.title("Autism's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        A1 = st.text_input('A1')
        
    with col2:
        A2 = st.text_input('A2')
        
    with col3:
        A3 = st.text_input('A3')
        
    with col4:
        A4= st.text_input('A4')
        
    with col5:
        A5 = st.text_input('A5')
        
    with col1:
        A6 = st.text_input('A6')
        
    with col2:
        A7 = st.text_input('A7')
        
    with col3:
        A8= st.text_input('A8')
        
    with col4:
        A9 = st.text_input('A9')
        
    with col5:
        A10 = st.text_input('A10')
        
    with col1:
        Age = st.text_input('Age_Mons')
        
    with col2:
        Qchat = st.text_input('Qchat-10-Score')
        
    with col3:
        Sex=st.text_input('Sex')
        
    with col4:
        Ethnicity = st.text_input('Ethnicity')
        
    with col5:
        Jaundice = st.text_input('Jaundice')
        
    with col1:
        Family_mem = st.text_input('Family_mem_with_ASD')
    
    
    # code for Prediction
    autism_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Autism Test Result"):
        autisms_prediction = autism_model.predict([[A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,Age,Qchat,Sex,Ethnicity,Jaundice,Family_mem]])                          
        
        if (autisms_prediction[0] == 1):
          autism_diagnosis = "The person has Autism disease"
        else:
          autism_diagnosis = "The person does not have Autism disease"
        
    st.success(autism_diagnosis)

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parks_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)


