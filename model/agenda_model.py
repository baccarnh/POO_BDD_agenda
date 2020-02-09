from model.connection import *
from model.event import *

class AgendaModel():
    '''class to execute SQL statements'''
    def __init__(self):
        self.db = Connection()
         # The class requires an instance of Connection to execute SQL statements


    def add_event(self, the_title, the_day, the_hour, the_description):
        """method adding event and inform the user"""
        self.db.initialize_connection()
        self.db.cursor.execute("INSERT INTO events (title, date, hour, description) VALUES (%s,%s,%s,%s);",
                               (the_title, the_day, the_hour, the_description))
        self.db.connection.commit()
        self.db.close_connection()

    def check_event(self, the_day):
        '''method selecting all events in a given date'''
        self.db.initialize_connection()
        self.db.cursor.execute("SELECT * FROM events WHERE date=%s ;", (the_day,))
        stored_events = self.db.cursor.fetchall()
        self.db.close_connection()
        return stored_events

    """def select_event(self, the_day, the_hour):
        self.db.initialize_connection()
        self.db.cursor.execute("SELECT * FROM events WHERE date=%s AND hour=%s;", the_day, the_hour)
        the_event = self.db.cursor.fetchone()
        self.db.close_connection()
        return the_event"""

    def cancel_event(self, the_day, the_hour ):
        """method selecting one event in given date and hour, delete it and inform the user"""
        self.db.initialize_connection()
        self.db.cursor.execute("SELECT * FROM events WHERE date=%s AND hour=%s;", (the_day, the_hour))
        selected_event = self.db.cursor.fetchone()
        self.db.cursor.execute("DELETE FROM events WHERE date=%s AND hour=%s;", (the_day, the_hour))
        self.db.connection.commit()
        self.db.close_connection()
        return selected_event

    def edit_event(self, the_day, the_hour, new_title, new_description):
        """method selecting an event in given date and hour, edit it and inform the user"""
        self.db.initialize_connection()
        self.db.cursor.execute("SELECT * FROM events WHERE date=%s AND hour=%s;", (the_day, the_hour))
        selected_event= self.db.cursor.fetchone()
        self.db.cursor.execute("UPDATE events SET title=%s, description=%s WHERE date=%s AND hour=%s;",(new_title, new_description, the_day, the_hour))
        self.db.connection.commit()
        self.db.cursor.execute("SELECT * FROM events WHERE date=%s AND hour=%s;", (the_day, the_hour))
        updated_event= self.db.cursor.fetchone()
        self.db.close_connection()
        return selected_event, updated_event

