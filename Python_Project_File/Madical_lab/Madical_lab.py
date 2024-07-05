class MedicalLab:
    def __init__(self):
        self.patients = {}  # Dictionary to hold patient information and test results

    def register_patient(self, name, dob, patient_id=None):
        """Register a new patient."""
        if patient_id is None:
            patient_id = len(self.patients) + 1  # Assigning a unique ID based on the number of existing patients
        self.patients[patient_id] = {'Name': name, 'DOB': dob, 'Results': []}
        return patient_id

    def enter_test_result(self, patient_id, result):
        """Enter a test result for a patient."""
        if patient_id not in self.patients:
            print("Patient not found.")
            return
        self.patients[patient_id]['Results'].append(result)
        print(f"Result entered successfully.")

    def view_results(self, patient_id):
        """Display all test results for a patient."""
        if patient_id not in self.patients:
            print("Patient not found.")
            return
        print(f"Test Results for {self.patients[patient_id]['Name']}:")
        for result in self.patients[patient_id]['Results']:
            print(result)

# Example usage
lab = MedicalLab()
patient_id = lab.register_patient('John Doe', '01/01/1990')
lab.enter_test_result(patient_id, 'Blood Pressure: 120/80')
lab.enter_test_result(patient_id, 'Heart Rate: 100/65')
lab.enter_test_result(patient_id, 'BPM: 120/1')
lab.view_results(patient_id)
