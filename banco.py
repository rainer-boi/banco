saldo_inicial=500
total_giros=0
total_depo=0

ciclo=True
while ciclo:
    print('''
        Sistema Bancario
        1) Girar
        2) Depositar
        3) Estado de cuenta
        4)Salir
        ''')
    try:
        op=int(input("Seleccione: "))
        match op:
            case 1:
                print("Girar dinero")
                while True:
                    try:
                        giro=int(input("Ingrese monto a girar: "))
                        if giro>=5000:
                            break
                        else:
                            print("Ingrese valor mayor o igual a 5000")
                    except ValueError:
                        print("Ingrese números")
                
                if saldo_inicial>=giro:
                    saldo_inicial-=giro
                    print(f"Giro: {giro}")
                    print(f"Nuevo saldo: {saldo_inicial}")
                else:
                    print(f"Saldo insuficiente, ud posee: {saldo_inicial}")
                total_giros=total_giros+giro
            case 2:
                print("Depositar dinero")
                while True:
                    try:
                        deposito=int(input("Ingrese monto a depositar: "))
                        if deposito>=1000 and deposito<=300000:
                            break
                        else:
                            print("Límite de depósito entre 1000 y 300000")
                    except:
                        print("Ingrese números")
                saldo_inicial=saldo_inicial+deposito
                total_depo=total_depo+deposito
            case 3:
                print("Estado de cuenta")
                print(f"Saldo: {saldo_inicial}")
                print(f"Depositos: { total_depo}")
                print(f"Giros: {total_giros}")
            case 4:
                ciclo=False
            case _:
                print("Opción incorrecta")
    except ValueError:
        print("Solo debe ingresar un número")