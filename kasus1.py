kecepatan = float(input("Masukkan kecepatan :"))
if kecepatan <= 10:
    print("Kecepatanmu hanya " , kecepatan ," Sangat Lambat!")
elif kecepatan <= 50:
    print("Kecepatanmu sebesar " , kecepatan ," Cukup Cepat.")
elif kecepatan <= 150:
    print("Kecepatanmu sebesar " , kecepatan ," Cepat Sekali!")
elif kecepatan <= 1000:
    print("Kecepatanmu sangat besar! sebesar " , kecepatan ," Terlalu Cepat!")