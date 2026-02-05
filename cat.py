# definisikan class NamaClass
class Cat:
    # __init__ = constructor = yang pertama kali di akses
    # definisikan atribute di dalam constructor
    def __init__(self, color, height, width):
        # set parameter ke self
        self.color = color
        self.height = height
        self.width = width

# buat objek dari class Cat
garfield = Cat("Orange", 25, 10)
persia = Cat("White", 20, 8)
# cek objek di memory kita, muncul address 0x1*********
print("Obj Garfield", garfield)
print("Obj Persia", persia)
# panggil nama atribute dari objek
print(f"Warna persia: {persia.color}")
print(f"Tinggi persia: {persia.height}")
print(f"Lebar persia: {persia.width}")