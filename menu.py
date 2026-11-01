#Modulo menu para a agenda de contatos
#Descrição: Modulo que contém as funções de menu para a agenda de contatos
#---------------------------------------------------------------------------
#Classe ContactBook
#Descrição: Classe que representa a agenda de contatos
#Atributos:
#contact_book: Dicionário que contém os contatos da agenda
#Métodos:
#display_menu: Exibe o menu de escolha ao usuario
#add_contact: Adiciona um contato à agenda
#view_contact: Exibe informações de um contato da agenda
#edit_contact: Edita informações de um contato da agenda
#delete_contact: Exclui um contato da agenda
#list_all_contacts: Exibe todos os contatos da agenda
class ContactBook:
    def __init__(self):
        self.contact_book = {}

    def display_menu(self):
        print("Contact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. List All Contacts")
        print("6. Exit")

    def add_contact(self):
        name = input("Enter contact name: ")
        phone = input("Enter contact phone: ")
        email = input("Enter contact email: ")
        address = input("Enter contact address: ")
        if name in self.contact_book:
            print("Contact already exists!")
        else:
            self.contact_book[name] = {"phone": phone, "email": email, "address": address}
            print("Contact added successfully!")

    def view_contact(self):
        name = input("Enter contact name: ")
        if name in self.contact_book:
            print(f"Contact: {name}")
            print(f"Phone: {self.contact_book[name]['phone']}")
            print(f"Email: {self.contact_book[name]['email']}")
            print(f"Address: {self.contact_book[name]['address']}")
        else:
            print("Contact not found!")


    def edit_contact(self):
        name = input("Enter contact name: ")
        if name in self.contact_book:
            print(f"Editing contact: {name}")
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            self.contact_book[name] = {"phone": phone, "email": email, "address": address}
            print("Contact updated successfully!")
        else:
            print("Contact not found!")

    def delete_contact(self):
        name = input("Enter contact name: ")
        if name in self.contact_book:
            del self.contact_book[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    def list_all_contacts(self):
        if self.contact_book == {}:
            print("No contacts in the book!")
            return
        else:
            print("All contacts:")
            for name in self.contact_book:
                print(f"Contact: {name}")
                print(f"Phone: {self.contact_book[name]['phone']}")
                print(f"Email: {self.contact_book[name]['email']}")
                print(f"Address: {self.contact_book[name]['address']}")
                print("-----------------")