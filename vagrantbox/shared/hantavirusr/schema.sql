DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS Patients;


CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE Patients (
    ID INTEGER PRIMARY KEY,
    Firstname TEXT,
    Lastname TEXT,
    Age INTEGER,
    Date_of_Birth TEXT,
    Phone_Number TEXT,
    Date_of_Admission TEXT,
    National_Insurance_Number TEXT,
    NHS_Number INTEGER,
    Infection_Status TEXT
);
