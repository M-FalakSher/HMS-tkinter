from app.models.bill import BillModel

class BillingService:
    @staticmethod
    def create_bill(appointment_id: int, amount: float):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        BillModel.create(appointment_id, amount)
        return True

    @staticmethod
    def list_bills():
        return BillModel.list_all()

    @staticmethod
    def mark_paid(bill_id: int):
        BillModel.mark_paid(bill_id)
        return True

    @staticmethod
    def delete_bill(bill_id: int):
        BillModel.delete(bill_id)
        return True
