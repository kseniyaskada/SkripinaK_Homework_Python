from smartphone import Smartphone

catalog = ([
    Smartphone("Samsung", "S24", "+79998885423"),
    Smartphone("IPhone", "15", "+74443330918"),
    Smartphone("Xiaomi", "14T Pro", "+79618026401"),
    Smartphone("Redmi", "Note 10", "+74490257675"),
    Smartphone("IPhone", "17", "+79910238732")
])

for s in catalog:
    print(s.brand + " - " + s.model + ". " + s.number)
