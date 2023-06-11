
while True:
    try:
        myInt = int(input("num enter: "))
    except:
        print("Gerçek numara giriniz")
        continue
    else:
        print("Teşekkürler (else)")
        break
    finally:
        print("finally çağırıldı")