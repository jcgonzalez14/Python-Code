#  File: Queens.py
#  Description:
#  Student's Name: Julio Gonzalez
#  Student's UT EID: jcg3245
#  Course Name: CS 313E 
#  Unique Number: 51325
#
#  Date Created: 11/8/16
#  Date Last Modified: 11/11/16

class QueensProblem:

    def __init__(self, size):
        self.size = size
        self.numbers = []
        self.answer = []
        self.solve(0)

    def solve(self, ball):
        if ball == self.size:
            self.answer.append(self.putittogether(self.numbers))
        else:
            for i in range(self.size):
                if self.isValidPlace(i):
                    self.numbers.append(i)
                    self.solve(ball + 1)
                    self.numbers.pop()

    def isValidPlace(self, foot):
        batman = len(self.numbers)
        for i in range(batman):
            if self.numbers[i] == foot or abs(batman - i) == abs(foot - self.numbers[i]):
                return False
        return True

    def putittogether(self, toy):
        horn = []
        for i in range(len(toy)):
            horn.append(' * ' * toy[i] + ' Q ' + ' * ' * (self.size - toy[i] - 1))
        return horn

    def __str__(self):
        string = ""
        git = 0
        for i in self.answer:
            count = 0
            for j in i:
                if count % self.size == 0:
                    git += 1
                    string += "\n"
                    string += "Solution # "
                    string += str(git)
                    string += "\n"
                string += j
                string += "\n"
                count += 1

        return(string)
        
        
        
        

def main():

    size = eval (input ("Enter the size of the square board: "))

    while size < 4:
        print("Invalid input")
        size = eval (input ("Enter the size of the square board: "))

    s = QueensProblem(size)
    print(s)
    



main()
