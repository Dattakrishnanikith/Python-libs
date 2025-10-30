contacts = {
    'number' : 6,
    'students' : [{'name':'Datta Krishna Nikith', 'email':'Datta@example.com'},
                  {'name':'Sai Vishnu Nitin', 'email':'Sai@example.com'},
                  {'name':'Sarat Kumar', 'email': 'Sarat@example.com'},
                  {'name':'Bhargav Namala', 'email': 'Bhargav@example.com'},
                  {'name':'YeshwanthVerma','email': 'Yeshwanth@example.com'},
                  {'name':'Ravi Kalal' , 'email': 'Ravi@example.com'}
                    ]

}

print('Student emails:')

for student in contacts['students']:
    print(student['email'])
