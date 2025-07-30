from gtts import gTTS
from pydub import AudioSegment
import urllib.request


def text_to_speech(teks, output_file):
    """
    Mengubah teks Bahasa Indonesia menjadi suara dan menyimpannya sebagai file MP3.
    
    :param teks: String teks yang akan diubah menjadi suara
    :param output_file: Nama file output (contoh: 'output.mp3')
    """
    tts = gTTS(text=teks, lang='id')
    tts.save(output_file)
    print(f"Berhasil menyimpan file audio: {output_file}")
    

def gabung_mp3(file_list, output_file):
    """
    Menggabungkan beberapa file MP3 menjadi satu file MP3.
    
    :param file_list: List berisi path file MP3 yang ingin digabungkan
    :param output_file: Nama file output hasil gabungan
    """
    if not file_list:
        raise ValueError("Daftar file tidak boleh kosong.")

    # Mulai dengan file pertama
    combined = AudioSegment.from_mp3(file_list[0])

    # Tambahkan file-file berikutnya
    for file_path in file_list[1:]:
        next_audio = AudioSegment.from_mp3(file_path)
        combined += next_audio

    # Ekspor hasil gabungan ke file output
    combined.export(output_file, format="mp3")
    print(f"File MP3 berhasil digabungkan menjadi: {output_file}")

def download_mp3(url, output_file):
    """
    Mengunduh file MP3 dari URL dan menyimpannya sebagai file lokal.
    
    :param url: URL dari file MP3
    :param output_file: Nama file output yang diinginkan (misal: 'lagu.mp3')
    """
    try:
        print(f"Mengunduh dari: {url}")
        urllib.request.urlretrieve(url, output_file)
        print(f"Berhasil disimpan sebagai: {output_file}")
    except Exception as e:
        print(f"Gagal mengunduh file: {e}")

def format_angka(angka, lebar=3):
    """
    Mengubah angka menjadi string dengan padding nol di depan.
    
    :param angka: Angka integer yang ingin diformat
    :param lebar: Jumlah digit total (default 3)
    :return: String dengan nol di depan
    """
    return str(angka).zfill(lebar)

def format_surah_ayat(surah_ayat_str):
    """
    Mengubah input 'surat:ayat' menjadi string 6 digit 'SSSAAA'
    :param surah_ayat_str: String dalam format 'surat:ayat', contoh '21:32'
    :return: String 6 digit, contoh '021032'
    """
    surat, ayat = surah_ayat_str.split(":")
    return f"{int(surat):03}{int(ayat):03}"

if __name__ == "__main__":
    suratayat = input("Masukkan surat:ayat :")
    
    url = f"https://everyayah.com/data/Abu_Bakr_Ash-Shaatree_64kbps/{format_surah_ayat(suratayat)}.mp3"
    download_mp3(url, f"{format_surah_ayat(suratayat)}.mp3")
    
    teks = "Al-maidah"
    text_to_speech(teks, "suara.mp3")

    daftar_file = ['suara.mp3', f'{format_surah_ayat(suratayat)}.mp3']
    gabung_mp3(daftar_file, 'hasil_akhir.mp3')