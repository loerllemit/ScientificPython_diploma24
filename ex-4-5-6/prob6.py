#%%
class Person():
    def __init__(self,first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def is_adult(self):
        return True if self.age >=18 else False
# %%

ins = Person('Christian','Llemit',26)
print('full name:',ins.full_name())
print('adult?:',ins.is_adult())