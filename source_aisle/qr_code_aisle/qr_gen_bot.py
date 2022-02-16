#module used -> qrcode
import qrcode

def gen_qr_code(content: str, filename:str)->bool:
    """qr gen bot

    Args:
        content (str): content to be inscribed in unique qrcode generated
        filename (str): name that's supposed to be assigned to the qr code generated

    Returns:
        bool: returns True or False relyin on...whether code has been generated successfully or not
    """
    
    try:
        #generating a qr bar 
        code_bar = qrcode.make(content)
        
        #savin the qr bar
        code_bar.save(filename)
    except: mission_check = False
    else: mission_check = True
    finally: pass
    
    return mission_check


if __name__=='__main__': 
    gen_qr_code('how r ya', 'max.jpg')
    