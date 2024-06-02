from typing import Any


class Average():
    def __init__(self) -> None:
        self.data:list[int]= []
        
    def __call__(self, number:int) -> Any:
        self.data.append(number)
        print(self.data)
        return sum(self.data) / len(self.data)
    
    
avj_obj:Average = Average()
average:float= avj_obj(3)
average1:float= avj_obj(4)
average2:float= avj_obj(3)
average3:float= avj_obj(2)

print(f"your average is {average}")