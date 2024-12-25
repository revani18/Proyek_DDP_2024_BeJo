import streamlit as st
import matplotlib.pyplot as plt

def show():
    # Judul Halaman
    st.markdown(f"<h1 style='text-align: center; color: #0077B6;'>Aplikasi Hitung Kalori Harian</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.subheader("Kalkulator Kebutuhan Kalori")
    st.write("Dengan kalkulator kebutuhan kalori anda dapat mengetahui kebutuhan kalori anda berdasarkan tinggi badan, berat badan, usia, jenis kelamin, dan tingkat aktivitas fisik anda.")

    # Membuat form untuk input
    with st.form(key='kalkulator_form'):
        # Menggunakan nilai default tanpa session state
        usia = st.number_input("Usia (tahun)", min_value=1, step=1)
        berat_badan = st.number_input("Berat Badan (kg)", min_value=0.0, format="%.2f", step=0.1)
        tinggi_badan = st.number_input("Tinggi Badan (cm)", min_value=0.0, format="%.2f", step=0.1)
        jenis_kelamin = st.selectbox("Jenis Kelamin", ("Pria", "Wanita"))

        # Pilih tingkat aktivitas fisik
        tingkat_aktivitas = st.selectbox(
            "Tingkat Aktivitas Fisik",
            ("Tidak aktif", "Sedikit aktif", "Aktif", "Sangat aktif")
        )

        # Menambahkan interaksi untuk menyesuaikan kalori
        tujuan = st.selectbox(
            "Apa tujuan Anda?",
            ("Menjaga berat badan", "Menurunkan berat badan", "Menaikkan berat badan")
        )

        # Tombol submit
        submit_button = st.form_submit_button("Hitung")

    # Tombol Hitung
    if submit_button:
        # Validasi input kosong
        if usia is None or berat_badan == 0.0 or tinggi_badan == 0.0 or jenis_kelamin is None or tingkat_aktivitas is None or tujuan is None:
            st.error("Semua kolom harus diisi dengan valid. Pastikan usia, berat badan, tinggi badan, jenis kelamin, tingkat aktivitas, dan tujuan telah dipilih.")
        else:
            # Rumus untuk menghitung kebutuhan kalori dasar (BMR) menggunakan rumus Mifflin-St Jeor
            if jenis_kelamin == "Pria":
                bmr = 10 * berat_badan + 6.25 * tinggi_badan - 5 * usia + 5  # BMR untuk pria
            else:
                bmr = 10 * berat_badan + 6.25 * tinggi_badan - 5 * usia - 161  # BMR untuk wanita

            # Faktor aktivitas fisik
            if tingkat_aktivitas == "Tidak aktif":
                tdee = bmr * 1.2
            elif tingkat_aktivitas == "Sedikit aktif":
                tdee = bmr * 1.375
            elif tingkat_aktivitas == "Aktif":
                tdee = bmr * 1.55
            else:  # Sangat aktif
                tdee = bmr * 1.725

            # Menampilkan hasil
            st.markdown(f"<h2 style='text-align: center; color: #0078D7;'>Kebutuhan Kalori Harian (TDEE) Anda adalah:</h2>", unsafe_allow_html=True)
            st.markdown(f"<h1 style='text-align: center; color: #0078D7;'>{tdee:.2f} kalori per hari</h1><br/>", unsafe_allow_html=True)

            # Menampilkan kalori yang disarankan berdasarkan tujuan
            if tujuan == "Menjaga berat badan":
                st.write(f"<h5 style='text-align: center;' >Disarankan  : Jika tujuan Anda menjaga berat badan, maka Anda dapat mempertahankan asupan kalori harian sesuai dengan TDEE yang dihitung</h5><br/>", unsafe_allow_html=True)
            elif tujuan == "Menurunkan berat badan":
                kalori_rekomendasi = tdee * 0.8  # Mengurangi 20% dari TDEE untuk penurunan berat badan
                st.write(f"<h5 style='text-align: center;' >Disarankan : Jika tujuan Anda menurunkan berat badan, maka Anda bisa mengonsumsi sekitar {kalori_rekomendasi:.2f} kalori per hari</h5><br/>", unsafe_allow_html=True)
            else:  # Menaikkan berat badan
                kalori_rekomendasi = tdee * 1.2  # Menambah 20% dari TDEE untuk kenaikan berat badan
                st.write(f"<h5 style='text-align: center;' >Disarankan : Jika tujuan Anda menaikkan berat badan, maka Anda bisa mengonsumsi sekitar {kalori_rekomendasi:.2f} kalori per hari</h5><br/>", unsafe_allow_html=True)

            # Menambahkan grafik untuk visualisasi BMR dan TDEE
            labels = ['BMR', 'TDEE']
            values = [bmr, tdee]

            fig, ax = plt.subplots()
            ax.bar(labels, values, color=['pink', 'lavender'])
            ax.set_ylabel('Kalori (kcal)')
            ax.set_title('Grafik Perbandingan BMR dan TDEE')
            st.pyplot(fig)
