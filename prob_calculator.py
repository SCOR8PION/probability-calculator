import copy
import random
class Hat:
    def __init__(self, **kwargs):
        content_dict = kwargs
        content_lst = []
        for k, v in content_dict.items():
            content_lst.append([k, v])
        contents = []
        for i in range(len(content_lst)):
            while content_lst[i][1] > 0:
                contents.append(content_lst[i][0])
                content_lst[i][1] -= 1
        self.contents = contents
        self.copy = copy.deepcopy(self.contents)

    def draw(self, num_balls):
        i = 0
        draw_lst = []
        self.contents = copy.deepcopy(self.copy)
        while i != num_balls:
            if len(self.contents) == 0:
                self.contents = copy.deepcopy(self.copy)
            draw = random.randrange(len(self.contents))
            draw_lst.append(self.contents.pop(draw))
            i += 1
        return draw_lst

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    match = 0
    experiment = 0
    while experiment < num_experiments:
        draw = hat.draw(num_balls_drawn)
        draw_cnt = {}
        for i in draw:
            count = draw.count(i)
            draw_cnt.update({i: count})
        valid = 0
        for i in expected_balls.keys():
            for j in draw_cnt.keys():
                if i == j and expected_balls[i] <= draw_cnt[j]:
                    valid += 1
        if valid == len(expected_balls):
            match += 1
        experiment += 1
    probability = match / num_experiments
    
    return probability