from gtts import gTTS
from pydub import AudioSegment
import urllib.request
import sys, os
import argparse

quran_surahs = {
    1:  {"nama": "Al-Fatihah", "jumlah_ayat": 7},
    2:  {"nama": "Al-Baqarah", "jumlah_ayat": 286},
    3:  {"nama": "Ali 'Imran", "jumlah_ayat": 200},
    4:  {"nama": "An-Nisa'", "jumlah_ayat": 176},
    5:  {"nama": "Al-Ma'idah", "jumlah_ayat": 120},
    6:  {"nama": "Al-An'am", "jumlah_ayat": 165},
    7:  {"nama": "Al-A'raf", "jumlah_ayat": 206},
    8:  {"nama": "Al-Anfal", "jumlah_ayat": 75},
    9:  {"nama": "At-Tawbah", "jumlah_ayat": 129},
    10: {"nama": "Yunus", "jumlah_ayat": 109},
    11: {"nama": "Hud", "jumlah_ayat": 123},
    12: {"nama": "Yusuf", "jumlah_ayat": 111},
    13: {"nama": "Ar-Ra'd", "jumlah_ayat": 43},
    14: {"nama": "Ibrahim", "jumlah_ayat": 52},
    15: {"nama": "Al-Hijr", "jumlah_ayat": 99},
    16: {"nama": "An-Nahl", "jumlah_ayat": 128},
    17: {"nama": "Al-Isra'", "jumlah_ayat": 111},
    18: {"nama": "Al-Kahf", "jumlah_ayat": 110},
    19: {"nama": "Maryam", "jumlah_ayat": 98},
    20: {"nama": "Ta-Ha", "jumlah_ayat": 135},
    21: {"nama": "Al-Anbiya'", "jumlah_ayat": 112},
    22: {"nama": "Al-Hajj", "jumlah_ayat": 78},
    23: {"nama": "Al-Mu'minun", "jumlah_ayat": 118},
    24: {"nama": "An-Nur", "jumlah_ayat": 64},
    25: {"nama": "Al-Furqan", "jumlah_ayat": 77},
    26: {"nama": "Asy-Syu'ara'", "jumlah_ayat": 227},
    27: {"nama": "An-Naml", "jumlah_ayat": 93},
    28: {"nama": "Al-Qasas", "jumlah_ayat": 88},
    29: {"nama": "Al-'Ankabut", "jumlah_ayat": 69},
    30: {"nama": "Ar-Rum", "jumlah_ayat": 60},
    31: {"nama": "Luqman", "jumlah_ayat": 34},
    32: {"nama": "As-Sajdah", "jumlah_ayat": 30},
    33: {"nama": "Al-Ahzab", "jumlah_ayat": 73},
    34: {"nama": "Saba'", "jumlah_ayat": 54},
    35: {"nama": "Fatir", "jumlah_ayat": 45},
    36: {"nama": "Ya-Sin", "jumlah_ayat": 83},
    37: {"nama": "As-Saffat", "jumlah_ayat": 182},
    38: {"nama": "Sad", "jumlah_ayat": 88},
    39: {"nama": "Az-Zumar", "jumlah_ayat": 75},
    40: {"nama": "Ghafir", "jumlah_ayat": 85},
    41: {"nama": "Fussilat", "jumlah_ayat": 54},
    42: {"nama": "Asy-Syura", "jumlah_ayat": 53},
    43: {"nama": "Az-Zukhruf", "jumlah_ayat": 89},
    44: {"nama": "Ad-Dukhan", "jumlah_ayat": 59},
    45: {"nama": "Al-Jasiyah", "jumlah_ayat": 37},
    46: {"nama": "Al-Ahqaf", "jumlah_ayat": 35},
    47: {"nama": "Muhammad", "jumlah_ayat": 38},
    48: {"nama": "Al-Fath", "jumlah_ayat": 29},
    49: {"nama": "Al-Hujurat", "jumlah_ayat": 18},
    50: {"nama": "Qaf", "jumlah_ayat": 45},
    51: {"nama": "Adz-Dzariyat", "jumlah_ayat": 60},
    52: {"nama": "At-Tur", "jumlah_ayat": 49},
    53: {"nama": "An-Najm", "jumlah_ayat": 62},
    54: {"nama": "Al-Qamar", "jumlah_ayat": 55},
    55: {"nama": "Ar-Rahman", "jumlah_ayat": 78},
    56: {"nama": "Al-Waqi'ah", "jumlah_ayat": 96},
    57: {"nama": "Al-Hadid", "jumlah_ayat": 29},
    58: {"nama": "Al-Mujadilah", "jumlah_ayat": 22},
    59: {"nama": "Al-Hasyr", "jumlah_ayat": 24},
    60: {"nama": "Al-Mumtahanah", "jumlah_ayat": 13},
    61: {"nama": "As-Saff", "jumlah_ayat": 14},
    62: {"nama": "Al-Jumu'ah", "jumlah_ayat": 11},
    63: {"nama": "Al-Munafiqun", "jumlah_ayat": 11},
    64: {"nama": "At-Taghabun", "jumlah_ayat": 18},
    65: {"nama": "At-Talaq", "jumlah_ayat": 12},
    66: {"nama": "At-Tahrim", "jumlah_ayat": 12},
    67: {"nama": "Al-Mulk", "jumlah_ayat": 30},
    68: {"nama": "Al-Qalam", "jumlah_ayat": 52},
    69: {"nama": "Al-Haqqah", "jumlah_ayat": 52},
    70: {"nama": "Al-Ma'arij", "jumlah_ayat": 44},
    71: {"nama": "Nuh", "jumlah_ayat": 28},
    72: {"nama": "Al-Jinn", "jumlah_ayat": 28},
    73: {"nama": "Al-Muzzammil", "jumlah_ayat": 20},
    74: {"nama": "Al-Muddathir", "jumlah_ayat": 56},
    75: {"nama": "Al-Qiyamah", "jumlah_ayat": 40},
    76: {"nama": "Al-Insan", "jumlah_ayat": 31},
    77: {"nama": "Al-Mursalat", "jumlah_ayat": 50},
    78: {"nama": "An-Naba'", "jumlah_ayat": 40},
    79: {"nama": "An-Nazi'at", "jumlah_ayat": 46},
    80: {"nama": "'Abasa", "jumlah_ayat": 42},
    81: {"nama": "At-Takwir", "jumlah_ayat": 29},
    82: {"nama": "Al-Infitar", "jumlah_ayat": 19},
    83: {"nama": "Al-Mutaffifin", "jumlah_ayat": 36},
    84: {"nama": "Al-Insyiqaq", "jumlah_ayat": 25},
    85: {"nama": "Al-Buruj", "jumlah_ayat": 22},
    86: {"nama": "At-Tariq", "jumlah_ayat": 17},
    87: {"nama": "Al-A'la", "jumlah_ayat": 19},
    88: {"nama": "Al-Ghasyiyah", "jumlah_ayat": 26},
    89: {"nama": "Al-Fajr", "jumlah_ayat": 30},
    90: {"nama": "Al-Balad", "jumlah_ayat": 20},
    91: {"nama": "Asy-Syams", "jumlah_ayat": 15},
    92: {"nama": "Al-Lail", "jumlah_ayat": 21},
    93: {"nama": "Adh-Dhuha", "jumlah_ayat": 11},
    94: {"nama": "Asy-Syarh", "jumlah_ayat": 8},
    95: {"nama": "At-Tin", "jumlah_ayat": 8},
    96: {"nama": "Al-'Alaq", "jumlah_ayat": 19},
    97: {"nama": "Al-Qadr", "jumlah_ayat": 5},
    98: {"nama": "Al-Bayyinah", "jumlah_ayat": 8},
    99: {"nama": "Az-Zalzalah", "jumlah_ayat": 8},
    100: {"nama": "Al-'Adiyat", "jumlah_ayat": 11},
    101: {"nama": "Al-Qari'ah", "jumlah_ayat": 11},
    102: {"nama": "At-Takatsur", "jumlah_ayat": 8},
    103: {"nama": "Al-'Asr", "jumlah_ayat": 3},
    104: {"nama": "Al-Humazah", "jumlah_ayat": 9},
    105: {"nama": "Al-Fil", "jumlah_ayat": 5},
    106: {"nama": "Quraisy", "jumlah_ayat": 4},
    107: {"nama": "Al-Ma'un", "jumlah_ayat": 7},
    108: {"nama": "Al-Kautsar", "jumlah_ayat": 3},
    109: {"nama": "Al-Kafirun", "jumlah_ayat": 6},
    110: {"nama": "An-Nasr", "jumlah_ayat": 3},
    111: {"nama": "Al-Lahab", "jumlah_ayat": 5},
    112: {"nama": "Al-Ikhlas", "jumlah_ayat": 4},
    113: {"nama": "Al-Falaq", "jumlah_ayat": 5},
    114: {"nama": "An-Nas", "jumlah_ayat": 6},
}

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

def cek_ayat_valid(input_str):
    try:
        surat_str, ayat_str = input_str.strip().split(':')
        surat = int(surat_str)
        ayat = int(ayat_str)

        if surat in quran_surahs:
            info = quran_surahs[surat]
            max_ayat = info["jumlah_ayat"]
            if 1 <= ayat <= max_ayat:
                return f"✅ Valid: Surat ke-{surat} ({info['nama']}), ayat ke-{ayat}."
            else:
                print(f"❌ Error: Surat ke-{surat} ({info['nama']}) hanya memiliki {max_ayat} ayat.")
                sys.exit(1)
        else:
            print(f"❌ Error: Surat nomor {surat} tidak ditemukan.")
            sys.exit(1)

    except (ValueError, AttributeError):
        return "❌ Error: Format input harus 'nomor_surat:nomor_ayat', misalnya 20:30"

def satuan():
    suratayat = input("Masukkan surat:ayat :")
    if not suratayat:
        sys.exit(1)
    surat_num, ayat_num = map(int, suratayat.split(':'))
    
    print(cek_ayat_valid(suratayat))
       
    url = f"https://everyayah.com/data/Abu_Bakr_Ash-Shaatree_64kbps/{format_surah_ayat(suratayat)}.mp3"
    download_mp3(url, f"./temp/{format_surah_ayat(suratayat)}.mp3")
    
    teks = f"{quran_surahs[surat_num]['nama']} surat {surat_num} ayat {ayat_num}"
    text_to_speech(teks, "./temp/suara.mp3")

    daftar_file = ['./temp/suara.mp3', f'./temp/{format_surah_ayat(suratayat)}.mp3', f'./terjemahan/{int(surat_num):03}/{format_surah_ayat(suratayat)}Terjemahan.mp3']
    gabung_mp3(daftar_file, f'./temp/_{format_surah_ayat(suratayat)}.mp3')
    os.startfile(f'H:/PYTHON/dl_ayat/temp/_{format_surah_ayat(suratayat)}.mp3')
    
def main():
    parser = argparse.ArgumentParser(description="Format ayat Al-Quran menjadi Audio.")
    group = parser.add_mutually_exclusive_group()

    group.add_argument('--ayat', type=str, help="Satu ayat dalam format SURAT:AYAT (misal 21:32)")
    group.add_argument('--list', nargs='+', help="Daftar beberapa ayat, pisahkan dengan spasi (misal: 2:255 3:7)")
    group.add_argument('--file', type=str, help="File .txt dengan daftar ayat per baris (misal: daftar.txt)")

    parser.add_argument('--output', type=str, default="kode_ayat.txt", help="Nama file output")

    args = parser.parse_args()

    if any(vars(args).values()):
        while True:
            satuan()
        sys.exit(1)
    else:
        if args.ayat:
            print("Ayat nih")
        if args.file:
            print("File")
    
    
if __name__ == "__main__":
    main()
    
    
