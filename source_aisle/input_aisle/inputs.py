from datetime import *


def name_in(username: str): #maccy approved snippet
    '''
    errors-> min limit or max limit or invalid datatype
    '''
    try:
        if 6<=len(username.strip())<=100:
            return username.strip(), True
        else:
            return "min or max limit breached! Try again", False
    except: return 'invalid data type used! Try again', False



def pass_in(passcode: str): #maccy approved snippet
    try:
        if 6<=len(passcode)<=120:
            if ' ' in passcode: return 'space not permitted to be used in passcodes', False
            else: return passcode, True
        else: return "min or max limit breached", False
    except: return 'invalid data type used', False



def phone_no_in(phoneno: str): #maccy approved snippet
    try: 
        if 10<=len(phoneno)<=11 and phoneno.isdigit(): return phoneno, True
        else: return 'max or min len might be breached or invalid phone no.', False
    except: return 'invalid data type used', False



def nationality_in(nationality: str): #maccy approved snippet
    try: 
        if len(nationality)==3 and nationality in ['USA', 'IND']:
            return nationality.upper(), True
        else: return 'max or min len might be breached or invalid Nationality! Try again', False
    except: return 'invalid data type used', False



def gender_in(gender: str): #maccy approved snippet
    try: 
        if len(gender)==1 and gender in list('MF'):
            return gender, True
        else: return 'max or min len might be breached or invalid Gender! Try again', False
    except: return 'invalid data type used! Try again', False



def dob_in(dob: str): #maccy approved snippet
    try:
        day,mnth,yr = dob.split('-')
        datetime(int(yr), int(mnth), int(day))
        main_age = date.today().year-int(yr), date.today().month - int(mnth), date.today().day - int(day)
        if main_age[0]>18: 
            return dob, True
        elif main_age[0]==18 and main_age[1]>=0 and main_age[2]>=0:
            return dob, True
        else: 
            return 'too young to let in', False
            
    except: return 'invalid dob! Try again', False



def pincode_in(pincode: str): #maccy approved snippet
    try: 
        if pincode.isdigit() and len(pincode)==4:
            return pincode, True
        else: return 'necessary parameters breached', False
    except: return 'wrong datatype', False
    
def email_in(email: str):
    try: 
        if (' ' not in email) and ('.' in email) and ('@' in email):
            return email, True
        else: return 'necessary parameters breached', False
    except: return 'wrong datatype', False

if __name__=='__main__':
    pass