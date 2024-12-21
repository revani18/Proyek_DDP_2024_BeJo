import streamlit as st
import pandas as pd

# Class untuk menyimpan dan menampilkan jadwal olahraga
class JadwalOlahraga:
    def __init__(self, nama):
        self.nama = nama
        self.jadwal = {hari: [] for hari in ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]}

    def set_jadwal(self, hari, olahraga, durasi):
        """Menambahkan olahraga dan durasi ke jadwal untuk hari tertentu"""
        self.jadwal[hari].append((olahraga, durasi))

    def tampilkan_jadwal(self):
        """Mengembalikan jadwal dalam bentuk DataFrame"""
        jadwal_flat = []
        for hari, aktivitas in self.jadwal.items():
            for olahraga, durasi in aktivitas:
                jadwal_flat.append([hari, olahraga, f"{durasi} menit"])
        return pd.DataFrame(jadwal_flat, columns=["Hari", "Olahraga", "Durasi"])

# Fungsi untuk menghitung total durasi olahraga dalam seminggu
def hitung_total_durasi(jadwal):
    total_durasi = 0
    for aktivitas in jadwal.values():
        for olahraga, durasi in aktivitas:
            total_durasi += durasi
    return total_durasi

# Fungsi utama untuk menjalankan aplikasi
def show():
    st.markdown(f"<h1 style='text-align: center; color: #0077B6;'>Aplikasi Perencanaan Jadwal Olahraga Mingguan</h1>", unsafe_allow_html=True)
    st.markdown("---")

    olahraga_options = ["Jogging", "Bersepeda", "Yoga", "Angkat Beban", "Renang", "Zumba", "Pilates"]
    nama = st.text_input("Masukkan Nama Anda:")

    if nama:
        # Membuat objek jadwal olahraga untuk pengguna
        jadwal = JadwalOlahraga(nama)

        # Mengambil input untuk setiap hari dalam seminggu
        for hari in ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]:
            st.subheader(f"{hari}")
            olahraga_pilihan = st.multiselect(f"Pilih olahraga untuk {hari}:", olahraga_options)
            for olahraga in olahraga_pilihan:
                durasi = st.number_input(f"Durasi (dalam menit) untuk {olahraga} pada {hari}:", min_value=1, step=1)
                if durasi > 0:
                    jadwal.set_jadwal(hari, olahraga, durasi)

        # Tombol untuk menampilkan jadwal di tab yang sama
        if st.button("Tampilkan Jadwal Olahraga"):
        
            # Menampilkan jadwal
            st.write("### Jadwal Olahraga Anda")
            st.table(jadwal.tampilkan_jadwal())

            # Menghitung total durasi
            total_durasi = hitung_total_durasi(jadwal.jadwal)
            st.write(f"**Total durasi olahraga dalam seminggu: {total_durasi} menit**")

            # Feedback berdasarkan jumlah olahraga yang dipilih
            total_olahraga = sum(len(aktivitas) for aktivitas in jadwal.jadwal.values())
            if total_olahraga >= 7:
                st.success("Hebat! Anda merencanakan olahraga untuk setiap hari!")
            elif total_olahraga >= 4:
                st.warning("Bagus, tapi Anda bisa lebih konsisten!")
            else:
                st.info("Cobalah untuk merencanakan lebih banyak olahraga!")

            # Operator dan While Loop untuk motivasi
            motivasi = ["Terus semangat!", "Konsistensi adalah kunci!", "Jangan lupa istirahat yang cukup!"]
            idx = 0
            while idx < len(motivasi):
                st.write(motivasi[idx])
                idx += 1
        
    else:
        st.warning("Masukkan nama Anda terlebih dahulu.")

# Menjalankan aplikasi
if __name__ == "__main__":
    show()
