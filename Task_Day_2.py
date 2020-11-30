
class ReadTextFile():
    
    def open_file(self, location):
        return open(location,"r")

    def read_in_file(self, location):
        file = self.open_file(location)
        read_in = file.read()
        return read_in
    
    def creat_list(self, location):
        read_in = self.read_in_file(location)
        rare_list = list(read_in)
        input_list = []
        for line in range(len(rare_list)):
            if rare_list[line] != ",":
                input_list.append(rare_list[line])
        return input_list
    
    def change_input(self, location):
        correct_input_list = self.creat_list(location)
        correct_input_list[1] = "12"
        correct_input_list[2] = "2"
        return correct_input_list

class CreatSplitList():

    def __init__(self):
        self.split_list = []
        self.input_list = []
    
    def set_input_list(self,input_list):
        self.input_list = input_list
        

    def create_list(self):
        elem = 4
        column = int(len(self.input_list)/4)
        self.split_list = [[0 for x in range(elem)] for x in range(column)]
    

    def fill_list(self):
        count = 0
        count_2 = 0
        while count < int(len(self.input_list)/4):
            count_1 = 0
            count_2 = 0
            while count_1 < 4:
                self.split_list[count][count_1] = self.input_list[count_2]
                count_2 += 1
                count_1 += 1
            count += 1

    def full_cycle(self,input_list):
        self.set_input_list(input_list)
        self.create_list()
        self.fill_list()



class Move():

    def __init__(self, split_list_object):
        self.split_list_object = split_list_object

    def play(self, input_list):
        count = 0
        print("start")
        self.split_list_object.full_cycle(input_list)
        split_list = self.split_list_object.split_list
        while count < len(input_list)/4 -1:
            print("count= ")
            print(count)
            if self.check_first(split_list[count][0]) == "Add":
                input_list[int(split_list[count][3])] = self.add_value(input_list[int(split_list[count][1])], input_list[int(split_list[count][2])])
            if self.check_first(split_list[count][0]) == "multi":
                input_list[split_list[count][3]] = self.multiply_value(input_list[split_list[count][1]], input_list[split_list[count][2]])
            if self.check_first(split_list[count][0]) == "end":
                print("FERTIG")  
            count += 1
            self.split_list_object.full_cycle(input_list)
            split_list = self.split_list_object.split_list
        return input_list[0]


    def check_first(self, value):
        if value == "1":
            return "Add"
        if value == "2":
            return "multi"
        if value == "99":
            return "end"
        else:
            return False
    

    def add_value(self, first, second):
        return first + second
    
    def multiply_value(self, first, second):
        return first * second





if __name__ == "__main__":
    input_value = ReadTextFile()
    input_list = input_value.change_input("input_day_2.txt")
    print(len(input_list))
    split_list_object = CreatSplitList()
    move = Move(split_list_object)
    print(move.play(input_list))
