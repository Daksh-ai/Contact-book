class contact:
    def key(self):
        l=int(input("How Many Contact No You Wants To Add In Contact List:\n"))
        for i in range(l):
            self.a=input("Enter the contact Name:\n")
            self.b=int(input("Enter the Contact No:\n"))
            dict1.update({self.a:self.b})
        return "CONTACT IS ADD TO THE CONTACT LIST"
    def find_con_no(self):
        self.c=input("Enter the contact name:\n")
        if self.c in dict1:
            return "Contact no:{}".format(dict1.get(self.c))
        else:
            return "CONTACT NOT FOUND!"
    def show(self):
        return "{}".format(dict1)
if __name__ == '__main__':
    print("WELCOME TO CONTACT BOOK")
    dict1={}
    instace=contact()
    ip=int(input("1:Add Contact numbers\n2:Find Number\n3:Show Contact List\n"))
    if ip==1:
        print(instace.key())
        op=int(input("Press 2:Find Number\n3:Show contact list\n"))
        if op==2:
            print(instace.find_con_no())
        elif op==3:
            print(instace.show())
    elif ip==2:
        print(instace.find_con_no())
    elif ip==3:
        print(instace.show())
        
        

            


    

        