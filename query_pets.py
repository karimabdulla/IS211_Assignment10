import sys
import load_pets

def display_person(id, pets_db):

    # Select the person with the provided ID number
    person = (pets_db.cursor.execute('''
                SELECT  first_name,
                        last_name,
                        age
                FROM person
                WHERE id = (? )
            ''', (id,))).fetchall()

    # Check to see if a record could be found for the ID number
    if len(person) > 0:
        print("\n{} {}, {} years old.".format(person[0][0],
                                              person[0][1], person[0][2]))

        # Select pets that belong to the person
        pets = (pets_db.cursor.execute('''
                SELECT  name,
                        breed,
                        age,
                        dead
                FROM pet
                INNER JOIN person_pet
                on person_pet.pet_id = pet.id
                WHERE person_pet.person_id = (? )
            ''', (id,))).fetchall()

        # Check to see if pets could be found for the ID number
        if len(pets) > 0:
            for pet in pets:
                print("{} {} {} {}, a {}, that {} {} years old." \
                    .format(
                    person[0][0],
                    person[0][1],
                    "owns" if pet[3] == 0 else "owned",
                    pet[0],
                    pet[1],
                    "is" if pet[3] == 0 else "was",
                    pet[2]
                )
                )

        else:
            print("{} {} owned no pets.".format(person[0][0],
                                                person[0][1]))

        # Print new line for readability
        print("\n")

    else:
        print("Unable to locate a person with that ID number, please try again.")


def get_id():

    try:
        id = int(input('Enter a person ID # or -1 to exit: '))
        return id

    except ValueError:
        print('Please enter a valid numerical person ID')
        get_id()


def main():

    # Use the PetsDB class to connect to the pets.db sqlite database
    pets_db = load_pets.PetsDB()

    # Track if the user wishes to exit
    exit_signal = False

    while not exit_signal:
        id = get_id()

        if id == -1:
            print('Received entry of -1. Exiting program.')
            exit_signal = True

        else:
            display_person(id, pets_db)

    sys.exit()


if __name__ == '__main__':
    main()