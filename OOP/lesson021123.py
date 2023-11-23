class Building :

    def __init__(self, name, address, floors):
        self.name = name
        self.address = address
        self.floors = floors


    def greeting(self):
        print(f"Zdanie2 {self.name}")


    def __str__(self):
        return f"Здание {self.name}, адрес {self.address}, этажей { self.floors} "


class BussinessCentr(Building):
    def __init__(self, name, address, floors, staff):
        super().__init__(name, address, floors)

        self.staff = staff

    def __str__(self):
        return f"{super().__str__()} Здесь работает персонал { self.staff} человек  "


# muit = Building(name="MUIT", address="Manasa 94", floors=10)
alatau = BussinessCentr(name="Alatau",address="abaya roz", floors= 15, staff=40)

alatau.greeting()
print(alatau)