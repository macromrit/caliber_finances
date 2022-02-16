import cv2
import numpy as np
import time

def qr_reader()->str or bool:
    main = cv2.VideoCapture(0)
    reader = cv2.QRCodeDetector()
    while main.isOpened():
        ret, frame = main.read()
        found = False
        if ret: 
            try:
                content, abicissa, bar = reader.detectAndDecode(frame)
            except: 
                print('source error.. shift to a detectable region')
                break
            
            try:
                if abicissa: pass
                else: 
                    cv2.putText(frame, 'no resource found'.title(), (150,30), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
            except: 
                abicissa = tuple(map(lambda x:tuple(x),np.array(abicissa[0], dtype=np.uint8)))
                cv2.putText(frame, 'detected', abicissa[2], cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0), 3, cv2.LINE_AA)
                val = content
                found = True
                            
        else: break
        
        cv2.imshow('qr_frame', frame)
        if found: 
            if len(val)>0:
                cv2.waitKey(1000) & 0xFF
                break
        else:
            cv2.waitKey(1) & 0xFF
    
    cv2.destroyAllWindows()
    return val



if __name__ == '__main__':
    print(qr_reader())