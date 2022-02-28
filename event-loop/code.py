from datetime import datetime, timedelta                                      
from time import sleep                                                        
                                                                              
                                                                              
class Delay:                                                                  
    def __init__(self, secs):                                                 
        self._secs = secs                                                     
        self.when = datetime.now() + timedelta(seconds=secs)                  
                                                                              
    def __await__(self):                                                      
        while self.when >= datetime.now():                                    
            yield self._secs                                                  
        return True                                                           
                                                                              
                                                                              
async def coro(sound ,delay):                                                 
    d = Delay(delay)                                                          
    res = await d                                                             
    if res is True:                                                           
        return sound                                                          
                                                                              
                                                                              
def main():                                                                   
    tasks = {"-=* BOOM *=-": 2, "~=* shaka *=~": 1}                           
    in_action = None                                                          
                                                                              
    while True:                                                               
        if not in_action:                                                     
            in_action = [coro(sound, delay) for sound, delay in tasks.items()]
                                                                              
        while in_action:                                                      
            task = in_action.pop(0)                                           
                                                                              
            try:                                                              
                dl = task.send(None)                                          
            except StopIteration as e:                                        
                print(e.value)                                                
                in_action.append(coro(e.value, tasks[e.value]))               
                continue                                                      
                                                                              
            in_action.append(task)                                            
                                                                              
                                                                              
if __name__ == "__main__":                                                    
    print(main())  