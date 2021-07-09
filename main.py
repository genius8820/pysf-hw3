import turtle
from turtle import Turtle
import time

def Caesar_cipher_encrypt(strr):
    x=""
    for i in range(0,len(strr)):
        if ord(strr[i])==32:
            x+=" "
        else:
            x+=chr((ord(strr[i])+3))
    return x
    
def Caesar_cipher_decrypt(strr):
    x=""
    for i in range(0,len(strr)):
        if ord(strr[i])==32:
            x+=" "
        else:
            x+=chr((ord(strr[i])-3))
    return x

def Pinpen_cipher_encrypt(strr):
    dictt={"a":chr(5287),"b":chr(8852),"c":chr(5290),"d":chr(8848),"e":chr(9633),
       "f":chr(8847),"g":chr(5283),"h":chr(8851),"i":chr(5285),
       "j":chr(5287)+"x","k":chr(8852)+"x","l":chr(5290)+"x","m":chr(8848)+"x",
       "n":chr(9633)+"x","o":chr(8847)+"x","p":chr(5283)+"x","q":chr(8851)+"x",
       "r":chr(5285)+"x",
       "s":chr(5287)+"o","t":chr(8852)+"o","u":chr(5290)+"o","v":chr(8848)+"o",
       "w":chr(9633)+"o","x":chr(8847)+"o","y":chr(5283)+"o","z":chr(8851)+"o"}
    x=""
    for i in range(0,len(strr)):
        if strr[i] in dictt and strr[i]!=" ":
            y=dictt[strr[i]]
            x+=y[0:2]
        else:
            x+=" "        
    return x

def Pinpen_cipher_decrypt(strr):
    dictt={chr(5287):"a",chr(8852):"b",chr(5290):"c",chr(8848):"d",chr(9633):"e",
       chr(8847):"f",chr(5283):"g",chr(8851):"h",chr(5285):"i",
       chr(5287)+"x":"j",chr(8852)+"x":"K",chr(5290)+"x":"l",
       chr(8848)+"x":"m",chr(9633)+"x":"n",chr(8847)+"x":"o",chr(5283)+"x":"p",chr(8851)+"x":"q",
       chr(5285)+"x":"r",
       chr(5287)+"o":"s",chr(8852)+"o":"t",chr(5290)+"o":"u",chr(8848)+"o":"v",
       chr(9633)+"o":"w",chr(8847):"x"+"o",chr(5283)+"o":"y",chr(8851)+"o":"z"}
       
    x=""
    z=""
    for i in range(0,len(strr)):
        if strr[i]==" ":
            x+=" "
        elif i!=len(strr)-1 and (strr[i+1]=="x" or strr[i+1]=="o"):
            z=strr[i]+strr[i+1]
        else:
            z=strr[i]
            
        if z in dictt:
            y=dictt[z]
            x+=y
    return x


def Photographic_encryption(strr):
    evan=turtle.Turtle()

    #darksage color changed with goldenrod because it isn't exist in turtle color lists   
    dictt={" ":"black", "a":"gray", "b":"silver", "c":"whitesmoke", "d":"rosybrown", "e":"firebrick", "f":"red", "g":"darksalmon",
        "h":"sienna", "i":"sandybrown", "j":"bisque", "k":"tan", "l":"moccasin", "m":"floralwhite", "n":"gold",
        "o":"darkkhaki", "p":"lightgoldenrodyellow", "q":"olivedrab", "r":"chartreuse", "s":"goldenrod", "t":"lightgreen",
        "u":"green", "v":"mediumseagreen", "w":"mediumaquamarine", "x":"mediumturquoise", "y":"darkslategray", "z":"cyan" }    

    x,y=-350,250
    for i in range(0,len(strr)):
        if strr[i] in dictt:
            color=dictt[strr[i]]
        else:
            continue

        if x==350:
            x=-350
            y-=50
        
        evan.penup()
        evan.goto(x,y)
        evan.fillcolor(color)
        evan.begin_fill()
        evan.goto(x,y+50)
        evan.goto(x+50,y+50)
        evan.goto(x+50,y)
        evan.goto(x,y)
        evan.end_fill()

        x+=50
        
        if i==len(strr)-1:
            time.sleep(7)


n1=int(input("Please select your cypher type(1-Caesar cipher, 2-Pig pen, 3-Photographic encryption): "))
if n1==3:
    str1=input("Please enter your text: ")
else:
    n2=int(input("Enter your operation(1-encrypt, 2-decrypt): "))
    if n1==2 and n2==2:
        print("""you can copy this encrypted pig pen characters
        a( ᒧ ),b( ⊔ ), c( ᒪ ), d( ⊐ ), e( □ ), f( ⊏ ), g( ᒣ ), h( ⊓ ), i( ᒥ ), j( ᒧx ), k( ⊔x ) ,l( ᒪx ), m( ⊐x ),
        n( □x ), o( ⊏x ), p( ᒣx ), q( ⊓x ), r( ᒥx ), s( ᒧo ), t( ⊔o ), u( ᒪo ), v( ⊐o ), w( □o ), x( ⊏o), y( ᒣo ),Z( ⊓o )
        """)
        str1=input("Please enter your text: ")
    else:
        str1=input("Please enter your text: ")


strr=str1.lower()

if n1==1 and n2==1:
    print("Encrypted text is: ",Caesar_cipher_encrypt(strr))
elif n1==1 and n2==2:
    print("Decrypted text is: ",Caesar_cipher_decrypt(strr))
elif n1==2 and n2==1:
    print("Eecrypted text is: ",Pinpen_cipher_encrypt(strr))
elif n1==2 and n2==2:
    print("Decrypted text is: ",Pinpen_cipher_decrypt(strr))
elif n1==3:
    Photographic_encryption(strr)