import os
import sys

from plugin import plugin
from six.moves import input

from colorama import Fore, Back, Style

@plugin('bmi')

class Bmi():

    def __call__(self, jarvis, s):
            
        syst = ['metric', 'imperial']
        system = self.get_system('Type your system', syst)

        if system == 'metric':
            height, weight = self.ask_measurements(jarvis, "m")
            calc = self.calc_bmi_m(jarvis, height, weight)
        else:
            height, weight = self.ask_measurements(jarvis, "i")
            calc = self.calc_bmi_i(jarvis, height, weight)

        calc = round(calc, 1)
        print("BMI: ", str(calc))
        self.find_body_state(jarvis, calc)
        
    def get_system(self, jarvis, syst):

        prompt = ('Please choose the system you would like to use\n'
                '(1) For metric system\n'
                '(2) For imperial system\n'
                'Your choice: ')
        while True:            
            c = input(prompt)
            if c == '1':
                return 'metric'
            elif c == '2':
                return 'imperial'
            elif c == 'help me':
                prompt = ('If you want to calculate on metric system type 1\n'
                        'If you want to calculate on imperial system type 2: ')
                continue
            elif c == 'try again':
                prompt = 'Please type 1 for metric and 2 for imperial system: '
                continue 
            else:
                prompt = ('Type <help me> to see valid inputs \n'
                        'or <try again> to continue: ')

    def calc_bmi_m(self, jarvis, height, weight):

        #Calculate bmi for metric system
        height = height/100
        bmi = weight/height**2
        return bmi

    def calc_bmi_i(self, jarvis, height, weight):

        #Calculate bmi for imperial system
        bmi = weight/height**2 * 703
        return bmi

    def find_body_state(self, jarvis, calc):

        if calc < 16:
            print('STATE: ' + Back.RED + 'Severe thinness')
        elif calc < 18.5:
            print('STATE: ' + Back.YELLOW + 'Mild thinness')
        elif calc < 25:
            print('STATE: ' + Back.GREEN + 'Healthy')
        elif calc < 30:
            print('STATE: ' + Back.YELLOW + 'Pre-obese')
        else:
            print('STATE: ' + Back.RED + 'Obese')
        print(Style.RESET_ALL)

    def ask_measurements(self, jarvis, s):

        if s == "m":   
            jarvis.say("Please insert your height (cm): ")
            height = input()
            while True:
                try:
                    height = int(height)
                    if height <0:
                        raise ValueError('Please only positive numbers!')
                    break
                except ValueError:
                    print("Error on input type for height, please insert an integer: ")
                    height = input()

            jarvis.say("Please insert your weight (kg): ")
            weight = input()            
            while True:
                try:
                    weight = int(weight)
                    if weight <=0:
                        raise ValueError('Please only positive numbers!')
                    break
                except ValueError:
                    print("Error on input type for weight, please insert an integer: ")
                    weight = input()

        else:
            jarvis.say("Please insert your height (feet): ")
            feet = input()
            jarvis.say("Please insert your height (inches): ")
            inches = input()
            jarvis.say("Please insert your weight (lbs): ")
            weight = input()

            height = int(feet)*12 + int(inches)
            weight = int(weight)
        return height, weight
