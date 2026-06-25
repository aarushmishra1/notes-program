x = 'yes'

while x == 'yes':
    user_input = input("Would you like to add anything to the note? (yes/no): ").strip().lower()

    if user_input == 'yes':
        note = input("What would you like to add to the note? : ")
        print("NOTED!")

    if user_input == 'no':
        print("Got it!")
        note = input("If you change your mind and want to add a note, press Enter: ")

        if note == '':
            continue
        else:
            print("It seems like you want to exit the program.")
            exit_input = input("Press Enter to exit, or type anything else to continue: ")

            if exit_input == '':
                break
            else:
                continue

    if user_input != 'yes' and user_input != 'no':
        print("Invalid syntax")

    continue

