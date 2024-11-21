jadwal = {
    'senin': {1: [], 2: [], 3: [], 4: []},
    'selasa': {1: [], 2: [], 3: [], 4: []},
    'rabu': {1: [], 2: [], 3: [], 4: []},
    'kamis': {1: [], 2: [], 3: [], 4: []},
    'jumat': {1: [], 2: [], 3: [], 4: []},
    'sabtu': {1: [], 2: [], 3: [], 4: []},
    'minggu': {1: [], 2: [], 3: [], 4: []},
}
peralatan = {
    'Raket': 50,
    'Shuttlecock': 50,
}
pesanan = []
waiting_list = []
untung = {day: 0 for day in jadwal}
sesi_jam = {
    1: (6, 8),
    2: (8, 10),
    3: (10, 12),
    4: (12, 14),
    5: (14, 16),
    6: (16, 18),
    7: (18, 20),
    8: (20, 22),
}
def Waiting_list():
    if waiting_list == []:
        return "Tidak ada waiting list"
    
    print(f'Daftar waiting list: {waiting_list}')
    for wait in waiting_list[:]:
        print(f'Apakah waiting list {wait} akan difollow up?')
        x = input("masukkan inputan Y/N").upper()
        if x == 'N':
            print(f'Waiting list {wait} membatalkan pemesanan')
            waiting_list.remove(wait)
            return
        elif x == 'Y':
            print("Pilih hari:")
            for i, day in enumerate(jadwal.keys(), 1):
                print(f'{i}. {day.capitalize()}')

            hari_pilihan = int(input('\nMasukkan nomor: '))
            hari_keys = list(jadwal.keys())

            if hari_pilihan < 1 or hari_pilihan > len(hari_keys):
                print("Pilihan hari tidak valid. ")
                return
            
            hari_terpilih = hari_keys[ hari_pilihan-1 ]

            print('\nPilih lapangan yang tersedia: ')
            for lapangan in range(1,5):
                print(f'Lapangan {lapangan}')

            lapangan_pilihan = int(input('\nMasukkan nomor lapangan yang ingin di pesan: '))
            if lapangan_pilihan not in jadwal[hari_terpilih]:
                print('Pilihan lapangan tidak valid')
                return
            for waktu in jadwal[hari_terpilih][lapangan_pilihan]:
                if not (wait[2] <= waktu[0] or wait[1] >= waktu[1]):
                    print("Jadwal bentrok dengan reservasi lain di lapangan ini!")  
                    return
            harga_per_sesi = 50000
            jadwal[hari_terpilih][lapangan_pilihan].append((wait[1],wait[2]))
            waiting_list.remove(wait)
            print(f'Reservasi atas nama {wait[0]}, berhasil ditambahkan pada hari {hari_terpilih} di lapnagan {lapangan_pilihan} pada pukul {wait[1]}:00 - {wait[2]}:00')

def tambah_reservasi():
    global harga_per_sesi
    global hari_terpilih

    print("\nReservasi Lapangan Bulu Tangkis")
    nama = input("Masukkan Nama Pemesan Lapangan: ")
    print("Pilih hari:")
    for i, day in enumerate(jadwal.keys(), 1):
        print(f"{i}. {day.capitalize()}")

    hari_pilihan = int(input('\nMasukkan nomor: '))
    hari_keys = list(jadwal.keys())

    if hari_pilihan < 1 or hari_pilihan > len(hari_keys):
        print("Pilihan hari tidak valid. ")
        return
    hari_terpilih = hari_keys[ hari_pilihan-1 ]
    print("\nPilih sesi waktu yang tersedia:")
    for nomor, waktu in sesi_jam.items():
        print(f'{nomor}. {waktu[0]}:00 - {waktu[1]}:00')

    sesi_pilihan = int(input("\nMasukkan nomor sesi waktu yang ingin Anda pesan: "))
    if sesi_pilihan not in sesi_jam:
            print("Pilihan waktu tidak valid.")
            return
    waktu_mulai, waktu_selesai = sesi_jam[sesi_pilihan]

    print('\nPilih lapangan yang tersedia: ')
    for lapangan in range(1,5):
        print(f'Lapangan {lapangan}')

    lapangan_pilihan = int(input('\nMasukkan nomor lapangan yang ingin di pesan: '))
    if lapangan_pilihan not in jadwal[hari_terpilih]:
        print('Pilihan lapangan tidak valid')
        return
    for waktu in jadwal[hari_terpilih][lapangan_pilihan]:
        if not (waktu_selesai <= waktu[0] or waktu_mulai >= waktu[1]):
            print("Jadwal bentrok dengan reservasi lain di lapangan ini!")  
            x = input("Apakah jadwal akan dipindahkan ke hari lain Y/N: ").upper()
            if x == 'Y':
                waiting_list.append((nama, waktu_mulai, waktu_selesai))
                print(f'Pesanan pada hari {hari_terpilih} pada pukul {waktu_mulai}:00 - {waktu_selesai}:00 untuk lapangan {lapangan_pilihan} masuk kedalam waiting list')
                return
            elif x == "N":
                print("Pesanan dibatalkan")
                return
    harga_per_sesi = 50000
    jadwal[hari_terpilih][lapangan_pilihan].append((waktu_mulai,waktu_selesai))
    untung[hari_terpilih] += harga_per_sesi  # Tambahkan keuntungan untuk hari yang bersangkutan
    print(f'Reservasi atas nama {nama}, berhasil ditambahkan pada hari {hari_terpilih} di lapangan {lapangan_pilihan} pada pukul {waktu_mulai}:00 - {waktu_selesai}:00')

def peminjam_barang():
    global untung
    print("\nDaftar Barang yang Tersedia:")
    for item, stok in peralatan.items():
        print(f"{item}: {stok} unit")
    
    input_pengguna = input("\nPilih barang yang ingin dipinjam: ").capitalize()
    if input_pengguna in peralatan:
        if input_pengguna == 'Raket':
            harga_per_jam = 10000
        elif input_pengguna == 'Shuttlecock':
            harga_per_jam = 5000
        else:
            print("Barang tidak valid!")
            return
        
        jumlah = int(input(f'Masukkan jumlah {input_pengguna} yang ingin dipinjam: '))
        waktu = int(input(f'Masukkan jumlah waktu peminjaman (jam): '))

        if jumlah > peralatan[input_pengguna]:
            print(f"Maaf, stok tidak mencukupi. Stok tersedia: {peralatan[input_pengguna]} unit.")
            return

        total_harga = jumlah * harga_per_jam * waktu
        peralatan[input_pengguna] -= jumlah
        pesanan.append((input_pengguna, jumlah, waktu, total_harga))

        hari_terpilih = input("Masukkan hari peminjaman: ").lower()
        if hari_terpilih in untung:
            untung[hari_terpilih] += total_harga

        print(f"\nPesanan berhasil! Total harga: Rp{total_harga}")
        print(f"Stok {input_pengguna} tersisa: {peralatan[input_pengguna]} unit")

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
def sort_and_display():
    print("Jadwal Pemakaian Lapangan:")
    print("=" * 40)
    for hari in jadwal:
        jadwal_harian = [] 
        for lapangan, jam in jadwal[hari].items():
            if jam:
                bubble_sort(jam)
                for waktu in jam:
                    jadwal_harian.append((waktu, lapangan))
        bubble_sort(jadwal_harian)  

        if jadwal_harian:
            print(f"{hari.capitalize()}:")
            for waktu, lapangan in jadwal_harian:
                waktu_str = f"{waktu[0]}:00 - {waktu[1]}:00"
                print(f"  Lapangan {lapangan}: {waktu_str}")
        else:
            print(f"{hari.capitalize()}: Tidak ada jadwal")
        print("-" * 40)

def perhitungan_untung():   # done
    print("Apakah shift hari ini sudah selesai? (Y/N)")
    selesai = input("Masukkan pilihan: ").strip().upper()
    if selesai == "Y":
        print("Ingin cek keuntungan Harian (H) atau Mingguan (M)?")
        pilihan = input("Masukkan pilihan: ").strip().upper()

        if pilihan == "H":
            hari_terpilih = input("Masukkan shift hari ini: ").lower()
            if hari_terpilih not in jadwal:
                print("Hari tidak valid.")
                return
            print(f"Keuntungan hari {hari_terpilih.capitalize()}: Rp{untung[hari_terpilih]}")
        elif pilihan == "M":
            total_untung = sum(untung.values())
            print(f"Total keuntungan mingguan: Rp{total_untung}")
        else:
            print("Pilihan tidak valid.")

while True:
    print("\nMenu Reservasi Lapangan Bulu Tangkis: ")
    print("1. Cek Waiting List")
    print("2. Reservasi Lapangan")
    print("3. Peminjaman Raket")
    print("4. Tampilkan Jadwal")
    print("5. Perhitungan keuntungan dan keluar")

    pilihan = int(input("\nPilih opsi (nomor): "))
    if pilihan == 1:
        print(Waiting_list())
    elif pilihan == 2:
        tambah_reservasi()
    elif pilihan == 3:
        peminjam_barang()
    elif pilihan == 4:
        sort_and_display()
    elif pilihan == 5:
        print('Apakah shift sudah selesai? ')
        jawab = (input("N/Y: ")).upper()
        if jawab == 'Y':
            perhitungan_untung()
            break
        elif jawab == 'N':
            print("Belum bisa menghitung keuntungan")
    else:
        print("Opsi tidak valid. Silakan pilih nomor antara 1-5.")
