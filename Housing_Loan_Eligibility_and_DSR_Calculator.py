import sys
import os

os.system('cls')  # Clear console screen (for Windows)

# List to store loan calculations
loan_calculations = []

# Function to calculate the monthly loan installment
def calculate_monthly_instalment(principal, annual_interest_rate, loan_term):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    num_payments = loan_term * 12
    monthly_installment = principal * (
            monthly_interest_rate * ((1 + monthly_interest_rate) ** num_payments) / (((1 + monthly_interest_rate) ** num_payments) - 1))
    return monthly_installment

# Function to calculate the total amount payable
def calculate_total_amount_payable(monthly_instalment, loan_term):
    return monthly_instalment * loan_term * 12

# Function to calculate the Debt Service Ratio (DSR)
def calculate_dsr(monthly_income, monthly_instalment, monthly_commitments):
    total_commitments = sum(monthly_commitments) + monthly_instalment
    dsr = (total_commitments / monthly_income) * 100
    return dsr

# Function to display loan details
def display_loan_details(loan_details):
    print("\n****************************************")
    print("Loan Details:")
    print(f"Principal Amount: RM{loan_details['principal']:.2f}")
    print(f"Annual Interest Rate: {loan_details['annual_interest_rate']:.2f}%")
    print(f"Loan Term: {loan_details['loan_term']} years")
    print(f"Monthly Income: RM{loan_details['monthly_income']:.2f}")
    print(f"Monthly Instalment: RM{loan_details['monthly_instalment']:.2f}")
    print(f"Total Amount Payable: RM{loan_details['total_amount_payable']:.2f}")
    print(f"DSR (Debt Service Ratio): {loan_details['dsr']:.2f}%")
    print("****************************************")

# Function to delete a loan calculation
def delete_calculation(index):
    if 1 <= index <= len(loan_calculations): #index more or equal than 1 and the length of loan calculation in list less than and equal than index
        del loan_calculations[index - 1]   #deleted the loan calculation 
        print(f"Calculation {index} deleted.")
    else: #if the index out of bound for the list
        print("Invalid index.")

# Function to view details of a specific loan calculation
def view_details(index):
    if 1 <= index <= len(loan_calculations): #index more or equal than 1 and the length of loan calculation in list less than and equal than index
        print(f"\nDetails for Loan Calculation {index}:") 
        display_loan_details(loan_calculations[index - 1]) # display specific loan calculation by index that user insert
    else: #if the index out of bound for the list
        print("Invalid index.")

# Function to update the DSR threshold
def update_dsr_threshold():
    new_threshold = get_user_input("Enter the new DSR threshold percentage: ")
    return float(new_threshold) #return new dsr threshold

# Function to determine loan eligibility based on DSR
def calculate_loan_eligibility(dsr, dsr_threshold):
    # if dsr <= dsr thereshold display congratulation else Sorry
    return "Congratulations! You are eligible for the loan." if dsr <= dsr_threshold else "Sorry, you are not eligible for the loan due to high Debt Service Ratio (DSR)."

# Function to display the main menu and get user input
def main_menu():
    print("\n****************************************")
    print("************* Main Menu: ***************")
    print("****************************************")
    print("1. Calculate a new loan")
    print("2. Display details of all loan calculations")
    print("3. Delete details of a loan calculation")
    print("4. View details of a specific loan calculation")
    print("5. Update DSR Threshold")
    print("6. Exit")
    return input("Enter your choice (1/2/3/4/5/6): ")

# Function to get numerical input from the user
def get_user_input(prompt, allow_zero=False, allow_negative=False):
    while True: # repeat until the input is non zero and non negative value
        try:
            value = float(input(prompt)) #if the input not a number will catch exception
            if not allow_zero and value == 0: # the input is zero
                print("Please enter a non-zero value.")
            elif not allow_negative and value < 0: # the input is negative value
                print("Please enter a non-negative value.")
            else: # the input is non zero and non negative value , return the value
                return value
        except ValueError: #the input is not a number or float number
            print("Invalid input. Please enter a valid numerical value.")

def get_user_integer_input(prompt, allow_zero=False, allow_negative=False):
    while True: # repeat until the input is non zero and non negative value and just integer number
        try:
            value = int(input(prompt))#if the input not a integer number will catch exception
            if not allow_zero and value == 0: # the input is zero
                print("Please enter a non-zero integer.")
            elif not allow_negative and value < 0: # the input is negative value
                print("Please enter a non-negative integer.")
            else: # the input is non zero and non negative value , return the value
                return value
        except ValueError: #the input is not a integer number 
            print("Invalid input. Please enter a valid integer.")


# Main program execution
def main():
    dsr_threshold = 70  # Default DSR threshold
    while True: # repeat until enter 5
        choice = main_menu() #display main menu

        if choice == '1': # enter 1
            # Get user input for loan details, cannot enter 0 and negative value and word
            principal = get_user_input("Enter the principal loan amount: RM ", allow_zero=False, allow_negative=False)
            interest_rate = get_user_input("Enter the annual interest rate (in percentage): ", allow_zero=False, allow_negative=False)
            loan_term = get_user_integer_input("Enter the loan term (in years): ", allow_zero=False, allow_negative=False)
            monthly_income = get_user_input("Enter the applicant's monthly income: RM ", allow_zero=False, allow_negative=False)

            # Handle the case where the number of other financial commitments is zero, cannot negative value and word only
            num_commitments = get_user_integer_input("Enter the number of other monthly financial commitments: ", allow_negative=False, allow_zero = True)

            # Check if there are commitments to be entered
            if num_commitments > 0: #if have financial commitments mean user insert number more than 0 on number of commitment
             monthly_commitments = [get_user_input(f"Enter the amount of commitment {i + 1}: RM ", allow_negative=False) #cannot insert 0 ,negative value and word
                            for i in range(num_commitments)] #do repeat until the number of commitment
            else: #if not have financial commitment
             monthly_commitments = []


            # Calculate loan details
            monthly_installment = calculate_monthly_instalment(
                principal=principal,
                annual_interest_rate=interest_rate,
                loan_term=loan_term
            )
            #calculate total amount payable
            total_amount_payable = calculate_total_amount_payable(monthly_installment, loan_term)
            #calculate dsr
            dsr = calculate_dsr(monthly_income, monthly_installment, monthly_commitments)

            # Update loan details
            loan_details = {
                'principal': principal,
                'annual_interest_rate': interest_rate,
                'loan_term': loan_term,
                'monthly_income': monthly_income,
                'monthly_commitments': monthly_commitments,
                'monthly_instalment': monthly_installment,
                'total_amount_payable': total_amount_payable,
                'dsr': dsr
            }

            # Add loan details to the list
            loan_calculations.append(loan_details)
            # display the loan details
            display_loan_details(loan_details)

            # Determine loan eligibility and display message
            eligibility_message = calculate_loan_eligibility(dsr, dsr_threshold)
            print(eligibility_message)

        elif choice == '2': #enter 2
            # Display details of all loan calculations
            if loan_calculations: # have loan details in the list
                for i, loan in enumerate(loan_calculations, 1): #repeat until display all loan details 
                    print(f"\nLoan Calculation {i}:")
                    display_loan_details(loan) # display loan details 
            else: # not any loan details in the list
                print("No loan calculations available.")

        elif choice == '3': #enter 3
            # Delete details of a loan calculation
            index_to_delete = get_user_integer_input("Enter the index of the calculation to delete: ")
            delete_calculation(index_to_delete)

        elif choice == '4': #enter 4
            # View details of a specific loan calculation
            index_to_view = get_user_integer_input("Enter the index of the calculation to view details: ")
            view_details(index_to_view)

        elif choice == '5': # enter 5
            # Update DSR Threshold
            dsr_threshold = update_dsr_threshold()
            print(f"DSR Threshold updated to {dsr_threshold:.2f}%")

        elif choice == '6': #enter 6
            # Exit the program
            print("Exiting the program. Goodbye!")
            sys.exit() #stop running

        else: # not enter 1,2,3,4 or 5 will display
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")


if __name__ == "__main__":
    main()
