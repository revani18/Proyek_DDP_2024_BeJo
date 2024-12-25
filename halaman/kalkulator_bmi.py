import streamlit as st
import pandas as pd

class BMI:
    def __init__(self):
        self.berat = 0
        self.tinggi = 0
        self.usia = 0
        self.jenis_kelamin = ""
        self.bmi = 0
        self.kategori = ""
        self.tips = ""
    
    def get_input(self):
        # Membuat form untuk input
        with st.form(key='bmi_form'):
            # input jenis kelamin, berat badan, dan tinggi badan
            self.jenis_kelamin = st.radio("Pilih Jenis Kelamin : ", ["Laki-Laki", "Perempuan"])
            self.berat = st.number_input("Masukkan Berat Badan (kg) : ", min_value=0.0, format="%.2f", step=0.1)
            self.tinggi = st.number_input("Masukkan Tinggi Badan (cm) : ", min_value=0.0, format="%.2f", step=0.1)
            self.usia = st.number_input("Masukkan Usia Anda (tahun) : ", min_value=1, step=1)
            
            # Tombol submit form
            submit_button = st.form_submit_button("Hitung BMI")
        
        return submit_button
    
    def hitung_bmi(self):
        # Rumus menghitung BMI : Berat(kg) / Tinggi(m) * Tinggi(m)
        tinggi_m = self.tinggi / 100    
        self.bmi = self.berat / (tinggi_m ** 2)
    
    def kategori_bmi(self):
        # Kategori BMI berdasarkan Nilai BMI
        if self.bmi < 18.5:
            self.kategori = "Kurus"
            self.tips = "Disarankan untuk meningkatkan konsumsi kalori, melakukan latihan kekuatan dan istirahat yang cukup"
        elif 18.5 <= self.bmi < 24.9:
            self.kategori = "Normal"
            self.tips = "Tetap aktif dan konsumsi makanan bergizi"
        elif 25 <= self.bmi < 29.9:
            self.kategori = "Gemuk"
            self.tips = "Disarankan untuk meningkatkan aktivitas fisik dan memperbaiki pola makan"
        elif 30 <= self.bmi < 34.9:
            self.kategori = "Obesitas Klas I"
            self.tips = "Disarankan untuk meningkatkan aktivitas fisik dan berolahraga secara teratur serta menjaga pola makan dengan mengurangi makanan tinggi gula dan tinggi lemak"
        else:
            self.kategori = "Obesitas Klas II"
            self.tips = "Penting untuk berkonsultasi dengan dokter dan merencanakan penurunan berat badan secara bertahap"
        
    # Menampilkan
    def show(self):
        # st.title("Aplikasi Kalkulator BMI (Body Mass Index)")
        st.markdown(f"<h1 style='text-align: center; color: #0077B6;'>Aplikasi Kalkulator BMI (Body Mass Index)</h1>", unsafe_allow_html=True)
        st.markdown("---")
        st.subheader("Kalkulator BMI")
        st.write("Kalkulator BMI adalah metrik standar yang digunakan untuk menentukan siapa saja yang masuk dalam kategori berat badan sehat dan tidak sehat. Menghitung berat badan ideal membantu anda menjaga kesehatan dan sebagai pengingat risiko penyakit yang mungkin mengganggu kesehatan anda. Kalkulator BMI adalah cara menghitung berat badan ideal berdasarkan tinggi dan berat badan. BMI juga dapat dibedakan berdasarkan usia dan jenis kelamin. Berikut adalah kategori BMI yang umum digunakan :")

        # Menampilkan tabel kategori BMI
        data = {
            "Kategori BMI": ["Kurus", "Normal", "Gemuk", "Obesitas Klas I", "Obesitas Klas II"],
            "Indeks BMI": ["Kurang dari 18.5", "18.5 - 24.9", "25 - 29.9", "30 - 34.9", "Lebih dari 35"],
            "Deskripsi": [
                "Berat badan kurang dari normal.",
                "Berat badan normal dan ideal.",
                "Kelebihan berat badan.",
                "Obesitas tingkat 1, berisiko lebih tinggi untuk kesehatan.",
                "Obesitas tingkat 2, berisiko sangat tinggi untuk kesehatan."
            ]
        }
        df = pd.DataFrame(data)
        st.table(df)
        
        # Mengambil input dari pengguna melalui form
        submit_button = self.get_input()

        # Hitung dan tampilkan hasil BMI jika tombol "Hitung BMI" ditekan
        if submit_button:
            if self.berat > 0 and self.tinggi > 0 and self.usia > 0:

                # Perhitungan BMI
                self.hitung_bmi()
                self.kategori_bmi()

                # Tampilkan hasil perhitungan
                st.markdown(f"<h2 style='text-align: center; color: #0078D7;'>BMI Anda adalah : {self.bmi:.2f}</h2>", unsafe_allow_html=True)
                st.markdown(f"<h2 style='text-align: center; color: #0078D7;'>Kategori BMI : {self.kategori}</h2>", unsafe_allow_html=True)

                # Tampilkan tips berdasarkan kategori
                st.markdown(f"<h4 style='text-align: left; '>Tips untuk Anda : {self.tips}</h4>", unsafe_allow_html=True)

                # Menambahkan tips berdasarkan usia
                if self.usia < 18:
                    st.markdown(f"<h4 style='text-align: left; '>Tips Usia Muda : Fokus pada pertumbuhan fisik yang sehat dan hindari diet ketat</h4>", unsafe_allow_html=True)
                elif self.usia >= 18 and self.usia < 40:
                    st.markdown(f"<h4 style='text-align: left; '>Tips Usia Dewasa Muda: Jaga berat badan ideal melalui diet seimbang dan olahraga rutin</h4>", unsafe_allow_html=True)
                elif self.usia >= 40 and self.usia < 60:
                    st.markdown(f"<h4 style='text-align: left; '>Tips Usia Menengah : Mulai perhatian pada kesehatan jantung dan keseimbangan berat badan</h4>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<h4 style='text-align: left; '>Tips Usia Lanjut : Fokus pada keseimbangan nutrisi, memperhatikan kesehatan tulang dan menjaga massa otot</h4>", unsafe_allow_html=True)
                
                # Menambahkan catatan untuk perbedaan jenis kelamin
                if self.jenis_kelamin == "Laki-Laki":
                    st.markdown(f"<h4 style='text-align: left; '>Catatan : BMI normal untuk laki-laki adalah 18–25. Laki-laki pada umumnya memiliki massa otot lebih banyak yang bisa mempengaruhi BMI</h4>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<h4 style='text-align: left; '>Catatan : BMI normal untuk perempuan adalah 17–23. Perempuan cenderung memiliki lebih banyak jaringan lemak dibandingkan otot</h4>", unsafe_allow_html=True)
            else:
                st.error("Harap masukkan nilai yang valid untuk berat badan, tinggi badan, usia, dan jenis kelamin anda.") 
