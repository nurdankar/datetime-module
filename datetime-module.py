"""Trafiğe çıkış tarihi alınan bir aracın servis zamanı"""

import datetime
tarih= input('Aracınız hangi tarihte trafiğe cıktı ? Lütfen (YYYY/AA/GG) formatında giriniz :')
tarih=tarih.split('/')
trafigeCıkıs=datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2]))   #datetime int bilgi ister
simdi=datetime.datetime.today()
fark=simdi-trafigeCıkıs
days=fark.days                        #Fark değişkeni arasından days bilgisi alınır

if 0<days<=365:
    print('1.Bakım')
elif 366<=days<=365*2:
    print('2.Bakım')
elif (365*2)+1<=days<=365*3:
    print('3.Bakım')
elif (365*3)+1<=days<=365*4:
    print('4.Bakım')
elif (365*4)+1<=days<=365*5:
    print('5.Bakım')
else:
    print('Servis zamanı hesaplanamıyor.')