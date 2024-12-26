import streamlit as st
from streamlit_option_menu import option_menu
from halaman import kalkulator_bmi, hitung_kalori, hitung_minum, jadwal_olahraga

# Mengatur Layout Halaman
st.set_page_config(page_title="Aplikasi Kesehatan & Kebugaran", page_icon="💙", layout="wide")

# Sidebar untuk menu navigasi
with st.sidebar:
    selected = option_menu("Main Menu", ["Kalkulator BMI", "Hitung Kalori", "Hitung Air Minum", "Jadwal Olahraga"], 
        icons=['calculator', 'egg-fried', 'cup-straw', 'calendar'], 
        menu_icon="cast", default_index=0, orientation="vertical",
        styles={
            "container": {"padding": "0!important", "background-color": "#e6f5ff"},
            "icon": {"color": "#0077B6", "font-size": "22px"},
            "nav-link": {"font-size": "18px", "text-align": "left", "padding": "12px 16px","border-radius": "8px","background-color": "#ffffff","color": "#0077B6", "--hover-color": "#b3e0ff"},
            "nav-link-selected": {"background-color": "#0077B6", "color": "white"},
            "menu-title": {"font-size": "24px","font-weight": "bold","color": "#0077B6", "padding-top": "10px"},
})
    selected

# Halaman sesuai pilihan pengguna
if selected == "Kalkulator BMI":
    kalkulator_bmi.show()
elif selected == "Hitung Kalori":
    hitung_kalori.show()
elif selected == "Hitung Air Minum":
    hitung_minum.show()
elif selected == "Jadwal Olahraga":
    jadwal_olahraga.show()