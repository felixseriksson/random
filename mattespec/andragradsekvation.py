while True:
    print("tryck 'a' för att avsluta")
    p1=input("Ange p:")

    if p1 == 'a':
        break
    else:
        q1=input("Ange q:")
        p=int(p1)
        q=int(q1)
        x1=((-p/2)+(((p/2)**2-q)**0.5))
        x2=((-p/2)-(((p/2)**2-q)**0.5))
        if int((p/2)**2-q)<0:
            x1=round(x1.real, 2) + round(x1.imag, 2)*1j
            x2=round(x2.real, 2) + round(x2.imag, 2)*1j

        print("Lösningarna är x1=", x1, " och x2=", x2)
        break
        