hrs,mins = list(map(int,input("enter the time(HH:MM):").split(':')))
if 0<= hrs <=23 and 0<= mins <= 59 :
    if 0<= hrs <= 11:
        print(f'{str(hrs).zfill(2)}:
              {str(mins).zfill(2)}AM')
    elif hrs == 12:
             print(f'{str(hrs).zfill(2)}:
              {str(mins).zfill(2)}PM')
    else:
        print(f'{hrs-12}:{mins} PM')
    if 4<=hrs<=11:
        print("good morning,have nice day")
     elif 12<=hrs<=16:
        print("good afternoon,have launch")
     elif 17<=hrs<=19:
        print("good morning,have tea")
    elif 4<=hrs<=11:
        print("good morning,have tea")
     elif 20<=hrs<=23:
        print("good morning,have a good sleep")
    elif 0 <= hrs <= 3:
        print("its mid night.have a sleep")
     else:
         print("Invalid Time")
        
        
        
           
            
