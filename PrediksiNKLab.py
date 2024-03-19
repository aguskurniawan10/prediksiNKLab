# Mengimpor library
import pandas as pd
import streamlit as st
import pickle

# Menghilangkan warning
import warnings
warnings.filterwarnings("ignore")

# Menulis judul
st.markdown("<h1 style='text-align: center; '> Prediksi Nilai Kalor Lab</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; '>PLN Indonesia Power UBP JPR</h1>", unsafe_allow_html=True)

# Pilihan utama
pilihan = st.sidebar.selectbox('Penasaran kan mau liat hasil prediksinya ?', ('Prediksi NK Lab'))

if pilihan == 'Prediksi NK Lab':

    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            NKCOALoading = st.number_input('NK COA Loading', value=1)
        with col2:
            TotalMoisture = st.number_input('Total Moisture', value=0)
        with col3:
            AshContent = st.number_input('Ash Content', value=0)
        with col4:
            TotalSulphur = st.number_input('TotalSulphur', value=0)

    data1 = {
        'NK COA Loading': NKCOALoading,
        'Total Moisture': TotalMoisture,
        'Ash Content': AshContent,
        'TotalSulphur': TotalSulphur,
    }

    kolom = list(data1.keys())
    df_final= pd.DataFrame([data1.values()], columns=kolom)

    # Load model
    my_model1 = pickle.load(open('Nklabfix.pkl', 'rb'))




    # Predict
    result = round(float(my_model1.predict(df_final)), 2)

    st.write("<center><b><h4>Prediksi Nilai Kalor Lab =", result, "</b></h4>Kcal/Kg", unsafe_allow_html=True)
    
    st.markdown('---' * 10)
