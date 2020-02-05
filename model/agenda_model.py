from .connection import Connection

class AgendaModel:
    '''class to execute SQL statements'''
    def __init__(self):
        self.db = Connection()
    # The class requires an instance of Connection to execute SQL statements

    def check_event(self):
        '''method selecting all events in a given date'''
        self.db.initialize_connection()
        self.db.cursor.execute("SELECT * FROM events WHERE date=%s ;", the_day,)
        stored_events = self.db.cursor.fetchall()
        self.db.close_connection()
        return stored_events

    def cancel_event(self):
        '''method selecting one event in given date and hour, delete it and inform the user '''
        self.db.initialize_connection()
        self.db.cursor.execute("SELECT * FROM events WHERE date=%s AND hour=%s;", the_day, the_hour )
        the_event = self.db.cursor.fetchone()
        self.db.cursor.execute("DELETE FROM events WHERE date=%s AND hour=%s;", the_day, the_hour)
        self.db.connection.commit()
        self.db.close_connection()
        return "the event {} has been deleted".format(the_event)

    def edit_event(self):
        '''method selecting an event in given date and hour, edit it and inform the user '''
        self.db.initialize_connection()
        self.db.cursor.execute("SELECT * FROM events WHERE date=%s AND hour=%s;", the_day, the_hour)
        event_to_update= self.db.cursor.fetchone()
        self.db.cursor.execute("UPDATE events SET title=%s, description=%s WHERE date=%s AND hour=%s;",new_date, new_description,  the_day, the_hour)
        updated_event=self.db.cursor.fetchone()
        self.db.connection.commit()
        self.db.close_connection()
        return "the event {} has been replaced by {}".format(event_to_update, updated_event)

    def add_event(self, event):
        '''method adding event and inform the user '''
        self.db.initialize_connection()
        self.db.cursor.execute("INSERT INTO events (title, date, hour, description) VALUES (%s,%s,%s,%s);",
                               (event.title, event.date, event.hour, event.description))
        self.db.connection.commit()
        self.db.close_connection()