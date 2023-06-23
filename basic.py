# # POMODORO

import time
from PIL import Image

import tkinter as tk                    
from tkinter import ttk
import playsound

knowledge_pomodoro = input('Do you know about the POMODORO TECHNIQUE?(Yes/No)--> ')



if knowledge_pomodoro == 'No':
    pomodoro = Image.open('pomodoro.jpg')
    pomodoro.show()
    print('I hope you got a breif idea of how pomodoro works')
    answer = input('')
    print('WELCOME TO THE WORLD OF POMODORO \n')

elif knowledge_pomodoro=='Yes': 
    print('GREAT, WELCOME TO THE WORLD OF POMODORO \n')
else:
    print('WRONG INPUT')
    


def pomodoro_technique(pomodoro_work_time,pomodoro_rest_time):
    while knowledge_pomodoro=='Yes' or answer=='Yes':

        mins, secs = divmod(pomodoro_work_time,60)
        pomodoro_timer = '{:02d}:{:02d}'.format(mins, secs)
        print(pomodoro_timer, end='\r')
        time.sleep(1)
        pomodoro_work_time-=1
        if pomodoro_work_time==0:
            print('BREAK!')
            playsound.playsound('BREAK.mp3')
            while pomodoro_rest_time>0:
                pomodoro_round = 0
                mins, secs = divmod(pomodoro_rest_time,60)
                pomodoro_timer = '{:02d}:{:02d}'.format(mins, secs)
                print(pomodoro_timer, end='\r')
                time.sleep(1)
                pomodoro_rest_time-=1
                pomodoro_round+=1
        if pomodoro_rest_time==0:
            print(f'Congrats!, ROUND {pomodoro_round} COMPLETE.')
            continue_pomodoro = input('Do you want to continue?: ')
            if continue_pomodoro == 'Yes':
                        pomodoro_technique(pomodoro_work_time=1,pomodoro_rest_time=3)
            else:
                print('Thankyou for coming')
                break
            

pomodoro_technique(pomodoro_work_time=1500,pomodoro_rest_time=300)

# lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# lst1 = lst[5:15:2]
# lst2 = lst[::4]
# sum = 0
# for a in lst1:
#     sum = sum + a
# print(sum)
# for b in lst2:
#     sum = sum + b
# print(sum/len(lst2))

   




    


 


    








    
