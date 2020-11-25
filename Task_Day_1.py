class ReadTextFile():
    
    def open_file(self, location):
        return open(location,"r")

    
    def file_in_list(self, location):
        file = self.open_file(location)
        matrix = [[],[],[],[],[]]
        count = 0
        for line in file:
            act_line = line.rstrip()
            for element in act_line:
                matrix[count].append(element)
            count += 1
        return matrix
    

class MatrixUpdater():

    def __init__(self, matrix):
        self.old_matrix = matrix
        self.new_matrix = [[".",".",".",".","."],[".",".",".",".","."],[".",".",".",".","."],[".",".",".",".","."],[".",".",".",".","."]]

    def search_bugs(self):
        for line in range(5):
            for elem in range(5):
                if self.old_matrix[line][elem] == "#":
                    self.check_bug(line,elem)
    
    def search_empty(self):
        for line in range(5):
            for elem in range(5):
                if self.old_matrix[line][elem] == ".":
                    self.born_bugs(line, elem)
                
      
    def check_bug(self, line, elem):
        count = 0
        try:
            if line -1 >= 0:
                if self.old_matrix[line-1][elem] == "#":
                    count += 1
        except IndexError:
            pass
        try:
            if self.old_matrix[line+1][elem] == "#":
                count += 1
        except IndexError:
            pass
        try:
            if elem -1 >= 0:
                if self.old_matrix[line][elem-1] == "#":
                    count += 1
        except IndexError:
            pass
        try:
            if self.old_matrix[line][elem+1] == "#":
                count += 1
        except IndexError:
            pass
        if count == 1:
            self.new_matrix[line][elem] = "#"
    
    def born_bugs(self, line, elem):
        count = 0
        try:
            if line -1 >= 0:
                if self.old_matrix[line-1][elem] == "#":
                    count += 1
        except IndexError:
            pass
        try:
            if self.old_matrix[line+1][elem] == "#":
                count += 1
        except IndexError:
            pass
        try:
            if elem -1 >= 0:
                if self.old_matrix[line][elem-1] == "#":
                    count += 1
        except IndexError:
            pass
        try:
            if self.old_matrix[line][elem+1] == "#":
                count += 1
        except IndexError:
            pass
        if count == 1 or count == 2:
            self.new_matrix[line][elem] = "#"

    def print_matrix(self, matrix):
        for line in range(5):
            print(matrix[line])
    
    def get_new_matrix(self):
        self.search_bugs()
        self.search_empty()
        print("Das ist die Eingangsmatrix")
        self.print_matrix(self.old_matrix)
        print("Das ist die neue Matrix")
        self.print_matrix(self.new_matrix)

        

            



if __name__ == "__main__":
    test = ReadTextFile()
    initial_matrix = test.file_in_list("task.txt")
    new_matrix = MatrixUpdater(initial_matrix)
    new_matrix.get_new_matrix()
