menu_1 = '''
1-> Signup
2-> Login - Qrcode
3-> Login - Passcode
4-> Shares Composition
5-> Terminate
'''


menu_Login = '''
1-> Withdraw Funds($100000 at max)
2-> Deposit Funds
3-> Transfer Funds
4-> Change Pin
5-> Change Password
6-> Transactional History(Get it Mailed in a CSV format)
7-> Account Info
8-> Delete Account
9-> Log out
----------------------------------------------------------
'''



User_created_email_info = '''
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Account Created Successfully
------------------------------
User's Name: {}
User's Id: {}
User's Balance: ${}
Date Created: {}
User's Email: {}
User's Gender: {}
User's Phone Number: {}
User's Nationality: {}
User's DOB: {}
------------------------------
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''

User_Transaction_info = '''
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
------------------------------
Sender's Name: {}
Sender's Email: {}
Sender's Id: {}
Transaction Time: {}
Reciever's Name: {}
Reciever's Email: {}
Reciever's Id: {}
Funds Transferred: ${}
Royalty Fee: $1
------------------------------
Your Current Balance: ${}
------------------------------
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''

User_credition = '''
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
------------------------------
User's Name: {}
User's Id: {}
Funds Credited/Deposited: ${}
Royalty Fee: ${}
User's Balance: ${}
Credited Time: {}
------------------------------
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''

user_debition = """
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
------------------------------
User's Name: {}
User's Id: {}
Funds Debited/Withdrawn: ${}
Royalty Fee: ${}
User's Balance: ${}
Debited Time: {}
------------------------------
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""

splitter = r'''
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
-----------------------------------------------------------------------------------------------------
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
'''


Email_head_Title = 'CALIBER FINANCES'
suc_emailandres_debition = 'Funds Debited/Withdrawn successfully'
suc_emailandres_credition = 'Funds Credited/Deposited successfully'
suc_emailandres_transcation = 'Funds Transferred successfully'

unsuc_emailandres_debition = 'Fund Debition Failed'
unsuc_emailandres_credition = 'Fund Credition Failed'
unsuc_emailandres_transcation = 'Fund Tranfer Failed'

login_fail = "Login-Unsuccessful"
signup_fail = "Signup-Unsuccessful"

login_pass = "Logged in as -> {}"
signup_pass = "Signup-Successful"

logout_pass = "Logout-Successful"

terminate = 'See ya soon... Program Terminating'

otp_verification = "CALIBER Finances - Verifying your email.. OTP->"

