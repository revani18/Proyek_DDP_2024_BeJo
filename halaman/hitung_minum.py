import streamlit as st

def show():

    # Judul Halaman
    st.title("Aplikasi Hitung Air Minum Harian")
    st.write("Aplikasi ini dapat membantu Anda menghitung kebutuhan air minum harian Anda.")

    # Form Input
    st.header("Masukkan Data Anda")
    weight = st.number_input("Berat Badan (kg)", min_value=1.0, max_value=300.0, step=0.1)
    age = st.number_input("Usia (tahun)", min_value=1, max_value=120, step=1)
    activity_level = st.selectbox("Tingkat Aktivitas", ["Rendah", "Sedang", "Tinggi"])

    # Kalkulasi
    if st.button("Hitung"):
        if weight and age:
            # Rumus dasar kebutuhan air
            water_needs = weight * 30  # ml per kg berat badan
            
            # Penyesuaian berdasarkan tingkat aktivitas
            if activity_level == "Sedang":
                water_needs *= 1.2
            elif activity_level == "Tinggi":
                water_needs *= 1.5

            # Penyesuaian usia
            if age > 55:
                water_needs *= 0.9

            # Tampilkan hasil
            st.markdown(f"<h2 style='text-align: center; color: #0078D7;'>Kebutuhan Air Anda:</h2>", unsafe_allow_html=True)
            st.markdown(f"<h1 style='text-align: center; color: #0078D7;'>{water_needs:.0f} ml/hari</h1>", unsafe_allow_html=True)
        else:
            st.error("Mohon masukkan data dengan benar!")
