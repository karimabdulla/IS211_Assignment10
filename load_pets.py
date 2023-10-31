import sys
import sqlite3


class PetsDB(object):

    def __init__(self):

        self.conn = sqlite3.connect('pets.db')
        self.cursor = self.conn.cursor()

    def __del__(self):

        try:
            self.cursor = None
            self.conn.close()

            # Print success message
            print("Database closed successfully.")

        except:
            # Print error message
            print("Database could not be closed or wasn't open.")

    def create_schema(self):

        try:
            # Execute the script to (re)create the schema
            self.cursor.executescript('''
                                    DROP TABLE IF EXISTS person;
                                    DROP TABLE IF EXISTS pet;
                                    DROP TABLE IF EXISTS person_pet;

                                    CREATE TABLE person (
                                        id INTEGER PRIMARY KEY,
                                        first_name TEXT,
                                        last_name TEXT,
                                        age INTEGER
                                    );

                                    CREATE TABLE pet (
                                        id INTEGER PRIMARY KEY,
                                        name TEXT,
                                        breed TEXT,
                                        age INTEGER,
                                        dead INTEGER
                                    );

                                    CREATE TABLE person_pet (
                                        person_id INTEGER,
                                        pet_id INTEGER
                                    );
                                ''')
            # Part II: The purpose of the person_pettable is to store the relationships between people and their pets.


            # Commit the schema
            self.conn.commit()

            # Print success message
            print("Created the pets.db schema")

        except:
            # Print error message
            print("Unable to create the pets.db schema")

    def load_data(self):
        """Loads data into the pets.db sqlite database"""

        try:
            # Insert rows into the person table
            self.cursor.executemany("INSERT INTO person VALUES(?, ?, ?, ?)",
                                    (
                                        (1, 'James', 'Smith', 41),
                                        (2, 'Diana', 'Greene', 23),
                                        (3, 'Sara', 'White', 27),
                                        (4, 'William', 'Gibson', 23)
                                    )
                                    )

            # Insert rows into the pet table
            self.cursor.executemany("INSERT INTO pet VALUES(?, ?, ?, ?, ?)",
                                    (
                                        (1, 'Rusty', 'Dalmation', 4, 1),
                                        (2, 'Bella', 'Alaskan Malamute', 3, 0),
                                        (3, 'Max', 'Cocker Spaniel', 1, 0),
                                        (4, 'Rocky', 'Beagle', 7, 0),
                                        (5, 'Rufus', 'Cocker Spaniel', 1, 0),
                                        (6, 'Spot', 'Bloodhound', 2, 1)
                                    )
                                    )

            # Insert rows into the person_pet table
            self.cursor.executemany("INSERT INTO person_pet VALUES(?, ?)",
                                    (
                                        (1, 1),
                                        (1, 2),
                                        (2, 3),
                                        (2, 4),
                                        (3, 5),
                                        (4, 6)
                                    )
                                    )

            # Commit the data
            self.conn.commit()

            # Print success message
            print("Loaded data into pets.db")

        except:
            # Print error message
            print("Unable to load data into pets.db")


def main():

    # Instantiate a PetsDB object
    pets_db = PetsDB()
    # Create the schema
    pets_db.create_schema()
    # Load the data into the schema
    pets_db.load_data()

    # Exit the program after the spreads are printed
    sys.exit()


if __name__ == '__main__':
    main()