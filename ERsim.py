#  File: ERsim.py
#  Description:
#  Student's Name: Julio Gonzalez
#  Student's UT EID: jcg3245
#  Course Name: CS 313E 
#  Unique Number: 51325
#
#  Date Created: 10/10/16
#  Date Last Modified:


class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]

    def printy(self):
        print(self.items)

    def empty(self):
        self.items = []

def main():
    

    critical = Queue()
    serious = Queue()
    fair = Queue()

    f = open ("ERsim.txt", "r")
    for line in f:
        if line[0:3] == "add":
            index = 0
            while index < len(line):
                symbol = line[index]
                if symbol == ".":
                    name = line[4:index]
                index +=1
            if "Critical" in line:
                critical.enqueue(name)
                print("adding",name, "to critical")
                print("Queues are:")
                print("Critical:",end = '')
                critical.printy()
                print("Serious:",end = '')
                serious.printy()
                print("Fair:",end = '')
                fair.printy()
                print()
                
            elif "Serious" in line:
                serious.enqueue(name)
                print("adding",name, "to serious")
                print("Queues are:")
                print("Critical:",end = '')
                critical.printy()
                print("Serious:",end = '')
                serious.printy()
                print("Fair:",end = '')
                fair.printy()
                print()
                
            elif "Fair" in line:
                fair.enqueue(name)
                print("adding",name, "to fair")
                print("Queues are:")
                print("Critical:",end = '')
                critical.printy()
                print("Serious:",end = '')
                serious.printy()
                print("Fair:",end = '')
                fair.printy()
                print()
                
        elif line[0:5] == "treat":
            if "next" in line:
                print("treating next patient")
                if critical.size() != 0:
                    print("Treating '"+critical.peek()+"' from Critical queue")
                    critical.dequeue()
                    print("Queues are:")
                    print("Critical:",end = '')
                    critical.printy()
                    print("Serious:",end = '')
                    serious.printy()
                    print("Fair:",end = '')
                    fair.printy()
                    print()

                else:
                    if serious.size() != 0:
                        print("Treating '"+serious.peek()+"' from Serious queue")
                        serious.dequeue()
                        print("Queues are:")
                        print("Critical:",end = '')
                        critical.printy()
                        print("Serious:",end = '')
                        serious.printy()
                        print("Fair:",end = '')
                        fair.printy()
                        print()
                        
                    else:
                        if fair.size() !=0:
                            print("Treating '"+fair.peek()+"' from Fair queue")
                            fair.dequeue()
                            print("Queues are:")
                            print("Critical:",end = '')
                            critical.printy()
                            print("Serious:",end = '')
                            serious.printy()
                            print("Fair:",end = '')
                            fair.printy()
                            print()
                            
                        else:
                            print("No patients in queue")
            elif "all" in line:
                print("treating all")
                while critical.size() != 0:
                    print("Treating '"+critical.peek()+"' from Critical queue")
                    critical.dequeue()
                    print("Queues are:")
                    print("Critical:",end = '')
                    critical.printy()
                    print("Serious:",end = '')
                    serious.printy()
                    print("Fair:",end = '')
                    fair.printy()
                    print()

                while serious.size() != 0:
                    print("Treating '"+serious.peek()+"' from Serious queue")
                    serious.dequeue()
                    print("Queues are:")
                    print("Critical:",end = '')
                    critical.printy()
                    print("Serious:",end = '')
                    serious.printy()
                    print("Fair:",end = '')
                    fair.printy()
                    print()

                while fair.size() != 0:
                    print("Treating '"+fair.peek()+"' from Fair queue")
                    fair.dequeue()
                    print("Queues are:")
                    print("Critical:",end = '')
                    critical.printy()
                    print("Serious:",end = '')
                    serious.printy()
                    print("Fair:",end = '')
                    fair.printy()
                    print()
                
            elif "Critical" in line:
                if critical.size() != 0:
                    critical.dequeue()
                    print("treating critical")
                    print("Queues are:")
                    print("Critical:",end = '')
                    critical.printy()
                    print("Serious:",end = '')
                    serious.printy()
                    print("Fair:",end = '')
                    fair.printy()
                    print()
                else:
                    print("No patients in queue")
                
            elif "Serious" in line:
                if serious.size() !=0:
                    serious.dequeue()
                    print("treating serious")
                    print("Queues are:")
                    print("Critical:",end = '')
                    critical.printy()
                    print("Serious:",end = '')
                    serious.printy()
                    print("Fair:",end = '')
                    fair.printy()
                    print()
                else:
                    print("No patients in queue")

            elif "Fair" in line:
                if fair.size() != 0:
                    fair.dequeue()
                    print("treating fair")
                    print("Queues are:")
                    print("Critical:",end = '')
                    critical.printy()
                    print("Serious:",end = '')
                    serious.printy()
                    print("Fair:",end = '')
                    fair.printy()
                    print()
                else:
                    print("No patients in queue")
                    
        elif line[0:4] == "exit":
            print("exiting, bye.")
            break
        
main()
