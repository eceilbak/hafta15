from radar import Radar
from ucak import Ucak, Ucak_Filosu
from sorti import Sorti
import time
u1=Ucak('001','F16')
u2=Ucak('002','F16')
u3=Ucak('003','F16')
u4=Ucak('004','F16')
u5=Ucak('005','F16')
v1=Ucak('010','F22')
v2=Ucak('011','F22')
v3=Ucak('012','F22')
v4=Ucak('013','F22')
v5=Ucak('014','F22')
k=Ucak('s0001','siha')
l=Ucak('s0002','siha')
m=Ucak('s0003','siha')
n=Ucak('s0004','siha')

filo=Ucak_Filosu()
filo.Ucak_Filosuna_Ekle(u1)
filo.Ucak_Filosuna_Ekle(u2)
filo.Ucak_Filosuna_Ekle(u3)
filo.Ucak_Filosuna_Ekle(u4)
filo.Ucak_Filosuna_Ekle(u5)
filo.Ucak_Filosuna_Ekle(v1)
filo.Ucak_Filosuna_Ekle(v2)
filo.Ucak_Filosuna_Ekle(v3)
filo.Ucak_Filosuna_Ekle(v4)
filo.Ucak_Filosuna_Ekle(v5)
filo.Ucak_Filosuna_Ekle(k)
filo.Ucak_Filosuna_Ekle(l)
filo.Ucak_Filosuna_Ekle(m)
filo.Ucak_Filosuna_Ekle(n)

kazanilan=0
kaybedilen=0
while True:
    t1=Radar()
    tarama=t1.koordinat_tarama()
    print('-----------------------------')
    print('kazanılan :{}     kaybedilen :{}'.format(kazanilan,kaybedilen))
    print('-----------------------------')
    if kazanilan==5 or kaybedilen==5:
        galip=max(kazanilan,kaybedilen)
        print('savaş bitti ')
        if galip==kazanilan:
            print('Oley !!!  savaşı Kazandık')
            print('Tebrikler Komutan GENERALliğe Terfi Oldun.')
            kazanilan+=1
        else :
            print('Maalesef Savaşı Kaybettik.')
            kaybedilen+=1
        break
    else:
        if tarama>0:
            print('hedeflerin imhası için koordinatlar merkeze gönderiliyor')
            hdf = t1.hedef
            imh = Sorti('imha01', u1, hdf)
            time.sleep(1)
            scr=imh.hedefi_imha_et()
            if str(scr)=='1':
                kazanilan += 1
            else:
                kaybedilen+=1
            time.sleep(1)
        else:
            print('...diğer bölgeler taranılıyor.....')
            time.sleep(1)
