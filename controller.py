from view import menu, show_contacts, print_message, input_contact, input_return
import model
from view import text


def start():
    while True:
        choice = menu()
        if choice == 1:
            if not model.phone_book:
                model.open_file()
                print_message(text.open_successful[0])
            else:
                print_message(text.open_successful[1])
        elif choice ==2:
            model.save_file()
        elif choice ==3:
            show_contacts(model.phone_book)
        elif choice == 4:
            new = input_contact(text.input_new_contact)
            model.add_contact(new)
            print_message(text.contact_saved(new.get('name')))
        elif choice == 5:
            word = input_return(text.search_word)
            result = model.search(word)
            show_contacts(result)
        elif choice == 6:
            word = input_return(text.search_word)
            result = model.search(word)
            show_contacts(result)
            index = input_return(text.input_index)
            new = input_contact(text.input_change_contact)
            model.change(int(index), new)
            old_name = model.phone_book[int(index)-1].get('name')
            print_message(text.contact_changed(new.get('name') if new.get('name') else old_name))

        elif choice == 7:
            index = input_return(text.input_delete_index[0])
            if int(index)>len(model.phone_book):
                print_message(text.input_delete_index[1])
            else:
                model.delete_record(int(index))

        elif choice == 8:
            break
