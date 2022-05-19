import time
def conv_a_seg(hh,mm,ss):
    HH=hh*3600
    MM=mm*60
    SS=ss
    tTotal=HH+MM+SS
    return tTotal
print(conv_a_seg(1,1,6))

def conv_a_hhmmss(tTotal):
    horas=tTotal/3600
    hh=int(horas//1)
    decHoras=horas-hh #esto da los decimales de la hora para calcular los minutos
    minutos=decHoras*60
    mm=int(minutos//1)
    decMinutos=minutos-mm
    seg=decMinutos*60
    ss=int(seg//1)
      
    print (f"{hh:.0f}:{mm:.0f}:{ss:.0f}")

conv_a_hhmmss(3666)

def temporizador(hh,mm,ss):
    if hh>=60 or mm>=60 or ss>=60:
        print("Ingrese valores correctos")
        
    else:
        tTotal=conv_a_seg(hh,mm,ss)

        while tTotal>0:
            tTotal-=1
            time.sleep(0.6)
            #print(tTotal)
            conv_a_hhmmss(tTotal)
            if hh==0 and mm==0 and ss==0:
                break
       

temporizador(0,1,6)