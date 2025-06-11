import random

class Grades:
    
    DE = ['sehr gut', 'gut', 'befriedigend', 'ausreichend', 'mangelhaft', 'ungenügend']
    
    def trns_to_no(self, grade:str):
        if grade not in self.DE:
            raise ValueError(f'Grade {grade} is not valid!')
        return self.DE.index(grade) +1 
     
    def trns_to_txt(self, no:str):
        if no not in range(1, 7):
            raise ValueError(f'Grade no {no} is not valid!')
        return self.DE[no-1]  
        
foo = Grades()

print(foo.trns_to_no(grade='befriedigend'))

print(foo.trns_to_txt(4))





# #print(foo.trns_to_no(grade='foo'))
# lst = []
# for i in range(23):
#     lst.append(foo.DE[random.randint(0,5)])
    
# print (lst)