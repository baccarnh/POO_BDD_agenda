from model.agenda_model import *

class AgendaView():
    def __init__(self):
        self.rdv = AgendaModel()


    def enter_event(self):
        the_title= input ("Enter the title: ")
        the_day= input("Enter the date: ")
        the_hour = input("Enter the hour: ")
        the_description=input ("Enter the description: ")
        self.rdv.add_event(the_title, the_day, the_hour, the_description)

    def display_events(self):
        the_day=input("enter the date that you want to check events:")
        events_list = self.rdv.check_event(the_day)

        if events_list==[]:
            print (f"you have no stored event in {the_day}")
        else:
            for element in events_list:
                print(f"there are all events for {the_day} : at {element['hour']} \n"
                  f"which title is {element['title']} and description is {element['description']}")

    def delete_event(self):
        the_day=input("enter the event's date that you want to delete :")
        the_hour=input("enter the event's hour that you want to delete :")
        deleted_event= self.rdv.cancel_event(the_day, the_hour)
        if deleted_event==None:
            print ("there is no event in date and hour given")
        else:
            print ("the event {} has been deleted".format(deleted_event))

    def modify_event(self):
        the_day = input("enter the event's date that you want to edit :")
        the_hour = input("enter the event's hour that you want to edit :")
        new_title = input("enter the new event's title that you want to replace :")
        new_description = input("enter the new event's descripition that you want to replace :")
        (selected_event, new_event)=self.rdv.edit_event(the_day, the_hour, new_title, new_description)
        print("the {} event has been replaced by {}". format(selected_event, new_event))