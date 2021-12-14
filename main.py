class Ricecooker:
 def __init__(self,nama_merk,Tuas,panci,Mode):
    self.nama_merk = nama_merk
    self.Tuas = Tuas
    self.panci = panci
    self.Mode = Mode
    self._activatedtemperature = None
    print(f'data ricecooker {self.nama_merk} dibuat')

 def __del__(self):
      print(f'data ricecooker {self.nama_merk} dihapus')
#Membuat data ricecooker kost
print('DATA RICECOOKER KOST')
kost = Ricecooker('Young Ma', 'memasak', 'terisi', 5)

del kost
print('__________________________________')
#Membuat data ricecooker dapur
print('DATA RICECOOKER DAPUR')
dapur = Ricecooker('Cosmos', 'menghagatkan', 'terisi', 6)

del dapur
