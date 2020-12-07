class Bag:
    
    def __init__(self, bag_instruction):
        self.instructions = bag_instruction
        self.color = None
        self.contents = []
        self.bags = None
        self.parse_bag_instruction(bag_instruction)
    
    def parse_bag_instruction(self, bag_instruction):
        # 'light red bags contain 1 bright white bag, 2 muted yellow bags.'
        instruction = bag_instruction.split('contain')
        self.color = instruction[0].strip()

        contents = instruction[1].strip().split(',')
        # print(contents)
        if contents == '':
            return
        elif contents[0] == 'no other bags.':
            return
        for item in contents:
            # self.contents.append(item)
            item = item.strip().strip('.')
            item_qty = int(item[:item.find(' ')])
            item_description = item[item.find(' ')+1:]
            if item_qty == 1:
                item_description = item_description + 's'
            for i in range(item_qty):
                self.contents.append(item_description)
    
    def get_bags(self, bag_instructions):
        if self.bags is not None:
            return self.bags
        else:
            # bags = [self.color]
            bags = []
            for bag in self.contents:
                # I'm trying to memoize here... but did I already do it?
                # if bag_instructions[bag]['contents'] is None:
                #     #Do something
                #     bag = Bag(bag_instructions[bag]['class'].instructions)
                #     bag_instructions[bag]['contents'] += bag.get_bags(bag_instructions)
                # bags = bag_instructions[bag]['contents']
                bag = Bag(bag_instructions[bag]['class'].instructions)
                bags.append(bag.color)
                if bag_instructions[bag.color]['contents'] is  not None:
                    bags += bag_instructions[bag.color]['contents']
                else:
                    # bag = Bag(bag_instructions[bag]['class'].instructions)
                    # bags.append(bag.color)
                    # bags += bag.get_bags(bag_instructions)
                    bag_instructions[bag.color]['contents'] = bag.get_bags(bag_instructions)
                    bags += bag_instructions[bag.color]['contents']
            self.bags = bags
            return self.bags

    def __str__(self):
        return f'{self.color} contains {self.contents}'





if __name__=='__main__':

    # data = []
    # with open('Day07TEST.txt') as f:
    #     data = f.readlines()
    #     data = [a.strip().split('contain') for a in data]
    #     data = [[b.strip() for b in a] for a in data]
    
    # data_dict = []
    # with open('/home/pi/Programming/AdventOfCode/2020/Day07/Day07TEST.txt') as f:
    #     data_dict = f.readlines()
    #     data_dict = [a.strip() for a in data_dict]
    #     data_dict = [Bag(a) for a in data_dict]
    
    # print(data_dict)
    # [print(a) for a in data_dict]
    # [print(a.get_bags(data_dict)) for a in data_dict]
    
    data = []
    with open('/home/pi/Programming/AdventOfCode/2020/Day07/Day07.txt') as f:
        data = f.readlines()
        data = [a.strip() for a in data]
        data = [Bag(a) for a in data]
    
    # print(data)
    # [print(a) for a in data]
    
    data_dict = {a.color:{'class': a, 'contents':None} for a in data}
    # print(data_dict)
    # print(data[0].get_bags(data_dict))
    count = 0
    for bag in data:
        bags = bag.get_bags(data_dict)
        if 'shiny gold bags' in bags:
            print(bag.color, bag.bags)
            count +=1
    print(count)