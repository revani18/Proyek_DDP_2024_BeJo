import streamlit as st

def show():
    # Menampilkan judul informasi
    st.markdown(f"<h1 style='text-align: center; color: #0077B6;'>Tentang Kami</h1>", unsafe_allow_html=True)
    st.markdown("---")

    # Menampilkan informasi tentang Visi&Misi
    st.markdown(f"<h1 style='color: #0077B6;'>Visi & Misi</h1>", unsafe_allow_html=True)
    st.write("""**Visi Kami** adalah menciptakan aplikasi yang bisa membantu banyak orang untuk peduli dan teratur dalam menjaga kesehatan mereka sehari-hari, serta mencapai tujuan kebugaran dengan cara yang lebih efektif dan efisien.""")
    st.write("""**Misi Kami** adalah:
             \n 1. Menyediakan Fitur Kalkulator BMI yang membantu pengguna memahami apakah berat badan mereka berada dalam rentang yang sehat atau tidak.
             \n 2. Menyediakan Fitur Hitung Kalori yang membantu pengguna menghitung jumlah kalori yang dibutuhkan tubuh setiap hari.
             \n 3. Menyediakan Fitur Hitung Air Minum yang membantu pengguna untuk memenuhi kebutuhan cairan tubuh.
             \n 4. Menyediakan Fitur Jadwal Olahraga yang membantu pengguna untuk merencanakan dan mengatur jadwal olahraga mingguan. Dengan fitur ini, pengguna dapat secara teratur berolahraga dan menjaga kebugaran tubuh.""")
    
    # Menampilkan informasi tentang tim pengembang
    st.markdown(f"<h1 style='color: #0077B6;'>Tim Pengembang</h1>", unsafe_allow_html=True)
    st.write("""
    - **Ketua Tim**: 
    \n 1. Revani (0110224111)
    """) 
    st.write("""
    - **Anggota Tim**: 
    \n 2. Fitri Aura Ramadhani (0110224096)
    \n 3. Yurida Yahsya (0110224100)
    \n 4. Muhammad Fajrul Falah (0110224072)
    """)

    st.markdown(f"\n<h2 style='text-align: center; color: #0077B6;'>Foto Kelompok BeJo</h2></br>", unsafe_allow_html=True)
    col1, col2,col3 = st.columns(3)  # Membuat tiga kolom
    col2.image("images/revani.png", width=250, caption="Revani")
    col1, col2,col3 = st.columns(3)  # Membuat tiga kolom
    col1.image("images/yuri.png", width=200, caption="Yurida Yahsya")
    col2.image("images/arul.png", width=200, caption="Muhammad Fajrul Falah")
    col3.image("images/aura.png", width=290, caption="Fitri Aura Ramadhani")