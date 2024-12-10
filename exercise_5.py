import gc

class PetsOwner:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

class Child(PetsOwner):
    def __init__(self, firstname, lastname, age, countOfPets):
        PetsOwner.__init__(self, firstname, lastname)
        self.age = age
        self.countOfPets = countOfPets

    def prInfoOfChild(self):
        print("Child's name is", self.firstname, "and lastname is", self.lastname, ".")
        if (self.countOfPets == 1):
            print("The child is", self.age, "years old and has", self.countOfPets, "pet.")
        else:
            print("The child is only", self.age, "years old and already has", self.countOfPets, "pets.")
        print("- " * 27)

class Adult:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def countOfChildsMethod(self, firstname, childsCount, petsCount):
        print("In ", firstname + "'s family are ",childsCount, "children and", petsCount, "pets.")

child1 = Child("Ilze", "Saulīte", 14, 1)
child1.prInfoOfChild() # tiek izsaukta klases Child metode "prInfoOfChild()"
child2 = Child("Roberts", "Saulīte", 13, 2)
child2.prInfoOfChild() # tiek izsaukta klases Child metode "prInfoOfChild()"
child3 = Child("Gustavs", "Mēnestiņš", 17, 2)
child4 = Child("Mareks", "Zvaigznīte", 16, 2)
adult1 = Adult("Baiba", "Saulīte")
adult2 = Adult("Ronijs", "Zvaigznīte")

# metode kas saliek sarakstā objektus no klases Child:
def get_all_childs(Child): 
    childs_instances = []
    for obj in gc.get_objects(): #gc.get_objects - atgriež visus objektus
        if isinstance(obj, Child): #isinstance - pārbauda, vai objekts pieder klasei Child
            childs_instances.append(obj)
            
    return childs_instances
all_childs = get_all_childs(Child)

# metode kas saliek sarakstā objektus no klases Adult:
def get_all_adults(Adult): 
    adults__instances = []
    for obj in gc.get_objects():
        if isinstance(obj, Adult):
            adults__instances.append(obj)
    return adults__instances
all_adults = get_all_adults(Adult)


countOfChilds = 0
countOfChildsPets = 0
for adult in all_adults:
    countOfChilds = 0
    countOfChildsPets = 0
    for child in all_childs:
        if child.lastname == adult.lastname:
            countOfChilds += 1
            countOfChildsPets = countOfChildsPets + child.countOfPets
            if child == all_childs[-1]:
                # tiek izsaukta klases Adult metode "countOfChildsMethod()", kur tiek atspoguļos bērnu un viņu mājdzīvnieku skaits katra pieaugušā ģimenē:
                adult.countOfChildsMethod(adult.firstname, countOfChilds, countOfChildsPets) 
        else:
            if child == all_childs[-1]:
                # tiek izsaukta klases Adult metode "countOfChildsMethod()"
                adult.countOfChildsMethod(adult.firstname, countOfChilds, countOfChildsPets) 
