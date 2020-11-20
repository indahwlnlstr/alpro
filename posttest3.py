print("HALLO SELAMAT DATANG")
print("Ditoko Kue Sule")
print("NO            Kue         Pembelian         Diskon")
print(66 * "-")
print("1.        Kue Coklat       5-20biji            7%  ")
print("2.        Kue Coklat      21-35biji            12% ")
print("3.        Kue Keju         4-15biji            10% ")
print("4.        Kue Keju        16-25biji            15% ")
print(66 * "-")
print()
def print_menu():
    print(30 * "-", "MENU", 30*"-")
    print("1. Kue Coklat")
    print("2. Kue Keju")

print_menu()
stok_keju =[25]
stok_coklat = [35]

pilihan = int(input("Masukkan Pilihan = "))
if pilihan == 1:
    jumlah = int(input("Masukkan Jumlah Kue: ")) 
    harga = 3500

    if jumlah <=4:
        total = harga*jumlah
        print("Total Pembayaran = Rp ",total)
        print("Anda Tidak Mendapat Diskon Karena pembelian di Bawah 5")

        stok_baru = stok_coklat[0] - jumlah
        stok_coklat.pop(0)
        stok_coklat.insert(0, stok_baru)
        print("Sisa stok kami: ", stok_coklat)

    elif jumlah >=5 and jumlah <=20:
        total = harga*jumlah
        diskon = total*7/100
        pembayaran = total-diskon
        print("total harga sebelum diskon = Rp.",total)
        print("Anda Mendapat Diskon 7%")
        print("Total Pembayaran = Rp.", pembayaran)

        stok_baru = stok_coklat[0] - jumlah
        stok_coklat.pop(0)
        stok_coklat.insert(0, stok_baru)
        print("Sisa stok kami: ", stok_coklat)

    elif jumlah >=21 and jumlah <=35:
        total = harga*jumlah
        diskon = total*12/100
        pembayaran = total-diskon
        print("Total Harga Sebelum Diskon Rp.",total)
        print("Anda Mendapat Diskon 12%")
        print("Total Pembayaran = Rp. ", pembayaran)

        stok_baru = stok_coklat[0] - jumlah
        stok_coklat.pop(0)
        stok_coklat.insert(0, stok_baru)
        print("Sisa stok kami: ", stok_coklat)

    else:
        print("Mohon maaf pesanan anda melebihi stok, stok kami terbatas hanya 35")

elif pilihan == 2:
    jumlah = int(input("Masukkan Jumlah Kue : ")) 
    harga = 6000
    if jumlah <=4:
        total = harga*jumlah
        print("total yang harus di bayar = Rp ",total)
        print("Anda Tidak Mnedapat Diskon Karena pembelian di bawah 4")

        stok_baru = stok_keju[0] - jumlah
        stok_keju.pop(0)
        stok_keju.insert(0, stok_baru)
        print("Sisa stok kami: ", stok_keju)

    elif jumlah >=5 and jumlah <=15:
        total = harga*jumlah
        diskon = total*10/100
        pembayaran = total-diskon
        print("total harga sebelum diskon Rp.",total)
        print("Anda Mendapat Diskon 10%")
        print("total yang harus di bayar = Rp.", pembayaran)

        stok_baru = stok_keju[0] - jumlah
        stok_keju.pop(0)
        stok_keju.insert(0, stok_baru)
        print("Sisa stok kami: ", stok_keju)

    elif jumlah >=16 and jumlah <=25:
        total = harga*jumlah
        diskon = total*15/100
        pembayaran = total-diskon
        print("total harga sebelum diskon Rp.",total)
        print("Anda Mendapat Diskon 15%")
        print("total yang harus di bayar = Rp.", pembayaran)

        stok_baru = stok_keju[0] - jumlah
        stok_keju.pop(0)
        stok_keju.insert(0, stok_baru)
        print("Sisa stok kami: ", stok_keju)

    elif jumlah >=16 and jumlah <=25:
        total = harga*jumlah
        diskon = total*15/100
        pembayaran = total-diskon
        print("total harga sebelum diskon Rp.",total)
        print("Anda Mendapat Diskon 15%")
        print("total yang harus di bayar = Rp.", pembayaran)

        stok_baru = stok_keju[0] - jumlah
        stok_keju.pop(0)
        stok_keju.insert(0, stok_baru)
        print("Sisa stok kami: ", stok_keju)
    else:
        print("Mohon maaf pesanan anda melebihi stok, stok kami terbatas hanya 25")
                
print(28 * "-","TERIMAKASIH", 28* "-")
print("Selamat Menikmati Kue Kami")
print("Jangan Lupa Datang Kembali Ke Toko Kami")