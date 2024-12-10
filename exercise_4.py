# Vārdnīcā tiek atspoguļots skolēnu un mājdzīvnieku skaits katrā klasē (no 3.uzdevuma)
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
            "countOfPets": 14
        }
    ]

}

# For Loop
# pārbaudīt, kurā klasē ir lielākais dzīvnieku skaits uz vienu bērnu
countOfPetsPerOneChild = 0.0
className = ""
for student in petsAndStudentsDictionary['classes']:
    petCount = student.get("countOfPets")
    studentCount = student.get("countOfStudents")
    countOfPPerOneC = petCount / studentCount
    if countOfPetsPerOneChild < countOfPPerOneC:
        countOfPetsPerOneChild = countOfPPerOneC
        className = student.get("name")

print("The largest pets count per one student is in the class", className)

# Range Loop
# saskaita, cik skolā ir klases, kuru skolēnu dzīvnieku skaits ir vai zem 15 vai arī vismaz 20
countOfClasses = 0
for x in range(len(petsAndStudentsDictionary['classes'])):
    if petsAndStudentsDictionary['classes'][(x-1)].get("countOfPets")>=20:
        countOfClasses += 1
    elif petsAndStudentsDictionary['classes'][(x-1)].get("countOfPets")<15:
        countOfClasses += 1
print("There are", countOfClasses, "such classes in this school")

# While
# izvadīt katras klases studentu skaitu
boo = True
sk = 0
while boo:
    print("In the class", petsAndStudentsDictionary["classes"][sk].get("name"), "are", petsAndStudentsDictionary["classes"][sk].get("countOfStudents"), "students.")
    sk = sk + 1
    if sk == 3:
        boo = False