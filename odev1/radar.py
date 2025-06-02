import random

class Radar:
    def __init__(self):
        self.koordinat = (0, 0, 0)
        self.asker = 0
        self.tank = 0
        self.ucak = 0
        self.hedef = (0, 0, 0)

    def ucak_goruldu(self):
        self.ucak += 1

    def ucak_imha_edildi(self):
        self.ucak -= 1

    def tank_goruldu(self):
        self.tank += 1

    def tank_imha_edildi(self):
        self.tank -= 1

    def asker_goruldu(self):
        self.asker += 1

    def asker_imha_edildi(self):
        self.asker -= 1

    def koordinat_tarama(self):
        cisim = random.randint(1, 9)
        koord = (random.randint(0, 100), random.randint(0, 100), random.randint(0, 20))

        if 3 < cisim < 6:
            print('')
            print('!!!! DİKKAT DİKKAT DİKKAT !!!!')
            print(f' {koord} koordinatta düşman UÇAĞI tespit edildi')
            print('!!!! ------- DİKKAT DİKKAT DİKKAT -------!!!!')
            print('')
            self.ucak_goruldu()
            self.hedef = koord
        elif 1 < cisim < 3:
            print('')
            print('!!!! DİKKAT DİKKAT DİKKAT !!!!')
            print(f' {koord} koordinatta düşman TANKI tespit edildi')
            print('!!!! ------- DİKKAT DİKKAT DİKKAT -------!!!!')
            print('')
            self.tank_goruldu()
            self.hedef = koord
        elif 5 < cisim < 7:
            print('')
            print('!!!! DİKKAT DİKKAT DİKKAT !!!!')
            print(f' {koord} koordinatta düşman Askeri tespit edildi')
            print('!!!! ------- DİKKAT DİKKAT DİKKAT -------!!!!')
            print('')
            self.asker_goruldu()
            self.hedef = koord
        else:
            print(f'{koord} temiz')
            return 0
        return cisim

