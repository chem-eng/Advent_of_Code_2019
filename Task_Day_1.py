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
        #print("Das ist die Eingangsmatrix")
        #self.print_matrix(self.old_matrix)
        #print("Das ist die neue Matrix")
        #self.print_matrix(self.new_matrix)
        return self.new_matrix

class SafeMatrix():

    def __init__(self):
        self.master_list = []

    def save_matrix(self, matrix):
        self.master_list.append(matrix)
         

            
class CompareMatrix():

    def __init__(self):
        pass

    def compare(self, master_list, current_list):
        list_counter = 0
        while list_counter < len(master_list)-1:
            if current_list[0] == master_list[list_counter][0]:
                 if current_list[1] == master_list[list_counter][1]:
                      if current_list[2] == master_list[list_counter][2]:
                           if current_list[3] == master_list[list_counter][3]:
                                if current_list[4] == master_list[list_counter][4]:
                                    return list_counter
            list_counter += 1
        return False
        
                
class CalculatBiodivers():

    def __init__(self):
        pass

    def get_exponent(self, line, elem):
        exponent = 0
        if line == 0:
            exponent = elem
        if line == 1:
            exponent = elem +5
        if line == 2:
            exponent = elem +10
        if line == 3:
            exponent = elem + 15
        if line == 4:
            exponent = elem + 20
        return exponent
    
    def get_expo_list(self,matrix):
        exponents = []        
        for line in range(5):
            for elem in range(5):
                if matrix[line][elem] == "#":
                    exponents.append(self.get_exponent(line, elem))
        return exponents
    
    def calc_Bio(self, exp_list):
        result = 0
        for count in range(len(exp_list)):
            result += pow(2,exp_list[count])
        return result

    
    
        

if __name__ == "__main__":
    read_text = ReadTextFile()
    initial_matrix = read_text.file_in_list("task.txt")
    #test_matrix = read_text.file_in_list("test_matrix.txt")
    master = SafeMatrix()
    master.save_matrix(initial_matrix)
    compare_matrix = CompareMatrix()
    old_matrix = initial_matrix
    first_list = False
    count = 0
    while count < 100:
        new_matrix = MatrixUpdater(old_matrix)
        master.save_matrix(new_matrix.get_new_matrix())
        old_matrix = new_matrix.get_new_matrix()
        first_list = compare_matrix.compare(master.master_list,old_matrix)
        if first_list is not False:
            print("Geschafffft")
            break
        count += 1
        print(count)
    print("##################")
    print(first_list)
    print("Ergebniss:")
    bio = CalculatBiodivers()
    result = bio.calc_Bio(bio.get_expo_list(master.master_list[first_list]))
    print(result)

