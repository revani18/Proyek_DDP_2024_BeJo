import streamlit as st

def show():
    st.markdown(f"<h1 style='text-align: center; color: #0077B6;'>Aplikasi Hitung Air Minum Harian</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.subheader("Kalkulator Hidrasi")
    st.write("Berdasarkan aktivitas dan kondisi tubuh yang berbeda-beda, kita memiliki tingkat kebutuhan air yang juga beragam. Ketahui berapa banyak air yang kamu butuhkan dalam sehari dengan menggunakan Kalkulator Hidrasi!")

    # Fungsi untuk menghitung kebutuhan hidrasi
    def hitung_kebutuhan_air(berat, usia, tingkat_aktivitas, jenis_kelamin):
        kebutuhan_air_dasar = berat * 30  # ml per kg berat badan
        penyesuaian = 1.0

        # Penyesuaian berdasarkan tingkat aktivitas
        if tingkat_aktivitas == "Sedang":
            penyesuaian = 1.2
        elif tingkat_aktivitas == "Tinggi":
            penyesuaian = 1.5

        # Penyesuaian berdasarkan usia
        if usia > 55:
            penyesuaian *= 0.9

        # Penyesuaian berdasarkan jenis kelamin
        if jenis_kelamin == "Perempuan":
            penyesuaian *= 0.9

        # Total kebutuhan air
        return kebutuhan_air_dasar * penyesuaian

    # Kelas untuk melacak hidrasi
    class PelacakHidrasi:
        def __init__(self, kebutuhan_harian):
            self.kebutuhan_harian = kebutuhan_harian
            self.konsumsi = 0

        def catat_konsumsi_air(self, jumlah):
            self.konsumsi += jumlah
            if self.konsumsi >= self.kebutuhan_harian:
                return "Selamat! Anda telah mencapai kebutuhan hidrasi harian! 🎉"
            return f"Sisa kebutuhan: {self.kebutuhan_harian - self.konsumsi:.0f} ml"

    # Menyimpan pelacak di session state
    if "pelacak" not in st.session_state:
        st.session_state.pelacak = None
        st.session_state.berat = ""
        st.session_state.usia = ""
        st.session_state.tingkat_aktivitas = "Pilih tingkat aktivitas"
        st.session_state.jenis_kelamin = "Pilih jenis kelamin"
        st.session_state.konsumsi = ""

    # Form input data
    with st.form(key='form_input'):
        # Input berat badan
        input_berat = st.text_input(
            "Berat Badan (kg)", 
            value=st.session_state.berat,
            placeholder="Masukkan berat badan Anda...",
            help="Masukkan berat badan Anda dalam satuan kilogram (kg)."
        )
        berat = None
        if input_berat:
            try:
                berat = float(input_berat)
                st.session_state.berat = input_berat
            except ValueError:
                st.error("Berat badan harus berupa angka!")

        # Input usia
        input_usia = st.text_input(
            "Usia (tahun)", 
            value=st.session_state.usia,
            placeholder="Masukkan usia Anda...",
            help="Masukkan usia Anda dalam satuan tahun."
        )
        usia = None
        if input_usia:
            try:
                usia = int(input_usia)
                st.session_state.usia = input_usia
            except ValueError:
                st.error("Usia harus berupa angka!")

        # Input tingkat aktivitas
        tingkat_aktivitas = st.selectbox(
            "Tingkat Aktivitas",
            ["Pilih tingkat aktivitas", "Rendah", "Sedang", "Tinggi"],
            index=["Pilih tingkat aktivitas", "Rendah", "Sedang", "Tinggi"].index(st.session_state.tingkat_aktivitas),
            help="Pilih tingkat aktivitas Anda dari rendah, sedang, atau tinggi."
        )
        st.session_state.tingkat_aktivitas = tingkat_aktivitas

        # Input jenis kelamin
        jenis_kelamin = st.selectbox(
            "Jenis Kelamin",
            ["Pilih jenis kelamin", "Laki-laki", "Perempuan"],
            index=["Pilih jenis kelamin", "Laki-laki", "Perempuan"].index(st.session_state.jenis_kelamin),
            help="Pilih jenis kelamin Anda."
        )
        st.session_state.jenis_kelamin = jenis_kelamin

        # Tombol kirim form
        submit_button = st.form_submit_button("Hitung Kebutuhan Hidrasi")

    # Menghitung kebutuhan hidrasi jika tombol form ditekan
    if submit_button:
        if berat is not None and usia is not None and tingkat_aktivitas != "Pilih tingkat aktivitas" and jenis_kelamin != "Pilih jenis kelamin":
            kebutuhan_harian = hitung_kebutuhan_air(berat, usia, tingkat_aktivitas, jenis_kelamin)
            st.session_state.pelacak = PelacakHidrasi(kebutuhan_harian)
            st.markdown(f"<h2 style='text-align: center; color: #0078D7;'>Kebutuhan air Anda adalah : </h2>", unsafe_allow_html=True)
            st.markdown(f"<h1 style='text-align: center; color: #0078D7;'>{kebutuhan_harian:.0f} ml/hari</h1><br/>", unsafe_allow_html=True)
        else:
            st.error("Mohon masukkan semua data dengan benar!")

    # Log konsumsi air jika pelacak sudah ada
    if st.session_state.pelacak:
        st.markdown("### Air yang sudah Anda minum sekarang")
        
        # Form input konsumsi air
        with st.form(key='form_konsumsi'):
            # Input konsumsi air
            input_konsumsi = st.text_input(
                "Konsumsi Air (ml)", 
                value=st.session_state.konsumsi,
                placeholder="Silakan masukkan air yang sudah anda konsumsi...",
                help="Masukkan jumlah air yang sudah Anda minum dalam satuan mililiter (ml)."
            )
            konsumsi = None
            if input_konsumsi:
                try:
                    konsumsi = int(input_konsumsi)
                    st.session_state.konsumsi = input_konsumsi
                except ValueError:
                    st.error("Konsumsi air harus berupa angka!")

            # Tombol kirim form konsumsi
            submit_button_konsumsi = st.form_submit_button("Tambah Konsumsi")

        # Menambahkan konsumsi air jika tombol ditekan
        if submit_button_konsumsi:
            if konsumsi is not None:
                pesan = st.session_state.pelacak.catat_konsumsi_air(konsumsi)
                st.info(pesan)
            else:
                st.error("Mohon masukkan jumlah konsumsi air yang valid!")
