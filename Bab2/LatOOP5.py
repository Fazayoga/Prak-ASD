from LatOOP4 import Mahasiswa

class MhsTIF(Mahasiswa):
    """Class MhsTIF yang dibangun dari class Mahasiswa"""
    def katakanPy(self):
        print('Python is cool')

m4 = MhsTIF('Faza Yoga','L200210011','Surakarta', 230000)
m4.katakanPy()
print(m4)
print(m4.keadaan)
print(m4.makan('Pecel'))
print(m4.keadaan)
m4.ucapkanSalam()
