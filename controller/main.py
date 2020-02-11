from model.agenda_model import*
from view.agenda_view import *
import time
import calendar
import locale
from datetime import datetime
from controller.cal import *
action = AgendaView()

if __name__ == '__main__':

    choice_user = ""
    choice_view=""
today()
while choice_view != "ev":
    choice_view=input("veuillez saisir su pour voir le mois prochain\n"
                  "pr pour pour voir le mois precedent\n"
                  "ev pour sortir du calendrier").lower()
    if choice_view=='su':
        next_month()
    elif choice_view=='pr':
        last_month()

while choice_user != 'q':
    choice_user = input("Veuillez taper A pour ajouter un evenement \n"
                        " S pour supprimer un evenement \n"
                        " M pour modifier un evenement \n"
                        " C pour consulter \n "
                        "et Q pour quitter").lower()
    if choice_user == 'a':
        action.enter_event()
    if choice_user == 'c':
        action.display_events()
    if choice_user == "s":
        action.delete_event()
    if choice_user == 'm':
        action.modify_event()
exit()