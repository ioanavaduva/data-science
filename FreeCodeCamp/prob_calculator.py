import random
import copy 
import collections

class Hat:

    def __init__(self, **kwargs):
        self.contents = self.__process_contents(kwargs)


    def __process_contents(self, arguments):
        list_of_lists_content = []
        for key, value in arguments.items():
            list_of_lists_content.append([key]*value)
        
        list_content = [item for sublist in list_of_lists_content for item in sublist]

        return list_content


    def draw(self, num_balls): # num_balls is a number
        output_balls = []
        if num_balls >= len(self.contents):
            output_balls = self.contents
            self.contents = []
        else:
            for _ in range(num_balls):
                nr = random.randint(0, len(self.contents)-1)
                output_balls.append(self.contents[nr])
                self.contents.remove(self.contents[nr])

        return output_balls
    
def dict_includes(expected, actual):
    for key, value in expected.items():
        if key not in actual:
            return False
        if value > actual[key]:
            return False
    return True


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    m=0
    for _ in range(0, num_experiments):
        drawn = collections.Counter(copy.deepcopy(hat).draw(num_balls_drawn))

        if dict_includes(expected_balls, drawn):
            m = m+1

        else:
            pass

    probability = m/num_experiments

    return probability


    

hat1 = Hat(black=6, red=4, green=3)
# print(hat1.contents)
# print(hat1.draw(2))
# print(hat1.contents)
# print(hat1.draw(3))
# print(hat1.contents)
# print(hat1.draw(9))
# print(hat1.contents)
probability = experiment(hat=hat1, expected_balls={"red":2,"green":1}, num_balls_drawn=5, num_experiments=10)
print(probability)