# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account 
from savings_account import create_savings_account 

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    account_balance_string = input("Enter a savings acount balance: ")

    #Check if the customer typed a number
    input_is_digit=False
    while input_is_digit==False:
        match account_balance_string.isdigit():
         case True:
          input_is_digit=True
         case other:
          input_is_digit=False
          account_balance_string=input("Enter a valid number for your savings account balance: ")

    savings_balance=float(account_balance_string)

    savings_interest_string = input("Enter the interest rate: ")

    #Check if the customer typed a number
    input_is_digit=False
    while input_is_digit==False:
        match savings_interest_string.replace(".", "").isnumeric():
         case True:
          input_is_digit=True
         case other:
          input_is_digit=False
          savings_interest_string=input("Enter a valid number for the interest rate: ")

    savings_interest=float(savings_interest_string)

    savings_maturity_string = input("Enter the months for your savings acount maturity: ")

    #Check if the customer typed a number
    input_is_digit=False
    while input_is_digit==False:
        match savings_maturity_string.isdigit():
         case True:
          input_is_digit=True
         case other:
          input_is_digit=False
          savings_maturity_string=input("Enter a valid number for your savings maturity months: ")

    savings_maturity=float(savings_maturity_string)

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"Your updated savings balance is: $" + "%.2f" % updated_savings_balance)
    print(f"The savings interest earned is: $"  + "%.2f" % interest_earned)
    #print("%.2f" % interest_earned)

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_account_balance_string = input("Enter a CD acount balance: ")

    #Check if the customer typed a number
    input_is_digit=False
    while input_is_digit==False:
        match cd_account_balance_string.isdigit():
         case True:
          input_is_digit=True
         case other:
          input_is_digit=False
          cd_account_balance_string=input("Enter a valid number for your CD account balance: ")

    cd_balance=float(cd_account_balance_string)

    cd_interest_string = input("Enter the interest rate: ")

    #Check if the customer typed a number
    input_is_digit=False
    while input_is_digit==False:
        match cd_interest_string.replace(".", "").isnumeric():
         case True:
          input_is_digit=True
         case other:
          input_is_digit=False
          cd_interest_string=input("Enter a valid number for the interest rate: ")

    cd_interest=float(cd_interest_string)

    cd_maturity_string = input("Enter the months for your CD acount maturity: ")

    #Check if the customer typed a number
    input_is_digit=False
    while input_is_digit==False:
        match cd_maturity_string.isdigit():
         case True:
          input_is_digit=True
         case other:
          input_is_digit=False
          cd_maturity_string=input("Enter a valid number for your CD maturity months: ")

    cd_maturity=float(cd_maturity_string)

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    #print(f"Your updated CD balance is {updated_cd_balance}. The interest earned is {interest_earned}")

    print(f"Your updated CD balance is: $" + "%.2f" % updated_cd_balance)
    print(f"The CD interest earned is: $"  + "%.2f" % interest_earned)

if __name__ == "__main__":
    # Call the main function.
 main()