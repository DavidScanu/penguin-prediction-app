import pickle
import streamlit as st
import time
from sklearn import preprocessing


# venv 
# Install streamlit, scikit-learn

# Import pickle data 
pickle_in = open("model.pkl","rb")
export = pickle.load(pickle_in)
pickle_in.close()

# Variables
model_best = export['model_best_neigh_2']
scaler = export['scaler_neigh_2']
labelencoder_species = export['labelencoder_species']
X_neigh_2_info = export['X_neigh_2_info']



def prediction(culmen_length_mm, flipper_length_mm):

    if culmen_length_mm and flipper_length_mm:

        X = [[float(culmen_length_mm), float(flipper_length_mm)]]
        # Mise à l'échelle
        X_scaled = scaler.transform(X)
        # Prédiction
        prediction = model_best.predict(X_scaled)
        prediction_specie = labelencoder_species.inverse_transform(prediction)
        message = f"This penguin is : {prediction_specie[0]}."
    else : 
        message = "Please enter penguin parameters."
    
    return message


# Streamlit
st.set_page_config(
    page_title="Penguin Prediction",
    page_icon=":penguin:",
    layout="wide",
    initial_sidebar_state="expanded"
)

with st.container():
    st.title(':penguin: Penguin Prediction')

col1, col2 = st.columns(2)

with col1:
    st.subheader('Enter penguin parameters :')
    culmen_length_mm = st.slider("Culmen length in mm", 30, 60, 43)
    flipper_length_mm = st.slider("Flipper length in mm", 170, 232, 200)

with col2:
    # Check if session variable is set
    if 'my_button' in st.session_state:
        with st.spinner('Wait for it...'):
            time.sleep(1)
            st.header(prediction(culmen_length_mm, flipper_length_mm))

# st.write(st.session_state) 
if 'my_button' not in st.session_state:
    st.session_state.my_button = True
