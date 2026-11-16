import pickle
import json
import pandas as pd
import numpy as np
import streamlit as st

# Load all files

with open('model_lin_reg.pkl', 'rb') as file_1:
  model_lin_reg = pickle.load(file_1)

with open('model_scaler.pkl', 'rb') as file_2:
  model_scaler = pickle.load(file_2)

with open('model_encoder.pkl','rb') as file_3:
  model_encoder = pickle.load(file_3)

with open('list_num_cols.txt', 'r') as file_4:
  list_num_cols = json.load(file_4)

with open('list_cat_cols.txt', 'r') as file_5:
  list_cat_cols = json.load(file_5)
  
def run():
    # Pembuatan form
    
    with st.form('fifa-2022-046-HCK'):
        name = st.text_input('Your name', value='-')
        
        age = st.number_input('Your age',
                              min_value=15, 
                              max_value=40, 
                              step=1, 
                              help='Usia Pemain')
        
        weight = st.number_input('Your weight', 
                                 min_value=60, 
                                 max_value=100, 
                                 value=80)
        
        height = st.slider('Height', 
                           min_value=150,
                           max_value=230, 
                           value=180)
        
        price = st.number_input('Your price', 
                                min_value=0, 
                                max_value=1000000,
                                value=0)
        
        st.markdown('----')
        
        attacking_work_rate = st.selectbox('Attacking Work Rate', ('Low', 'Medium', 'High'))
        defensive_work_rate = st.radio('Defensive Work Rate', ('Low', 'Medium', 'High'))
        
        st.markdown('----')
        
        pace = st.number_input('Pace', min_value=0, max_value=100, value=50)
        shooting = st.number_input('Shooting', min_value=0, max_value=100, value=50)
        passing = st.number_input('Passing', min_value=0, max_value=100, value=50)
        dribbling = st.number_input('Dribbling', min_value=0, max_value=100, value=50)
        defending = st.number_input('Defending', min_value=0, max_value=100, value=50)
        physicality = st.number_input('Physically', min_value=0, max_value=100, value=50)
        
        submitted = st.form_submit_button('Predict')
        
        # Create a new data
        # Use all columns not just the results of feature selection

    data_inf = {
        'Name': name,
        'Age': age,
        'Height': height,
        'Weight': weight,
        'Price': price,
        'AttackingWorkRate': attacking_work_rate,
        'DefensiveWorkRate': defensive_work_rate,
        'PaceTotal': pace,
        'ShootingTotal': shooting,
        'PassingTotal': passing,
        'DribblingTotal': dribbling,
        'DefendingTotal': defending,
        'PhysicalityTotal': physicality
    }

    data_inf = pd.DataFrame([data_inf])
    data_inf
    
    if submitted:
        
        # Split the dataset between numerical and categorical 

            data_inf_num = data_inf[list_num_cols]
            data_inf_cat = data_inf[list_cat_cols]
        
        # Feature Scaling and Feature Encoding

            ## Feature Scaling
            data_inf_num_scaled = model_scaler.transform(data_inf_num)

            ## Feature Encoding
            data_inf_cat_encoded = model_encoder.transform(data_inf_cat)

            ## Concate
            data_inf_final = np.concatenate([data_inf_num_scaled, data_inf_cat_encoded], axis=1)
            
            # Predict using Linear Regression

            y_pred_inf = model_lin_reg.predict(data_inf_final)
            st.write('# Rating Score : ', str(int(y_pred_inf[0])))

if __name__ == '__main__':
    run()