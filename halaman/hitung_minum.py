import streamlit as st

def show():
    st.markdown(f"<h1 style='text-align: center; color: #0077B6;'>Aplikasi Hitung Air Minum Harian</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.subheader("Kalkulator Kebutuhan Air Minum")
    st.write("Kalkulator Kebutuhan Air Minum adalah cara menghitung kebutuhan air minum harian berdasarkan data berat badan, usia, dan tingkat aktivitas")

    # Membuat form untuk input
    with st.form(key='air_minum_form'):
        # Form Input
        berat_badan = st.number_input("Berat Badan (kg)", min_value=0.0, format="%.2f", step=0.1)
        usia = st.number_input("Usia (tahun)", min_value=1, step=1)
        tingkat_aktivitas = st.selectbox("Tingkat Aktivitas", ["Rendah", "Sedang", "Tinggi"])

        # Tombol submit
        submit_button = st.form_submit_button("Hitung")

    # Kalkulasi jika tombol submit ditekan
    if submit_button:
        if berat_badan and usia:
            # Rumus dasar kebutuhan air
            kebutuhan_air = berat_badan * 30  # ml per kg berat badan
            # Penyesuaian berdasarkan tingkat aktivitas
            if tingkat_aktivitas == "Sedang":
                kebutuhan_air *= 1.2
            elif tingkat_aktivitas == "Tinggi":
                kebutuhan_air *= 1.5

            # Penyesuaian usia
            if usia > 55:
                kebutuhan_air *= 0.9

            # Tampilkan hasil
            st.markdown(f"<h2 style='text-align: center; color: #0078D7;'>Kebutuhan Air Anda:</h2>", unsafe_allow_html=True)
            st.markdown(f"<h1 style='text-align: center; color: #0078D7;'>{kebutuhan_air:.0f} ml/hari</h1>", unsafe_allow_html=True)
        else:
            st.error("Mohon masukkan data dengan benar!")
