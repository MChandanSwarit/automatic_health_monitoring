import random

class Patient:
    patients = {}

    def __init__(self, id, name, gender, age, medicalRecord=None):
        self.id = id
        self.name = name
        self.gender = gender
        self.age = age
        self.medicalRecord = medicalRecord if medicalRecord is not None else {}

    @classmethod
    def add_patient(cls, id, name, gender, age, medicalRecord=None):
        if id in cls.patients:
            print(f"Patient with ID: {id} already exists.")
        else:
            cls.patients[id] = Patient(id, name, gender, age, medicalRecord)
            print(f"Patient {name} added successfully.")

    @classmethod
    def retrieve_patient(cls, name):
        patient = next((p for p in cls.patients.values() if p.name == name), None)
        if patient:
            print(f"\nID: {patient.id}")
            print(f"Name: {patient.name}")
            print(f"Gender: {patient.gender}")
            print(f"Age: {patient.age}")
            print(f"Medical Record: {patient.medicalRecord}")
        else:
            print(f"No patient found with Name: {name}")

    @classmethod
    def update_medical_record(cls, name, key, value):
        patient = next((p for p in cls.patients.values() if p.name == name), None)
        if patient:
            patient.medicalRecord[key] = value
            print(f"Medical record updated for patient {name}.")
        else:
            print(f"No patient found with Name: {name}.")
    
    @classmethod
    def delete_patient(cls, id=None, name=None):
      if id and id in cls.patients:
        del cls.patients[id]
        print(f"Patient with ID: {id} has been deleted.")
      elif name:
        patient_to_delete = next((p for p in cls.patients.values() if p.name == name), None)
        if patient_to_delete:
          del cls.patients[patient_to_delete.id]
          print(f"Patient with Name: {name} has been deleted.")
        else:
          print(f"No patient found with Name: {name}.")
      else:
        print("No valid ID or Name provided for deletion.")

def generate_random_id(min_value=1, max_value=10000000):
    return random.randint(min_value, max_value)

def main():
    while True:
        print("\nHealth Monitoring System:")
        print("1. Add Patient Record")
        print("2. Retrieve Patient Record")
        print("3. Update Medical Record")
        print("4. Delete Patient Record")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            id = generate_random_id()
            print(f"Generated Patient ID: {id}")
            name = input("Enter Patient Name: ")
            gender = input("Enter Patient Gender: ")
            age = int(input("Enter Patient Age: "))
            medicalRecord = {}
            while True:
                add_record = input("Add a medical record? (yes/no): ").strip().lower()
                if add_record == 'yes':
                    key = input("Enter Medical Record Key: ")
                    value = input("Enter Medical Record Value: ")
                    medicalRecord[key] = value
                elif add_record == 'no':
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
            Patient.add_patient(id, name, gender, age, medicalRecord)
            print("\nCurrent Patients List:")
            for pid, patient in Patient.patients.items():
                print(f"ID: {pid}, Name: {patient.name}")

        elif choice == '2':
            name = input("Enter Patient Name: ")
            Patient.retrieve_patient(name)

        elif choice == '3':
            name = input("Enter Patient Name: ")
            key = input("Enter Medical Record Key to Update: ")
            value = input("Enter New Medical Record Value: ")
            Patient.update_medical_record(name, key, value)

        elif choice == '4':
          id = input("Enter Patient ID (or leave blank to search by name): ")
          if id.strip() == "":
            name = input("Enter Patient Name: ")
            Patient.delete_patient(name=name)
          else:
            Patient.delete_patient(id=id)
          print("\nCurrent Patients List:")
          for pid, patient in Patient.patients.items():
              print(f"ID: {pid}, Name: {patient.name}")
            
        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
