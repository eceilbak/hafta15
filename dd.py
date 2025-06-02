vnot=int(input("vize notunuzu girin"))
fnot=int(input("final notunuzu girin"))
ort=vnot*40/100+fnot*60/100
if 50<=ort<=100:
    print(f"notunuz {ort} harfiniz A")
elif 20<=ort<=50:
    print(f"notunuz {ort} harfiniz B")
else:
    print(f"notunuz {ort} harfiniz C")
