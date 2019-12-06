class Destination:

    def __init__(self):
        self.country="hi"
        self.distance=0
        self.airport=""
        self.contactName=""
        self.contactNumber=0
        self.cancel=0

    def addInfo(self):
        self.country=input("Country: ")
        if self.country=="CANCEL":
            self.country=1
            return 0
        self.distance=input("Distance: ")
        if self.distance=="CANCEL":
            self.distance=1
            return 0
        self.airport=input("Airport: ")
        if self.airport=="CANCEL":
            self.airport=1
            return 0
        self.contactName=input("Contact name: ")
        if self.contactName=="CANCEL":
            self.contactName=1
            return 0
        self.contactNumber=input("Contact number: ")
        if self.name=="CANCEL":
            self.cancel=1
            return 0


#if __name__ == '__main__':
#    des=Destination()
#    print(des.country)
