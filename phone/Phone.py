from button.button import NumericButton, FunctionButton


class Phone(object):

    print " \n\n A) For Numeric input press 0 to 9 "
    print " B) For Using Function Buttons, Type  'Home' or 'View Contacts' or 'Add Contacts' or 'Call' or 'Disconnect' "

    accepted_strings = {"Home", "Call", "Disconnect", "View Contacts", "Add Contacts"}

    user_input = raw_input("\n what you want to do ?? ")

    print "\n you opted for ", user_input, "\n"

    if user_input:

        try:

            int_value = int(user_input)

            phone_button = NumericButton()

            phone_button.button_pressed(int_value)

        except ValueError:

            if user_input in accepted_strings:

                phone_button = FunctionButton()

                phone_button.button_pressed(user_input)

            else:

                print "This option is not supported, will come in next release :)"
