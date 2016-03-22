import os
from xml.dom import minidom
from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement

class Contacts(object):

    def add_contact(self, contact_name, contact_phone):

        document = ElementTree.parse(os.getcwd() + "/contacts/contacts.xml")

        root = document.getroot()

        contact = ElementTree.SubElement(root, 'contact', {'name': contact_name, 'phone': contact_phone})

        document.write(os.getcwd() + "/contacts/contacts.xml")

        print "New contact has been added "

        print "Updated list of contacts are as follows :"

        print "\n"
        for contact in document.findall('contact'):

            print "\n"+contact.attrib['name'] + " " + contact.attrib['phone'] + "\n"



    def display_contacts(self):

        document = ElementTree.parse(os.getcwd() + "/contacts/contacts.xml")

        # print "contacts ", document.findall('contact')
        print "\n"
        for contact in document.findall('contact'):

            print "\n"+contact.attrib['name'] + " " + contact.attrib['phone'] + "\n"


    def find_contact(self, firstname):
        doc = minidom.parse("contacts.xml")

        print "doc.nodeName ", doc.nodeName
        print "doc.firstChild.tagName ", doc.firstChild.tagName


    def delete_contact(self):
        pass
