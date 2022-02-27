#!/usr/bin/python3
import argparse
import sys
import os
import mailbox
import re
from collections import OrderedDict
from email.parser import BytesParser
from email.policy import default

count=0; #global variable to count the total occurence of search strings

# Function print out the header and date of emails that matches all the terms given by the user 
# function first called the read_email_payload method to parse the body of each email
# then it compare it against the search_clean list, the search list provided by the user
# if there is a match within the body, the function printout the count number, from and date header
def term_search(self, inboxName, search_clean):
    global count
    for search_term in search_clean:
        for i, message in enumerate(self):
            message = str(read_email_payload(message))
            if(len(re.findall('\\b'+search_term+'\\b', message)) > 0 ):
                print("INBOX:", inboxName)
                print("-------------------------")
                for email in self:
                    print("%d. <%s>, %s" %(count, email['from'], email['date']))
                    count+=1;
                print("-------------------------\n")

# Function obtain all the emails exchanged by two people
# regardless of who initiated the communication in the first place
# This is accomplished by compare the from and to header of each mbox mailbox
# if from is match with the first email and to is matched with the second and vice versa, output on the screen
# the relationship between 2 emails.
def interactive_search(self, inboxName, search_clean):
    global count

    #print("from: ",search_clean[0])
    #print("to: ",search_clean[1])
    for email in self:
         if(email['from'] == search_clean[0] and  email['to'] == search_clean[1] ):
             print("%d. <%s> -> <%s> [%s] %s\n" %(count, email['from'],email['to'], email['subject'],email['date']))
             count+=1;

         elif(email['from'] == search_clean[1] and  email['to'] == search_clean[0] ):
             print("%d. <%s> -> <%s> [Subject:%s] %s\n" %(count, email['to'],email['from'], email['subject'],email['date']))
             count+=1;
# Function read parse the mbox and return the body of each mbox mailbox  as a string
def read_email_payload(self):
        message = self
        if message.is_multipart():
            content = ''.join(part.get_payload(decode=True) for part in message.get_payload())
        else:
            content = message.get_payload(decode=True)
        return content

# The function clean the user input of duplicates, case-sensivity, order.
# The search_input is first join from  multiple arguments into a list, split by a space.
# The joined input then convert into lower case per character
# Finally, the input is searched and removed duplicate term and return the final cleaned input
def input_clean(search_input):
    search_input = str(' '.join(search_input)).split(" ") 
    for i in range(len(search_input)):
        search_input[i] = search_input[i].lower()
    cleaned_input = list(OrderedDict.fromkeys(search_input))
    
    return cleaned_input
    


def main():
    try:
        #help menu for the program
        parser=argparse.ArgumentParser(
        usage='enron_search term [term ...]', #usage option
        description='Welcome to Forensics Email Analyzer',
        epilog="This program was coded by Tri Nguyen and Ryan Salinas!!")

        
        parser.add_argument('-tS', '--term_search',  nargs='+', help='Enter keyword(s) to search in dataset')
        parser.add_argument('-aS', '--address_search', nargs='+', help='obtain all the emails sent and received by a given by the user')

        parser.add_argument('-iS', '--interaction_search', nargs='+', help='obtain all the emails exchanged by two people regardless of who initiated the communication in the first place')
        args=parser.parse_args() #parsed all arguments into args
        
        search_str =[] #array for term_search
        a_search=[] #array for address_search
        int_search=[] #array for interaction_search


        # if no argument are given, print help screen and exit
        if (len(sys.argv)==1):
            parser.print_help()
            exit(1)


        if(args.term_search != None):
            search_clean= input_clean(args.term_search)

        elif(args.address_search != None):
            search_clean= input_clean(args.address_search)

        elif(args.interaction_search != None):
            search_clean= input_clean(args.interaction_search)
 
       
        rootDir='.' #root directory where all the enron mbox files are located:
        for (root,dirs,files) in os.walk(rootDir, topdown=False):
            for inbox in files:
                mbox = mailbox.mbox(inbox,create=False)
                if (args.term_search is not None): 
                    term_search(mbox, inbox, search_clean)
                elif (args.interaction_search is not None):
                    interactive_search(mbox, inbox, search_clean)

        global count
        print("result found:",count) #print the total results


    #if user press CtrlC, print message and exit the program
    except KeyboardInterrupt:
        print("\nExiting the program, goodbye!")
        sys.exit(0)

if (__name__ == "__main__"):
    main()
