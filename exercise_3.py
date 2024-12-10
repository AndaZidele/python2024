# List
# Sarakstā tiek atspoguļoti mājdzīvnieku tipi vienas klases skolēniem
typesOfPetsIn1stClass = ["cat", "dog", "fish", "rabbit", "hamster"]
# ja kādam tiek iegādāts vēl kāds mājdzīvnieks, to var pievienot
typesOfPetsIn1stClass.append("guinea pig")
print(typesOfPetsIn1stClass)

# Tuple
# Tuplē tiek atspoguļoti mājdzīvnieku tipi otras klases skolēniem
typeOfPetsIn2ndClass = ("cat", "guinea pig", "dog", "rabbit")
# ja kādam tiek iegādāts vēl kāds mājdzīvnieks, to var pievienot
l = list(typeOfPetsIn2ndClass)
l.append("snake")
tup = tuple(l)
print(tup)

# Set
# Kopā tiek atspoguļoti mājdzīvnieku tipi trešās klases skolēniem
typeOfPetsIn3rdClass = {"cat", "rabbit", "snake"}
# ja kādam tiek iegādāts vēl kāds mājdzīvnieks, to var pievienot
typeOfPetsIn3rdClass.add("guinea pig")
print(typeOfPetsIn3rdClass)
# Var apskatīties kuru dzīvnieku tipi ir visās klasēs
print(typeOfPetsIn3rdClass & set(typeOfPetsIn2ndClass) & set(typesOfPetsIn1stClass))

# Dictionary
# Vārdnīcā tiek atspoguļots skolēnu un mājdzīvnieku skaits katrā klasē 
petsAndStudentsDictionary = {
    "date": "10.12.2024.",
    "classes": [
        {
            "name": "1_A",
            "countOfStudents": 25,
            "countOfPets": 20
        },
        {
            "name": "1_B",
            "countOfStudents": 26,
            "countOfPets": 19
        },
        {
            "name": "1_C",
            "countOfStudents": 27,
            "countOfPets": 21
        }
    ]

}
# var izvadīt katras klases bērnu skaitu:
for item in petsAndStudentsDictionary["classes"]:
    print("There are", item.get("countOfStudents"), "students in the class", item.get("name"))
    