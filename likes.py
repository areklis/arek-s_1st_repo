def likes(like=[]):
    
    if   (len(like)==0) :return("no one likes this")
    elif (len(like)==1) :return(like[0],"likes this")
    elif (len(like)==2) :return(f'{str(like[0])}, {like[1]}, like this')
    elif (len(like)==3) :return(f'{str(like[0])}, {like[2]} and {like[1]} like tihs')
    else : return(f'{str(like[3])}, {like[0]} and {len(like)-2} others like this')
    
