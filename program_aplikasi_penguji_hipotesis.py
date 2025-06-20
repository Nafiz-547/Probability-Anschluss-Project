# -*- coding: utf-8 -*-
"""Program_Aplikasi_Penguji_Hipotesis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/Nafiz-547/Nafiz-1stProject/blob/main/Program_Aplikasi_Penguji_Hipotesis.ipynb
"""

import scipy.stats as stats
import numpy as np

def hypothesis_test():
    """Performs a hypothesis test based on user input."""
    print("Selamat datang di program Uji Hipotesis!")

    # input dari pengguna
    test_type = input("Pilih jenis uji (satu-sampel, dua-sampel independen, berpasangan): ").lower()

    if test_type == "satu-sampel":
        print("\n--- Uji Satu Sampel ---")
        data = list(map(float, input("Masukkan data sampel (pisahkan dengan koma): ").split(',')))
        null_hypothesis_mean = float(input("Masukkan nilai rata-rata hipotesis nol (H0): "))
        alpha = float(input("Masukkan tingkat signifikansi (alpha, cth: 0.05): "))
        tail_type = input("Pilih jenis ekor uji (dua-ekor, ekor-kanan, ekor-kiri): ").lower()

        # uji t satu sampel
        t_statistic, p_value = stats.ttest_1samp(data, null_hypothesis_mean)

        print(f"\nStatistik Uji t: {t_statistic}")
        print(f"Nilai p (p-value): {p_value}")

        # Ambil keputusan
        print("\n--- Keputusan ---")
        if tail_type == "dua-ekor":
            if p_value < alpha:
                print(f"Karena nilai p ({p_value}) < alpha ({alpha}), tolak hipotesis nol (H0). Ada bukti yang cukup untuk mendukung hipotesis alternatif (Ha).")
            else:
                print(f"Karena nilai p ({p_value}) >= alpha ({alpha}), gagal menolak hipotesis nol (H0). Tidak ada bukti yang cukup untuk mendukung hipotesis alternatif (Ha).")
        elif tail_type == "ekor-kanan":
             if p_value / 2 < alpha and t_statistic > 0:
                print(f"Karena nilai p/2 ({p_value/2}) < alpha ({alpha}) dan statistik t positif, tolak hipotesis nol (H0). Ada bukti yang cukup untuk mendukung hipotesis alternatif (Ha).")
             else:
                print(f"Karena nilai p/2 ({p_value/2}) >= alpha ({alpha}) atau statistik t tidak positif, gagal menolak hipotesis nol (H0). Tidak ada bukti yang cukup untuk mendukung hipotesis alternatif (Ha).")
        elif tail_type == "ekor-kiri":
             if p_value / 2 < alpha and t_statistic < 0:
                print(f"Karena nilai p/2 ({p_value/2}) < alpha ({alpha}) dan statistik t negatif, tolak hipotesis nol (H0). Ada bukti yang cukup untuk mendukung hipotesis alternatif (Ha).")
             else:
                print(f"Karena nilai p/2 ({p_value/2}) >= alpha ({alpha}) atau statistik t tidak negatif, gagal menolak hipotesis nol (H0). Tidak ada bukti yang cukup untuk mendukung hipotesis alternatif (Ha).")
        else:
            print("Jenis ekor uji tidak valid.")

    elif test_type == "dua-sampel independen":
        print("\n--- Uji Dua Sampel Independen ---")
        data1 = list(map(float, input("Masukkan data sampel 1 (pisahkan dengan koma): ").split(',')))
        data2 = list(map(float, input("Masukkan data sampel 2 (pisahkan dengan koma): ").split(',')))
        alpha = float(input("Masukkan tingkat signifikansi (alpha, cth: 0.05): "))
        equal_var = input("Asumsikan variansi sama? (ya/tidak): ").lower() == 'ya'
        tail_type = input("Pilih jenis ekor uji (dua-ekor, ekor-kanan, ekor-kiri): ").lower()


        # uji t dua sampel independen
        t_statistic, p_value = stats.ttest_ind(data1, data2, equal_var=equal_var)

        print(f"\nStatistik Uji t: {t_statistic}")
        print(f"Nilai p (p-value): {p_value}")

        # Ambil keputusan
        print("\n--- Keputusan ---")
        if tail_type == "dua-ekor":
            if p_value < alpha:
                print(f"Karena nilai p ({p_value}) < alpha ({alpha}), tolak hipotesis nol (H0). Ada bukti yang cukup bahwa rata-rata populasi dari kedua sampel berbeda.")
            else:
                print(f"Karena nilai p ({p_value}) >= alpha ({alpha}), gagal menolak hipotesis nol (H0). Tidak ada bukti yang cukup bahwa rata-rata populasi dari kedua sampel berbeda.")
        elif tail_type == "ekor-kanan":
             if p_value / 2 < alpha and t_statistic > 0:
                 print(f"Karena nilai p/2 ({p_value/2}) < alpha ({alpha}) dan statistik t positif, tolak hipotesis nol (H0). Ada bukti yang cukup bahwa rata-rata populasi sampel 1 lebih besar dari sampel 2.")
             else:
                 print(f"Karena nilai p/2 ({p_value/2}) >= alpha ({alpha}) atau statistik t tidak positif, gagal menolak hipotesis nol (H0). Tidak ada bukti yang cukup bahwa rata-rata populasi sampel 1 lebih besar dari sampel 2.")
        elif tail_type == "ekor-kiri":
             if p_value / 2 < alpha and t_statistic < 0:
                 print(f"Karena nilai p/2 ({p_value/2}) < alpha ({alpha}) dan statistik t negatif, tolak hipotesis nol (H0). Ada bukti yang cukup bahwa rata-rata populasi sampel 1 lebih kecil dari sampel 2.")
             else:
                 print(f"Karena nilai p/2 ({p_value/2}) >= alpha ({alpha}) atau statistik t tidak negatif, gagal menolak hipotesis nol (H0). Tidak ada bukti yang cukup bahwa rata-rata populasi sampel 1 lebih kecil dari sampel 2.")
        else:
            print("Jenis ekor uji tidak valid.")


    elif test_type == "berpasangan":
        print("\n--- Uji Sampel Berpasangan ---")
        data1 = list(map(float, input("Masukkan data sampel 1 (sebelum - pisahkan dengan koma): ").split(',')))
        data2 = list(map(float, input("Masukkan data sampel 2 (setelah - pisahkan dengan koma): ").split(',')))
        alpha = float(input("Masukkan tingkat signifikansi (alpha, cth: 0.05): "))
        tail_type = input("Pilih jenis ekor uji (dua-ekor, ekor-kanan, ekor-kiri): ").lower()

        if len(data1) != len(data2):
            print("Error: Jumlah data pada kedua sampel harus sama untuk uji berpasangan.")
            return

        # uji t sampel berpasangan
        t_statistic, p_value = stats.ttest_rel(data1, data2)

        print(f"\nStatistik Uji t: {t_statistic}")
        print(f"Nilai p (p-value): {p_value}")

        # Ambil keputusan
        print("\n--- Keputusan ---")
        if tail_type == "dua-ekor":
            if p_value < alpha:
                print(f"Karena nilai p ({p_value}) < alpha ({alpha}), tolak hipotesis nol (H0). Ada bukti yang cukup bahwa terdapat perbedaan signifikan antara rata-rata sebelum dan setelah.")
            else:
                print(f"Karena nilai p ({p_value}) >= alpha ({alpha}), gagal menolak hipotesis nol (H0). Tidak ada bukti yang cukup bahwa terdapat perbedaan signifikan antara rata-rata sebelum dan setelah.")
        elif tail_type == "ekor-kanan":
             if p_value / 2 < alpha and t_statistic > 0:
                 print(f"Karena nilai p/2 ({p_value/2}) < alpha ({alpha}) dan statistik t positif, tolak hipotesis nol (H0). Ada bukti yang cukup bahwa rata-rata 'setelah' lebih besar dari 'sebelum'.")
             else:
                 print(f"Karena nilai p/2 ({p_value/2}) >= alpha ({alpha}) atau statistik t tidak positif, gagal menolak hipotesis nol (H0). Tidak ada bukti yang cukup bahwa rata-rata 'setelah' lebih besar dari 'sebelum'.")
        elif tail_type == "ekor-kiri":
             if p_value / 2 < alpha and t_statistic < 0:
                 print(f"Karena nilai p/2 ({p_value/2}) < alpha ({alpha}) dan statistik t negatif, tolak hipotesis nol (H0). Ada bukti yang cukup bahwa rata-rata 'setelah' lebih kecil dari 'sebelum'.")
             else:
                 print(f"Karena nilai p/2 ({p_value/2}) >= alpha ({alpha}) atau statistik t tidak negatif, gagal menolak hipotesis nol (H0). Tidak ada bukti yang cukup bahwa rata-rata 'setelah' lebih kecil dari 'sebelum'.")
        else:
            print("Jenis ekor uji tidak valid.")

    else:
        print("Jenis uji tidak valid. Pilih 'satu-sampel', 'dua-sampel independen', atau 'berpasangan'.")

# Menjalankan program
hypothesis_test()