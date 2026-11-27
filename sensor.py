class Sensor:
    def __init__(self, tag: str, value:float, limit: float) -> None:
        self.tag = tag
        self.value = value
        self.limit = limit
    def check (self) -> str: 
        """alarming function"""
        if self.value >= self.limit:
            return f"{self.tag} : Alarm({self.value})"
        return f"{self.tag} : Normal({self.value})"
        

s1 = Sensor("pressire",5.4,4.2)
print (s1.tag, s1.limit)
s1.value =3.2
print (s1.check())

s1.value = 9 
print(s1.check())


