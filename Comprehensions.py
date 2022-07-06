# COMPREHENSIONS

### List Comprehension


salaries = [1000, 2000, 3000, 4000, 5000]

# foksiyonumuz;

def new_salary(x):
    return x * 20 / 100 + x

for salary in salaries:
    print(new_salary(salary))

null_list = []

for salary in salaries:
    null_list.append(new_salary(salary))

null_list = []

for salary in salaries:
    if salary > 3000:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary * 2))


# Uzun uzun yazmak yerine, "Comprehension" kullanırız;

[new_salary(salary * 2) if salary < 3000 else new_salary(salary) for salary in salaries]


[salary * 2 for salary in salaries if salary < 3000] # sadece if varsa "for salary in salaries" sola yazılır.

[salary * 2 if salary < 3000 else salary * 0 for salary in salaries] # if ile else birlikte kullanılmıs ise "for salary in salaries" saga yazılır.

[new_salary(salary * 2) if salary < 3000 else new_salary(salary * 0.2) for salary in salaries]



# Başka bir örnek yapalım;

students = ["John", "Mark", "Venessa", "Mariam"]
students_no = ["John", "Venessa"]


[student.lower() if student in students_no else student.upper() for student in students]

# "not in" kullanımı;

[student.upper() if student not in students_no else student.lower() for student in students]



### Dict Comprehension


dictionary = {'a': 1,
              'b': 2,
              'c': 3,
              'd': 4}

dictionary.keys()
dictionary.values()
dictionary.items()

# key'lere dokunmadan valuelerin karesini almak istiyoruz; (k, v): indexlerimiz

{k: v ** 2 for (k, v) in dictionary.items()}

# key"lere islem yapmak (v sabit) istersem;
{k.upper(): v for (k, v) in dictionary.items()}

# key'lere de value'lere de islem yapmak iğsterem;
{k.upper(): v*2 for (k, v) in dictionary.items()}



### Uygulama

# Amaç: çift sayıların karesi alınarak bir sözlüğe eklemek;

# Key'ler orjinal değerler value'lar ise değiştirilmiş değerler olacak.


numbers = range(10)
new_dict = {}

for n in numbers:
    if n % 2 == 0: #n :cift sayilar
        new_dict[n] = n ** 2 #koseli parantez icerisinde yazınca otomatik kaylere atıyor. !
new_dict

# Uzun uzun yazmak yerine, "Comprehension" kullanırız;

numbers = range(10)
new_dict = {}

{n: n ** 2 for n in numbers if n % 2 == 0}