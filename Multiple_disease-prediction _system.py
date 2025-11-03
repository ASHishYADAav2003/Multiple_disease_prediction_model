

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading saved model

diabetes_model=pickle.load(open('C:/Users/Ashish/.streamlit/trained/sav file/diabetes_model (1).sav','rb'))

parkinsons_model=pickle.load(open('C:/Users/Ashish/.streamlit/trained/sav file/parkinsons_model.sav','rb'))

heart_disease_model=pickle.load(open('C:/Users/Ashish/.streamlit/trained/sav file/heart_disease_model.sav','rb'))

#sidebar for navigation


with st.sidebar:
    selected=option_menu('Multiple Disease Prediction System',
                         ['Diabetes Prediction',
                          'Heart Disease Prediction',
                          'Parkinson Prediction'],
                         icons=['activity','heart','person'],
                         default_index=0)



# diabetes prediction page
if (selected =='Diabetes Prediction'):
    
    #page title
    st.title('Diabetes prediction using ML')
    
    #column for creating input
    
    col1, col2, col3=st.columns(3)

    with col1:    
         Pregrancies= st.text_input('number of pregrancies')
    with col2:   
         Glucose= st.text_input('Glucose level')
    with col3:
         BloodPressure = st.text_input('BloodPressure value')
    with col1:     
         SkinThickness= st.text_input('Skinthickness value')
    with col2:
         Insulin= st.text_input('Insulin value')
    with col3:
         BMI= st.text_input('BMI value')
    with col1:     
         DiabetesPedigreeFuction= st.text_input('Diabetes pedigree function value')
    with col2:
         Age=st.text_input('Age of the person')
    
    
    
    #code for prediction
    diab_diagnosis=''
    
    #creating button for prediction
    if st.button('Diabetes Test result'):
        diab_prediction=diabetes_model.predict([[Pregrancies,Glucose, BloodPressure,SkinThickness,Insulin,BMI, DiabetesPedigreeFuction, Age]])
         
        
        if (diab_prediction[0]==1):
             diab_diagnosis= 'The person is diabetic'
              
        else:
             diab_diagnosis= 'The person is not  diabetic'
    
              
                    
        
    st.success(diab_diagnosis)  
    
    
    
    
    
if (selected =='Heart Disease Prediction'):
    
    #page title
    st.title('Heart Disease prediction using ML')    
    
    
    #column for creating input
    
    col1, col2, col3=st.columns(3) 
    
    with col1:
        age=st.text_input('Age of the person')
        
    with col2:
        sex=st.text_input('sex of the person')
    with col3:
        cp=st.text_input('cp of the person')
    with col1:
        trestbps=st.text_input('trestbps of the person')
    with col2:
        chol=st.text_input('chol of the person')
    with col3:
        fbs=st.text_input('fbs of the person')
    with col1:
        restecg=st.text_input('restecg of the person')
    with col2:
        thalach=st.text_input('thalach of the person')
    with col3:
        exang=st.text_input('exang of the person')
    with col1:
        oldpeak=st.text_input('oldpeak of the person')
    with col2:
        slope=st.text_input('slope of the person')
    with col3:
        ca=st.text_input('ca of the person')
    with col1:
        thal=st.text_input('thal of the person')
        
        
        
    
      
    #code for prediction
    heart_diagnosis=''
    
    #creating button for prediction
    if st.button('Heart Test result'):
        heart_prediction = heart_disease_model.predict([[
    float(age), int(sex), int(cp), float(trestbps), float(chol),
    int(fbs), int(restecg), float(thalach), int(exang), float(oldpeak),
    int(slope), int(ca), int(thal)
]])

         
        
        if (heart_prediction[0]==1):
             heart_diagnosis= 'The person is having heart disease'
              
        else:
             heart_diagnosis= 'The person is not having heart disease'
    
              
                    
        
    st.success(heart_diagnosis)  
    
    
    
    
    
    
    
    
    
    
    
    
    
    

if (selected =='Parkinson Prediction'):
    
    #page title
    st.title('Parkinson prediction using ML') 
    
    
    #column for creating input
    
    col1, col2, col3, col4 =st.columns(4) 
    
    with col1:
        Fo=st.text_input('fo of the person')
    with col2:
        Fhi=st.text_input('fhi of the person')
    with col3:
        Flo=st.text_input('flo of the person')
    with col4:
        Jitter_percent=st.text_input('jitter_percent of the person')
    with col1:
        Jitter_Abs=st.text_input('jitter_Abs of the person')
    with col2:
        RAP=st.text_input('RAP of the person')
    with col3:
        PPQ=st.text_input('PPQ of the person')
    with col4:
        DDP=st.text_input('DDP of the person')
    with col1:
        Shimmer=st.text_input('Shimmer of the person')
    with col2:
        Shimmer_db=st.text_input('Shimmer_db of the person')
    with col3:
        APQ3=st.text_input('APQ3 of the person')
    with col4:
        APQ5=st.text_input('APQ5 of the person')
    with col1:
        APQ=st.text_input('APQ of the person')
    with col2:
        DDA=st.text_input('DDA of the person')
    with col3:
        NHR=st.text_input('NHR of the person')
    with col4:
        HNR=st.text_input('HNR of the person')
    with col1:
        RPDE=st.text_input('RPDE of the person')
    with col2:
        DFA=st.text_input('DFA of the person')
    with col3:
        spread1=st.text_input('spread1 of the person')
    with col4:
        spread2=st.text_input('spread2 of the person')
    with col1:
        D2=st.text_input('D2 of the person')
    with col2:
        PPE=st.text_input('PPE of the person')
        
        
        
    #code for prediction
    park_diagnosis=''
        
        #creating button for prediction
    if st.button('Parkinson Test result'):
            park_prediction=parkinsons_model.predict([[Fo,Fhi,Flo,Jitter_percent,Jitter_Abs,RAP,PPQ,DDP,Shimmer,Shimmer_db,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
             
            
            if (park_prediction[0]==1):
                 park_diagnosis= 'The person is  having parkinson'
                  
            else:
                 park_diagnosis= 'The person is not  having parkinson'
        
                  
                        
            
    st.success(park_diagnosis)  
        
        
        
        
        
        
        
    
  
