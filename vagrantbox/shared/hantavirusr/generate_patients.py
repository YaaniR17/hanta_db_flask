import sqlite3
from faker import Faker
import random

fake = Faker('en_GB')

def generate_nhs_number():
    return random.randint(1000000000, 9999999999)

def generate_ni_number():
    letters = 'ABCEGHJKLMNPRSTWXYZ'
    return f"{random.choice(letters)}{random.choice(letters)}{random.randint(100000, 999999)}{random.choice('ABCD')}"

conn = sqlite3.connect('/shared/instance/hantavirusr.sqlite')
cursor = conn.cursor()

statuses = ['Confirmed', 'Suspected', 'Recovered', 'Deceased']

for _ in range(20):  # generates 20 fake patients
    firstname = fake.first_name()
    lastname = fake.last_name()
    age = random.randint(18, 90)
    dob = fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d')
    phone = fake.phone_number()
    admission = fake.date_between(start_date='-2y', end_date='today').strftime('%Y-%m-%d')
    ni_number = generate_ni_number()
    nhs_number = generate_nhs_number()
    status = random.choice(statuses)

    cursor.execute(
        'INSERT INTO Patients (Firstname, Lastname, Age, Date_of_Birth, Phone_Number, Date_of_Admission, National_Insurance_Number, NHS_Number, Infection_Status)'
        ' VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
        (firstname, lastname, age, dob, phone, admission, ni_number, nhs_number, status)
    )

conn.commit()
conn.close()
print("20 fake patients generated.")