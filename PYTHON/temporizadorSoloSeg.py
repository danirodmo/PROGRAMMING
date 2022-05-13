import time
def temporizador(hh,mm,ss):
    if hh>=60 or mm>=60 or ss>=60:
        print("Ingrese valores correctos")

    while hh>=0 and mm>=0 and ss>=0:
        time.sleep(1)
        ss-=1
        if ss==0 and mm>0:
            mm-=1
            ss=59
        if mm==0 and hh>0:
            hh-=1
            mm=59
            ss=59
        print(f"{hh}:{mm}:{ss}")
temporizador(1,10,6)