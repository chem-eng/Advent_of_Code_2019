
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




if __name__ == "__main__":
    test = ReadTextFile()
    print(test.creat_list("input_day_2.txt"))

