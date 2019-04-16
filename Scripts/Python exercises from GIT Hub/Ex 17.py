#! Python 3
# Question:
# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200
#
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

deposits = []
withdrawals = []

transaction = input("Input the transaction list - D for Deposit and W for Withdrawal. "
                    "If You'd like to exit just press ENTER:")

while transaction:
    transaction_type, transaction_value = transaction.split(" ")
    if transaction_type is "D":
        deposits.append(int(transaction_value))
    elif transaction_type is "W":
        withdrawals.append(int(transaction_value))
    else:
        continue

    transaction = input("Input the transaction list - D for Deposit and W for Withdrawal. "
                        "If You'd like to exit just press ENTER:")

budget = sum(deposits) - sum(withdrawals)
print("Your budget is {}".format(budget))
