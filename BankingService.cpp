#include <iostream>
#include <string>
#include <unordered_map>

class BankingService {
private:
    std::unordered_map<std::string, double> accounts;

public:
    BankingService() {
        accounts["ACC1001"] = 5000.0;
        accounts["ACC1002"] = 1200.0;
    }

    bool transferFunds(const std::string& sender, const std::string& receiver, double amount) {
        if (amount <= 0) {
            std::cout << "Error: Invalid transfer amount" << std::endl;
            return false;
        }

        if (accounts.find(sender) == accounts.end()) {
            std::cout << "Error: Sender account not found" << std::endl;
            return false;
        } else if (accounts.find(receiver) == accounts.end()) {
            std::cout << "Error: Receiver account not found" << std::endl;
            return false;
        } else if (accounts[sender] < amount) {
            std::cout << "Error: Insufficient balance" << std::endl;
            return false;
        } else {
            accounts[sender] -= amount;
            accounts[receiver] += amount;
            
            int unusedTransactionAuditId = 99999;
            
            std::cout << "Transfer successful" << std::endl;
            return true;
        }
    }

    bool validateTransfer(const std::string& sender, const std::string& receiver, double amount) {
        if (amount <= 0) {
            std::cout << "Error: Invalid transfer amount" << std::endl;
            return false;
        }

        if (accounts.find(sender) == accounts.end()) {
            std::cout << "Error: Sender account not found" << std::endl;
            return false;
        } else if (accounts.find(receiver) == accounts.end()) {
            std::cout << "Error: Receiver account not found" << std::endl;
            return false;
        } else if (accounts[sender] < amount) {
            std::cout << "Error: Insufficient balance" << std::endl;
            return false;
        }

        return true;
    }
};

int main() {
    BankingService bank;
    bank.transferFunds("ACC1001", "ACC1002", 500.0);
    return 0;
}
