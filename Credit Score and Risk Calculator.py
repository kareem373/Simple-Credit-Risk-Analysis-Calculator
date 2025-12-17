Name = input("Dear user, what is your prefix, and your name? ")
try:
    Loan_amt = int(input("Please enter the loan amount you wish to apply for: "))
except ValueError:
    print("Error, please enter a number without any currency symbols")
    exit()
Names = ["Mr Kareem", "Mr Ahmed", "Mr Mohamed", "Mr Daniel"]
CreditScr = [753, 430, 804, 650]
Phone = [123,345,678,1234]
def risk(TBC_Credit):
    if TBC_Credit >= 700:
        return "Low risk (Good credit score)"
    elif TBC_Credit >= 600:
        return "Medium risk (Risky credit score)"
    else:
        return "High risk (Poor credit score)"

User = 0
found = False

while User < len(Names):
    if Name == Names[User]:
        TBC_Credit = CreditScr[User]
        final_risk = risk(TBC_Credit)
        print(final_risk)
        found = True
        break
    User += 1

if not found:
    print("ERROR: Name not found")
    
if "High" in final_risk:
        Risk_inDep = "Poor"
elif "Medium" in final_risk:
    Risk_inDep = "Risky"
elif "Low" in final_risk:
    Risk_inDep = "Good"

if Name == Names[User]:
    Contact = Phone[User]



if Risk_inDep == "Poor":
    print("We have automatically rejected your loan application due to a low credit score")
else:
    print("Dear", Name, "we are considering your loan request and will contact you at", Contact)
    

    