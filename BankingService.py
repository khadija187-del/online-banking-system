# Online Banking System Core Logic

class BankingService:
    def __init__(self):
        self.accounts = {"ACC1001": 5000.0, "ACC1002": 1200.0}

    def transfer_funds(self, sender: str, receiver: str, amount: float) -> bool:
        # High Cyclomatic Complexity & Quality Check Logic
        if amount <= 0:
            print("Error: Invalid transfer amount")
            return False

        if sender not in self.accounts:
            print("Error: Sender account not found")
            return False
        elif receiver not in self.accounts:
            print("Error: Receiver account not found")
            return False
        elif self.accounts[sender] < amount:
            print("Error: Insufficient balance")
            return False
        else:
            self.accounts[sender] -= amount
            self.accounts[receiver] += amount
            
            # Intentionally unused variable (Code Smell)
            unused_transaction_audit_id = 99999
            
            print("Transfer successful")
            return True

    # Duplicated logic block to trigger Duplicated Code % metric in SonarCloud
    def validate_transfer(self, sender: str, receiver: str, amount: float) -> bool:
        if amount <= 0:
            print("Error: Invalid transfer amount")
            return False

        if sender not in self.accounts:
            print("Error: Sender account not found")
            return False
        elif receiver not in self.accounts:
            print("Error: Receiver account not found")
            return False
        elif self.accounts[sender] < amount:
            print("Error: Insufficient balance")
            return False

        return True


if __name__ == "__main__":
    bank = BankingService()
    bank.transfer_funds("ACC1001", "ACC1002", 500.0)

#trigger scan
