from itertools import chain

# 1 
class FlatIterator:
    def __init__(self, list):
        self.main_list = list

    def __iter__(self):
        self.main_cursor = 0
        self.nested_cursor = -1
        return self

    def __next__(self):
        self.nested_cursor += 1
        if self.nested_cursor == len(self.main_list[self.main_cursor]):
            self.main_cursor += 1
            self.nested_cursor = 0
            if self.main_cursor == len(self.main_list):
                raise StopIteration
        return self.main_list[self.main_cursor][self.nested_cursor]


# 2 
def flat_generator(main_list):
    for mail_item in main_list:
        for item in mail_item:
            yield item