classroom = [
    {
        'name': 'Alice',
        'email': 'alice@example.com',
        'grades': [
            ('math', 91),
            ('english', 78),
            ('math', 90),
            ('history', 34),
            ('math', 95),
        ],
    },
    {
        'name': 'Bob',
        'email': 'bob@example.com',
        'grades': [
            ('math', 85),
            ('english', 92),
            ('history', 75),
        ],
    },
    {
        'name': 'Charlie',
        'email': 'charlie@example.com',
        'grades': [
            ('physics', 78),
            ('english', 81),
            ('english', 89),
            ('history', 68),
            ('english', 82),
            ('physics', 91),
        ],
    },
]

def re_index(list,my_name):
    for i in range(len(list)):
        if(list[i]['name'] == my_name):
            return(i)
    return 
            
#print(re_index(classroom,'Charlie'))

def add_student(name, email=None):
    if email is None:
        email = name.lower() + "@example.com"
    student = {
        'name': name,
        'email': email,
        'grades': []
    }
    classroom.append(student)

add_student('dev','dev@gmail.com')

def print_details(lst):
    for _ in range(len(lst)):
        print(f'{lst[_]["name"]} | {lst[_]["email"]} | {lst[_]["grades"]} \n')

def delete_student(name):
    if(re_index(classroom, name)):
        i=re_index(classroom, name)
        student = {
        'name': classroom[i]['name'],
        'email': classroom[i]['email'],
        'grades': classroom[i]['grades']
        }
        student=classroom.pop(i)
    else:
        return
delete_student('dev')

def set_email(name, email):
    if(re_index(classroom,name)):
        i=re_index(classroom,name)
        classroom[i]['email'] = email
       

set_email('Bob','email@dfgdg.com')

def add_grade(name, profession, grade):
    if(re_index(classroom,name)):
        i=re_index(classroom,name)
        d= (profession,int(grade))
        classroom[i]['grades'].append(d)

add_grade('Bob','tora',100)


def avg_grade(name, profession):
    for student in classroom:
        if student['name'] == name:
            grades = [grade for subj, grade in student['grades'] if subj == profession]
            if len(grades) > 0:
                gpa = sum(grades) / len(grades)
                return gpa
            else:
                return None
    return None
avg_grade('Bob','english')


def get_professions(name):
    sub = set()
    i = re_index(classroom,name)
    grade=classroom[i]['grades']
    for s,_ in grade:
        sub.add(s)

get_professions("Bob")



