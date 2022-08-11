class Televisao:
    def __init__(self):
        self.__canal = 0
        self.__volume = 0
        self.__estado = 'Desligado'

    def __str__(self):
        return 'Uma televisão.'

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado):
        self.__estado = estado

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    @property
    def canal(self):
        return self.__canal

    @canal.setter
    def canal(self, canal):
        self.__canal = canal

    def aumentar_volume(self, valor=-1):
        if 0 < valor < 100:
            self.__volume = valor
        else:
            self.__volume += 1
        return print(f'Você esta no volume : {self.__volume}')

    def diminuir_volume(self, valor=None):
        if 0 < valor < 100:
            self.__volume = valor
        else:
            self.__volume -= 1
        return print(f'Você esta no volume : {self.__volume}')

    def aumentar_canal(self, valor=-1):
        if 0 < valor < 100:
            self.__canal = valor
        else:
            self.__canal += 1
        return print(f'Você esta no canal : {self.__canal}')

    def diminuir_canal(self, valor=None):
        if 0 < valor < 100:
            self.__canal = valor
        else:
            self.__canal -= 1
        return print(f'Você esta no canal : {self.__canal}')

    def power(self):
        if self.__estado == 'Desligado':
            self.__estado = 'Ligado'
            return print(f'Tv : {self.estado}')
        else:
            return print(f'Tv : {self.estado}')


class Controle:

    @staticmethod
    def power(t):
        if t.estado == 'Desligado':
            t.estado = 'Ligado'
        else:
            t.estado = 'Desligado'

    @staticmethod
    def aumentar_canal(t, valor=-1):
        return t.aumentar_canal(valor)

    @staticmethod
    def diminuir_canal(t, valor=-1):
        return t.diminuir_canal(valor)

    @staticmethod
    def aumentar_volume(t, valor=-1):
        return t.aumentar_volume(valor)

    @staticmethod
    def diminuir_volume(t, valor=-1):
        return t.diminuir_volume(valor)


tv = Televisao()
controle = Controle()
controle.aumentar_canal(tv, 10)
controle.diminuir_canal(tv)
controle.diminuir_canal(tv, 2)
print(tv.estado)
controle.power(tv)
print(tv.estado)
controle.aumentar_volume(tv, 10)
controle.diminuir_volume(tv)
controle.diminuir_volume(tv, -5)





