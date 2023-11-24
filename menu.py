
import os
import pierwszy_program as pp
while True:
    os.system("cls")
    print(f'''Moje menu
          Wybierz opcję:
          1. Dodaj kolarza
          2. Wyświetl kolarzy
          3. Edytuj kolarza
          4. Wyjdź z programu''')
    input_user = input("Wybierz opcję: ")
    
    if input_user == "1":
        # print("Dodaję kolarza")
        pp.create_kolarz()
    elif input_user == "2":
        # print("Wyświetlam kolarzy")
        pp.read_kolarze()
    elif input_user == "3":
        # print("Wyświetlam kolarzy")
        nr = int(input(f"Podaj numer startowy: "))
        pp.lista_kolarzy[nr]=pp.read_kolarzeupdate(pp.lista_kolarzy[nr])
    elif input_user == "4":
        #print("Wychodzę z programu")
        os._exit(0)
        break
    input("Naciśnij enter aby kontynuować")