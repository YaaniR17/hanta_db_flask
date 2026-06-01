DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
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

CREATE TABLE Medical_Examinations (
    Exam_ID INTEGER PRIMARY KEY,
    Patient_ID INTEGER,
    Date_of_Exam TEXT,
    Temperature REAL,
    Blood_Pressure TEXT,
    Oxygen_Saturation INTEGER,
    Symptoms_Description TEXT,
    FOREIGN KEY (Patient_ID) REFERENCES Patients(ID)
);

CREATE TABLE Laboratory_Tests (
    Test_ID INTEGER PRIMARY KEY,
    Patient_ID INTEGER,
    Test_Date TEXT,
    Test_Type TEXT,
    Result TEXT,
    IgM_Level REAL,
    Platelet_Count INTEGER,
    FOREIGN KEY (Patient_ID) REFERENCES Patients(ID)
);

CREATE TABLE Environmental_Exposure (
    Exposure_ID INTEGER PRIMARY KEY,
    Patient_ID INTEGER,
    Location_Type TEXT,
    Animal_Contact_Confirmed BOOLEAN,
    Recent_Activity TEXT,
    Exposure_Date TEXT,
    FOREIGN KEY (Patient_ID) REFERENCES Patients(ID)
);

CREATE TABLE Hantavirus_Species (
    Species_ID INTEGER PRIMARY KEY,
    Virus_Name TEXT,
    Common_Host_Animal TEXT,
    Typical_Region TEXT,
    Severity_Level TEXT
);