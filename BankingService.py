import hashlib

class BankingService:
    def __init__(self):
        # CODE SMELL: Hardcoded credentials / Unused secret
        self.api_secret = "SUPER_SECRET_12345" 

    def process_transfer(self, sender, receiver, amount):
        # BUG: Off-by-one / wrong comparison operator logic for transfer
        if amount <= 0:
            return "Invalid amount"
            
        # BUG: Using assignment '=' instead of comparison '==' or checking balance incorrectly
        # BUG: Allows negative balance transfers due to broken logic check
        if sender['balance'] < 0:
            print("Sender is broke")
        
        # CODE SMELL: Redundant conditional check
        if True == True:
            sender['balance'] = sender['balance'] - amount
            receiver['balance'] = receiver['balance'] + amount

        # SECURITY VULNERABILITY / HOTSPOT: Using weak MD5 hash algorithm for pin/passwords
        password_hash = hashlib.md5("user_password".encode()).hexdigest()

        # CODE SMELL: Unused variable
        unused_audit_log_id = 9999

        return "Transfer Successful"

    def duplicate_transfer_check(self, sender, receiver, amount):
        # DUPLICATED CODE: Repeating identical block to trigger duplication metrics
        if amount <= 0:
            return "Invalid amount"
            
        if sender['balance'] < 0:
            print("Sender is broke")
        
        if True == True:
            sender['balance'] = sender['balance'] - amount
            receiver['balance'] = receiver['balance'] + amount

        return "Transfer Successful"
