import streamlit as st
import matplotlib.pyplot as plt

def show():
    # Judul Halaman
    st.title("Aplikasi Hitung Kalori Harian")
    st.write("Aplikasi ini dapat membantu Anda menghitung kebutuhan kalori harian berdasarkan data usia, jenis kelamin, tinggi badan, berat badan, dan tingkat aktivitas fisik")

    # Input data usia, berat badan, tinggi badan, dan jenis kelamin
    st.header("Masukkan Data Anda")

    # Menyimpan input di session state agar tetap ada meskipun halaman direfresh
    if 'usia' not in st.session_state:
        st.session_state.usia = 25
    if 'berat_badan' not in st.session_state:
        st.session_state.berat_badan = 60
    if 'tinggi_badan' not in st.session_state:
        st.session_state.tinggi_badan = 160
    if 'jenis_kelamin' not in st.session_state:
        st.session_state.jenis_kelamin = "Pria"
    if 'tingkat_aktivitas' not in st.session_state:
        st.session_state.tingkat_aktivitas = "Tidak aktif"
    if 'tujuan' not in st.session_state:
        st.session_state.tujuan = "Menjaga berat badan"

    # Menggunakan nilai yang disimpan di session_state
    usia = st.number_input("Usia (tahun)", min_value=1, max_value=100, value=st.session_state.usia)
    berat_badan = st.number_input("Berat Badan (kg)", min_value=1, value=st.session_state.berat_badan)
    tinggi_badan = st.number_input("Tinggi Badan (cm)", min_value=50, value=st.session_state.tinggi_badan)
    jenis_kelamin = st.selectbox("Jenis Kelamin", ("Pria", "Wanita"), index=("Pria", "Wanita").index(st.session_state.jenis_kelamin))

    # Pilih tingkat aktivitas fisik
    tingkat_aktivitas = st.selectbox(
        "Tingkat Aktivitas Fisik",
        ("Tidak aktif", "Sedikit aktif", "Aktif", "Sangat aktif"),
        index=("Tidak aktif", "Sedikit aktif", "Aktif", "Sangat aktif").index(st.session_state.tingkat_aktivitas)
    )

    # Menambahkan interaksi untuk menyesuaikan kalori
    tujuan = st.selectbox(
        "Apa tujuan Anda?",
        ("Menjaga berat badan", "Menurunkan berat badan", "Menaikkan berat badan"),
        index=("Menjaga berat badan", "Menurunkan berat badan", "Menaikkan berat badan").index(st.session_state.tujuan)
    )

    # Simpan nilai tujuan di session state agar tidak hilang
    st.session_state.tujuan = tujuan

    # Tombol Hitung
    if st.button("Hitung"):
        # Simpan nilai input ke session state agar tidak hilang
        st.session_state.usia = usia
        st.session_state.berat_badan = berat_badan
        st.session_state.tinggi_badan = tinggi_badan
        st.session_state.jenis_kelamin = jenis_kelamin
        st.session_state.tingkat_aktivitas = tingkat_aktivitas

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
            st.write(f"<h5 style='text-align: center;' >Disarankan : Anda dapat mempertahankan asupan kalori harian sesuai dengan TDEE yang dihitung</h5><br/>", unsafe_allow_html=True)
        elif tujuan == "Menurunkan berat badan":
            kalori_rekomendasi = tdee * 0.8  # Mengurangi 20% dari TDEE untuk penurunan berat badan
            st.write(f"<h5 style='text-align: center;' >Disarankan : Untuk menurunkan berat badan, Anda bisa mengonsumsi sekitar {kalori_rekomendasi:.2f} kalori per hari</h5><br/>", unsafe_allow_html=True)
        else:  # Menaikkan berat badan
            kalori_rekomendasi = tdee * 1.2  # Menambah 20% dari TDEE untuk kenaikan berat badan
            st.write(f"<h5 style='text-align: center;' >Disarankan : Untuk menaikkan berat badan, Anda bisa mengonsumsi sekitar {kalori_rekomendasi:.2f} kalori per hari</h5><br/>", unsafe_allow_html=True)

        # Menambahkan grafik untuk visualisasi BMR dan TDEE
        labels = ['BMR', 'TDEE']
        values = [bmr, tdee]

        fig, ax = plt.subplots()
        ax.bar(labels, values, color=['pink', 'lavender'])
        ax.set_ylabel('Kalori (kcal)')
        ax.set_title('Grafik Perbandingan BMR dan TDEE')
        st.pyplot(fig)
