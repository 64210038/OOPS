#switch_procedure.py
switch_status = False #สถานะของไฟเปิดปิด
def turnon() : #เปิดไฟ
    global switch_ststus
    switch_ststus = True
    print("ไฟเปิด")

def turoff() : #ปิดไฟ
    global switch_ststus
    sswitch_status = False
    print ("ไฟปิด")


if __name__=="__main__":
    print (f'สถานะไฟ: {switch_status}')
    turnon()
    turoff()