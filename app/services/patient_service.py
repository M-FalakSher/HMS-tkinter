from app.models.patient import PatientModel
from app.utils.validators import require_non_empty

class PatientService:
    @staticmethod
    def create_patient(name, dob=None, gender=None, phone=None, address=None):
        require_non_empty(name, "Name")
        PatientModel.create(name, dob, gender, phone, address)
        return True

    @staticmethod
    def list_patients():
        return PatientModel.list_all()

    @staticmethod
    def update_patient(pid, name, dob, gender, phone, address):
        require_non_empty(name, "Name")
        PatientModel.update(pid, name, dob, gender, phone, address)
        return True

    @staticmethod
    def delete_patient(pid):
        PatientModel.delete(pid)
        return True
