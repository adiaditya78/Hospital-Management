import json 
import os   
from datetime import time 
"""                                      <- Hospital Management System ->                          """

# Doctor Details  
class Doctor_details:

    def __init__(self):
        self.details = []

    # To save data in the json file
    def save_record(self):
        data_name = self.details[0]['Name']
        data_name += ".json"
        with open(data_name, 'w') as doc_data:
            json.dump(self.details, doc_data, indent = 4)
            print(f"Record of doctor {data_name[0:-5]} saved.")


    # Add the data to the list in form of dictionary
    def add_Doc_Details(self):
        name = input("Enter the name of Doctor: ").title()
        quali = input("Enter the qualification: ").upper()
        specialty = input("Enter the specialty: ").title()
        print("Enter the available hours in HH:MM format")
        avi_from = input("From: ")
        avi_to = input("To: ")
        
        self.details.append({"Name" : name, "Qualification": quali, "Specialty" : specialty, "from" : avi_from, "to" : avi_to})

    # Update the details of doctor
    def update_details(self, doc_name):
        try:
            doc_name += ".json"
            with open(doc_name, 'r+') as readData:
                existing_data = json.load(readData)

                print("Which value do you want to update -> ")
                print("1. Name")
                print("2. Qualification")
                print("3. Specialty")
                print("4. Available Hours")
                dataToupdate = validChoice("Enter your choice: ",1,4)

                if dataToupdate == 1:
                    new_name = prompt('name').title()
                    existing_data[0]['Name'] = new_name
                    new_name += ".json"
                    os.rename(doc_name, new_name)
                elif dataToupdate == 2:    
                    existing_data[0]['Qualification'] = prompt('qualification').upper()
                elif dataToupdate == 3:
                    existing_data[0]['Specialty'] = prompt('specialty').title()
                else:    
                    existing_data[0]['from'] = prompt('available hours from')
                    existing_data[0]['to'] = prompt('available hours to')
                readData.seek(0)
                json.dump(existing_data, readData,indent=4)
                readData.truncate()
                print("Record updated Successfully.")
        except:
            print("Record doesn't exist.")

    # Delete the record of doctor
    def delete_details(self,record_name):
        record_name += ".json"
        if os.path.exists(record_name):
            os.remove(record_name)
            print(f"Doctor {record_name[0:-5]}'s details successfully deleted!")   
        else:
            print(f"Doctor {record_name[0:-5]}'s details does not exist.")         

    # Display the records of doctor
    def display_details(self, doctor_name):
        doctor_name += ".json"
        try:    
            with open(doctor_name, 'r') as readData:
                data = json.load(readData)
                data = data[0]
                print(f" Doctor's Name - {data['Name']}\n Qualification - {data['Qualification']}\n Specialty - {data['Specialty']}\n Available Hours - {data['from']} - {data['to']}")
        except:
            print("Record does not exist.")



# Patient Details
class Patient_details:

    def __init__(self):
        self.p_details = []
    # save the record of patient in json form
    def save_record(self):
        data_name = self.p_details[0]['Name']
        data_name += ".json"
        with open(data_name, 'w') as patient_data:
            json.dump(self.p_details, patient_data, indent = 4)
            print("Record of patient saved.")    


    # Add the details of the patient
    def add_patientDetails(self):
        name = input("Enter the name of Patient: ").title()
        age = input("Enter age: ")
        gender = input("Enter gender: ").title()
        contact = validContact("Enter the contact number: ")
        
        self.p_details.append({"Name" : name, "Age": age, "Gender" : gender, "Contact" : contact})


    # Update the details of Patient
    def update_details(self, patient_name):
        try:  
            patient_name += ".json"  
            with open(patient_name, 'r+') as readData:
                existing_data = json.load(readData)
                print("Which value do you want to update -> ")
                print("1. Name")
                print("2. Age")
                print("3. Gender")
                print("4. Contact")
                dataToupdate = validChoice("Enter your choice: ",1,4)
                if dataToupdate == 1:
                    new_name = prompt('name').title()
                    existing_data[0]['Name'] = new_name
                    new_name += ".json"
                    os.rename(patient_name, new_name)

                elif dataToupdate == 2:    
                    existing_data[0]['Age'] = prompt('age')
                elif dataToupdate == 3:
                    existing_data[0]['Gender'] = prompt('gender').title()
                else:    
                    existing_data[0]['Contact'] = validContact(prompt("contact"))                
                readData.seek(0)
                json.dump(existing_data, readData,indent=4)
                readData.truncate()
                print("Record updated Successfully.")
        except:
            print("Record doesn't exist.")


    # Delete the details of patient
    def delete_details(self, record_name):
        record_name += ".json"
        if os.path.exists(record_name):
            os.remove(record_name)
            print(f"Patient {record_name[:-5]}'s details successfully deleted!")   
        else:
            print(f"Patient {record_name[:-5]}'s details does not exist.") 


    # display the details of patient
    def display_detail(self, patient_name):
        patient_name += ".json"
        try:    
            with open(patient_name, 'r') as readData:
                data = json.load(readData)
                data = data[0]
                print(f" Patient's Name - {data['Name']}\n Age - {data['Age']}\n Gender - {data['Gender']}\n Contact - {data['Contact']}")
        except:
            print("Record does not exist.")


# Book an appointment             
def appointment(doctor_name, Pattime):
    doctor_name += ".json"
    Pattime = validtime(Pattime)
    if Pattime is None:
        print("Invalid time. try again!")
        return

    try:
        with open(doctor_name, 'r') as doc:
            data = json.load(doc)
            doc_from = data[0]['from']
            doc_to = data[0]['to']
            timefrom = validtime(doc_from)
            timeto = validtime(doc_to)
 
            if timefrom <= Pattime and timeto > Pattime :
                patient_name = input("Enter the patient name: ")
                patient = "appoint_" + patient_name + ".json"
                with open(patient, 'w') as app:
                    appoint_ = {"doc_name" : doctor_name, "pat_name" : patient_name, "Time" : str(Pattime)}
                    json.dump(appoint_, app)
                    print(f"Appointment of {patient_name} with doctor {doctor_name[:-5]} is booked.")
            else:
                print("Slot is not available!") 
    except FileNotFoundError:
        print(f"Can't found doctor {doctor_name[0:-5]}")                  


"""Functions"""
# For comparing the time
def validtime(time1):
    try:
        hour1, min1 = map((int), time1.split(":"))
        return time(hour1, min1)
    except:
        print("Enter the time in correct format!")
        return None

# used in update to provide prompt
def prompt(prompt):
    return input(f"Enter the new {prompt}: ")


# To take a valid input
def validChoice(prompt, start, end):
    while True:
        try:
            choice = int(input(prompt))
            if choice >= start and choice <= end:
                return choice
            else:
                print("Invalid Choice!")
        except:
            print(f"Enter only between {start} - {end}.") 


# To take valid contact number
def validContact(prompt):
    while True:
        try:
            num = int(input(prompt))
            if len(str(num)) == 10:
                return num
            else:
                print("Enter a valid contact number!")
        except:
            print("Enter only positive Integers.")        


# Doctor Details Manager
def doctor_menu():
    print("\n<- Doctor Details Manager ->")
    print("1. Add new details")
    print("2. Update details")
    print("3. Deleting details")
    print("4. Display details")
    doc_menu = validChoice("\nEnter your choice: ",1, 4)
    Doctor = Doctor_details()
    if doc_menu == 1:
        Doctor.add_Doc_Details()
        Doctor.save_record()
    elif doc_menu == 2:
        doc_name = input("Enter the name of Doctor: ").title()
        Doctor.update_details(doc_name)
    elif doc_menu == 3:
        doc = input("Enter the doctor name to delete the record: ").title()
        Doctor.delete_details(doc)
    else:
        doc = input("Enter the doctor name to display the details: ").title()
        Doctor.display_details(doc)

# Patient details manager
def patient_menu():
    print("\n<- Patient Details Manager ->")
    print("1. Add new details")
    print("2. Update details")
    print("3. Deleting details")
    print("4. Display details")
    pat_menu = validChoice("\nEnter your choice: ",1, 4)
    patient = Patient_details()
    if pat_menu == 1:
        patient.add_patientDetails()
        patient.save_record()
    elif pat_menu == 2:
        patient_name = input("Enter the name of Patient: ").title()
        patient.update_details(patient_name)
    elif pat_menu == 3:
        pat_name = input("Enter the doctor name to delete the record: ").title()
        patient.delete_details(pat_name)
    else:
        patient_dis = input("Enter the patient name to display the details: ").title()
        patient.display_detail(patient_dis)      

# Main function
def main():
    print('\n"Welcome to Hospital Management System"')
    stay = True
    while stay:
        print("\n<- Main Menu ->")
        print("1. Manage Doctor")
        print("2. Manage Patient")
        print("3. Book Appointment")
        print("4. Exit")
        menu = validChoice("\nEnter your Choice: ",1,4)
        if menu == 1:
            doctor_menu()
        elif menu == 2:
            patient_menu()
        elif menu == 3:
            doc = input("Enter the name of doctor: ").title()
            time1 = input("Enter the time(24 - format) to book appointment: ")
            appointment(doc, time1)    
        else:
            exitORnot = validChoice("Are You Sure?\n 1. Yes\n 2. No\n -> ",1,2)
            if exitORnot == 1:
                stay = False 
main()   