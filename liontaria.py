def meiwsi(pli=23000,et=0):
    if(pli>6000):
        pli-=pli*0.02
        et+=1
        return meiwsi(pli,et)
    else:return et
