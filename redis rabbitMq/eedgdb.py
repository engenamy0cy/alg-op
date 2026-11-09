#class - чертеж позволяющий собирать отрибуты и методы
# название класса всегда с бол буквы
class Human:
    def __init__(self,name,age,iq,pe):
        self.name = name
        self.age = age
        self.iq = iq
        self.pe = pe


        
    def walk(self):
        return f"{self.name} двигаеться вперед"
    

    def to_grow_iq(self):
        self.iq -=1
        return f"{self.age} бравл старс какашка {self.name}"


roman = Human("Роман",20,85,"M")
name2 = Human("Баби",20,85,"M")


print(roman.walk())
print(name2.walk())