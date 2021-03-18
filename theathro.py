andr=int(input("dwse tous andres theates: "))
gyn=int(input("dwse tis gynaikes theates: "))
paid=int(input("dwse ta paidia theates: "))
pli8=andr+gyn+paid
print("tin parastasi parakolou8isan",pli8,"8eates")
print("apo autous ta paidia itan se pososto",paid/pli8*100,"%")
print("oi andres itan se pososto",andr/(pli8-paid)*100,"%")
