from contacts.contact import Contacts
class LedScreen():

    def display_input(self, input_type, value):
        print "*********************\n"
        print "LED Display\n"
        print "\n\tInput was ", input_type, "\n with value ", value

        if value and value == "View Contacts":
            contacts_obj = Contacts()
            contacts_obj.display_contacts()

        if value and value == "Add Contacts":

            contact_name = raw_input("\n Enter the Name of person  ")

            contact_phone = raw_input("\n Enter the Phone number of person ")

            contacts_obj = Contacts()
            contacts_obj.add_contact(contact_name, contact_phone)

        print "*********************"