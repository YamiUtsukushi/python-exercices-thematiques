class CarnetContacts:
    def __init__(self):
        self._contacts = []

    def ajouter(self, nom):
        self._contacts.append(nom)

    def __len__(self):
        return len(self._contacts)

    def __getitem__(self, index):
        return self._contacts[index]

    def __contains__(self, nom):
        return nom in self._contacts

    def __str__(self):
        return "Carnet: " + ", ".join(self._contacts)


carnet = CarnetContacts()
carnet.ajouter("Alice")
carnet.ajouter("Bob")

print(len(carnet))       # 2
print("Alice" in carnet) # True
print(carnet[0])         # Alice
print(carnet)            # Carnet: Alice, Bob
