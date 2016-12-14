from Ticket import *
from menus import *

TicketList = [] ##empty list to store tickets

## method to add tickets, just a bunch of inputs and sets from the object class
def addTicket():

    newTicket = Ticket('', '', '')
    message = input('Introduce the ticket ID:\n')
    newTicket.setID(message)
    message2 = input('Introduce the ticket Description:\n')
    newTicket.setDescription(message2)
    message3 = input('Introduce the ticket Priority:\n')
    newTicket.setPriority(message3)
    TicketList.append(newTicket)

## a simple loop to display the ticket list. Index is to make it look slightly nice
def displayList():
    index = 0
    for Tick in TicketList:
        print(index, Tick)
        index = index + 1

## search ticket method, we look for a specific string on the ID field
def searchTicket():

    message4 = input('Introduce the ID of the ticket to search:\n')
    for Tice in TicketList:
        comp = Ticket.getID(Tice)
        if message4 == comp:
            print(Tice)
        else:
            print("There are no tickets with a matching ID")

## delete method, with data validation
def deleteTicket():
    while True:
        try:
            selection = int(input("Introduce the index on the list to delete:\n"))
            break
        except:
            display_error()

    if selection in range(len(TicketList)):
        del TicketList[selection]
        print('Ticket deleted')
    else:
        display_error()

## our main is a big elif block calling the other functions
def main():

    display_initial_message()
    while True:
        display_options_menu()
        main_menu_choice = input('Please select an option from above.\n')
        if main_menu_choice == '1':
            print('adding new ticket')
            addTicket()

        elif main_menu_choice == '2':
            print('Displaying Ticket list')
            displayList()

        elif main_menu_choice == '3':
            print('Searching the ticket list')
            searchTicket()

        elif main_menu_choice == '4':
            print('Deleting ticket')
            displayList()
            deleteTicket()

        elif main_menu_choice == '5':
            exit()

        else:
            display_error()


main()