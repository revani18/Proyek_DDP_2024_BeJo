import streamlit as st
from streamlit_option_menu import option_menu
from halaman import kalkulator_bmi, hitung_kalori, hitung_minum, jadwal_olahraga

st.set_page_config(page_title="Aplikasi Kesehatan dan Kebugaran", layout="wide")

with st.sidebar:
    selected = option_menu("Main Menu", ["Kalkulator BMI", "Hitung Kalori", "Hitung Air Minum", "Jadwal Olahraga"], 
        icons=['calculator', 'egg-fried', 'cup-straw', 'calendar'], menu_icon="cast", default_index=0)
    selected

if selected == "Kalkulator BMI":
    kalkulator_bmi.show()
elif selected == "Hitung Kalori":
    hitung_kalori.show()
elif selected == "Hitung Air Minum":
    hitung_minum.show()
elif selected == "Jadwal Olahraga":
    jadwal_olahraga.show()