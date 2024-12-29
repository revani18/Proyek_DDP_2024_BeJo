import streamlit as st

def show():
    # Menampilkan judul informasi
    st.markdown(f"<h1 style='text-align: center; color: #0077B6;'>INFORMASI APLIKASI & TIM</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.image("images/gambar.png")
    # Menjelaskan sistem perhitungan
    st.markdown(f"<h1 style='color: #0077B6;'>Aplikasi Kesehatan & Kebugaran</h1>", unsafe_allow_html=True)

    st.write("""
    Aplikasi **Kesehatan dan Kebugaran** dirancang untuk membantu Anda dalam memahami indeks massa tubuh (BMI), menghitung kebutuhan kalori, menghitung kebutuhan air minum, dan merencanakan jadwal olahraga. Dengan fitur yang saling melengkapi, aplikasi ini diharapkan dapat mendorong masyarakat untuk lebih peduli terhadap kesehatan dan kebugaran mereka secara menyeluruh. Serta diharapkan dapat membantu lebih banyak orang untuk peduli dan teratur dalam menjaga kesehatan mereka sehari-hari, serta mencapai tujuan kebugaran dengan cara yang lebih efektif dan efisien.
    Berikut adalah penjelasan tentang halaman yang digunakan dalam aplikasi ini:

    ### 1. Aplikasi Kalkulator BMI
    - Kalkulator BMI adalah metrik standar yang digunakan untuk menentukan siapa saja yang masuk dalam kategori berat badan sehat dan tidak sehat. Menghitung berat badan ideal membantu anda menjaga kesehatan dan sebagai pengingat risiko penyakit yang mungkin mengganggu kesehatan anda.
    - Input data kalkulator BMI yaitu : input Jenis Kelamin dan usia, input berat badan dan tinggi badan, untuk menghitung nilai BMI Anda.
    - Rumus yang digunakan adalah BMI = berat badan (kg) / tinggi badan (m) ^2
    - Nilai BMI dan Kategori BMI Anda akan ditampilkan dalam halaman ini.
    - Tips berdasarkan Kategori BMI dan Usia akan ditampilkan dalam halaman ini.
    - Serta Catatan berdasarkan Jenis Kelamin akan ditampilkan dalam halaman ini.
    - Anda dapat membandingkan nilai BMI Anda dengan nilai BMI yang normal untuk usia dan Jenis Kelamin 
    
    ### 2. Aplikasi Hitung Kalori Harian
    - Aplikasi ini membantu pengguna memahami kebutuhan kalori mereka dan bagaimana asupan makanan mempengaruhi berat badan dan kesehatan.
    - Input Data Pengguna: Pengguna diminta untuk memasukkan data Usia (tahun), Berat Badan (kg), Tinggi Badan (cm), Jenis Kelamin (Pria atau Wanita), Tingkat Aktivitas Fisik (Tidak aktif, Sedikit aktif, Aktif, Sangat aktif), dan Tujuan (Menurunkan berat badan, Meningkatkan berat badan, Mempertahankan berat badan)
    - Rumus yang Digunakan: 
    - Rumus untuk menghitung Basal Metabolic Rate (BMR): Untuk Pria: {BMR} = {berat} + {tinggi} - {usia}, Untuk Wanita: {BMR} = {berat} + {tinggi} -{usia}
    - Menghitung Total Daily Energy Expenditure (TDEE) berdasarkan tingkat aktivitas: Jika Tidak aktif: {TDEE} = {BMR}, Jika Sedikit aktif: {TDEE} = {BMR}, Jika Aktif: {TDEE} = {BMR}, Jika Sangat aktif: {TDEE} = {BMR}
    - Rekomendasi Kalori Berdasarkan Tujuan: Untuk Menjaga berat badan: Konsumsi kalori sesuai dengan TDEE, Untuk Menurunkan berat badan: {Kalori yang Disarankan} = {TDEE}, Untuk Menaikkan berat badan: {Kalori yang Disarankan} = {TDEE}
    - Hasil perhitungan kebutuhan kalori harian Anda akan ditampilkan di halaman ini. Anda dapat melihat total kalori yang dibakar dan rekomendasi kalori berdasarkan tujuan Anda. Selain itu, aplikasi juga menampilkan grafik perbandingan antara BMR dan TDEE untuk memberikan gambaran visual tentang kebutuhan kalori Anda.

    ### 3. Aplikasi Hitung Air Minum Harian
    - Kalkulator Kebutuhan Air Minum yang dirancang untuk membantu Anda mengetahui kebutuhan air minum harian berdasarkan berat badan, usia, tingkat aktivitas, dan jenis kelamin. Memastikan tubuh terhidrasi dengan baik sangat penting untuk menjaga fungsi organ tubuh dan mendukung aktivitas sehari-hari. Dengan kalkulator ini, Anda dapat menghitung kebutuhan air harian Anda secara mudah dan akurat.
    - Input data hitung air minum harian yaitu: input berat badan, usia, tingkat aktivitas, dan jenis kelamin untuk menghitung hasil kebutuhan hidrasi anda
    - 1. Rumus yang digunakan adalah Kebutuhan air (ml) = Berat Badan (kg) * 30 ml
    - 2. Rumus berdasarkan tingkat aktivitas : jika Sedang maka Kebutuhan air (ml) = Kebutuhan air * 1.2 . jika tinggi maka Kebutuhan air (ml) = Kebutuhan air * 1.5
    - 3. Rumus berdasarkan usia : jika usia lebih dari 55 tahun, kebutuhan air dikurangi 10% dengan rumus Kebutuhan air (ml) = Kebutuhan air * 0.9
    - 4. Rumus berdasarkan jenis kelamin : jika jenis kelamin Perempuan maka kebut Kebutuhan air (ml) = Kebutuhan air * 0.9
    - Hasil Kebutuhan air akan di tampilkan dalah halaman ini.
    - Anda bisa input Konsumsi air yang sudah diminum sekarang.
    - 5. Rumus berdasarkan konsumsi air yang sudah diminum : Sisa Kebutuhan Air = Kebutuhan air - Konsumsi air yang sudah diminum
    - Hasil sisa kebutuhan air akan di tampilkan dalam halaman ini.
    - Hasil perhitungan kebutuhan air minum harian Anda akan ditampilkan di halaman ini. Setelah itu, Anda dapat menginput jumlah air yang sudah Anda minum untuk melihat sisa kebutuhan air Anda. Lakukan terus hingga kebutuhan air harian Anda terpenuhi
    
    ### 4. Aplikasi Perencanaan Olahraga Mingguan 
    - Aplikasi ini digunakan untuk membantu merencanakan jadwal olahraga mingguan agar Anda dapat menjalani gaya hidup yang lebih sehat dan teratur.
    - Input data dalam aplikasi ini meliputi: Nama pengguna. Pilihan jenis olahraga seperti Jogging, Yoga, Renang, dan lain-lainnya. Durasi olahraga dalam hitungan menit untuk setiap jenis olahraga yang dipilih pada setiap harinya.
    - Jadwal olahraga mingguan Anda akan ditampilkan dalam format tabel berdasarkan input yang diberikan.
    - Total durasi olahraga dalam satu minggu akan dihitung secara otomatis dan ditampilkan dalam halaman ini.
    - Feedback akan diberikan berdasarkan jumlah olahraga yang Anda rencanakan, seperti:
    - Jika Anda berolahraga setiap hari, Anda akan mendapatkan pesan motivasi seperti "Hebat! Anda merencanakan olahraga untuk setiap hari!".
    - Jika hanya beberapa hari, Anda akan mendapatkan saran untuk lebih konsisten.
    - Jika jadwal olahraga minim, Anda akan diberi dorongan untuk meningkatkan aktivitas.
    - Aplikasi ini membantu Anda menciptakan kebiasaan olahraga yang teratur dan memberikan wawasan tentang total waktu yang Anda dedikasikan untuk kesehatan Anda
   
    """)

# Menampilkan informasi tentang tim pengembang
    st.markdown(f"<h1 style='color: #0077B6;'>Tim Pengembang</h1>", unsafe_allow_html=True)
    st.write("""
    - **Ketua Tim**: 
    \n 1. Revani
    """) 
    st.write("""
    - **Anggota Tim**: 
    \n 2. Fitri Aura Ramadhani
    \n 3. Yurida Yahsya
    \n 4. Muhammad Fajrul Falah
    """)

    st.markdown(f"<h2 style='text-align: center; color: #0077B6;'>Foto Kelompok BeJo</h2></br>", unsafe_allow_html=True)
    col1, col2,col3 = st.columns(3)  # Membuat tiga kolom
    col2.image("images/revani.png", width=250, caption="Revani")
    col1, col2,col3 = st.columns(3)  # Membuat tiga kolom
    col1.image("images/yuri.png", width=200, caption="Yurida Yahsya")
    col2.image("images/arul.png", width=200, caption="Muhammad Fajrul Falah")
    col3.image("images/aura.png", width=290, caption="Fitri Aura Ramadhani")