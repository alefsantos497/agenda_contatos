#Projeto Agenda de Contatos
#Autor: Alef
#Versao: 1.0
#Data: 01-11-2026
#Descricao: Projeto de uma agenda de contatos em Python
import menu #Importando o modulo menu

contact_book = menu.ContactBook()
#Loop principal do programa
#Exibe o menu de escolha ao usuario
#Lê a escolha do usuario
#Executa a ação correspondente
#Se a ação for inválida, exibe uma mensagem de erro
#Se a ação for válida, executa a ação
#Se a ação for 6, sai do loop
while True:
    contact_book.display_menu()
    choice = input("Enter your choice: ")
    #Validando a entrada do usuario
    #Se a entrada não for um número inteiro, exibe uma mensagem de erro
    #Se a entrada for um número inteiro, executa a ação correspondente
    try:
        choice = int(choice)
    except ValueError:
        print("Invalid choice! Please enter a number.")
        continue
    if choice == 1:
        print("")
        contact_book.add_contact()
    elif choice == 2:
        print("")
        contact_book.view_contact()
    elif choice == 3:
        print("")
        contact_book.edit_contact()
    elif choice == 4:
        print("")
        contact_book.delete_contact()
    elif choice == 5:
        print("")
        contact_book.list_all_contacts()
    elif choice == 6:
        print("Exiting the book...")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")
