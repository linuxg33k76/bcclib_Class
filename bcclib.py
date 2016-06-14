'''
Ben Calvert's Python Library - bcclib.py
Created June 7, 2016
'''
import math
import string
import re

class Environment(object):

    def __init__(self):
        pass

    def c_to_f(self, temp):
        '''
      This function takes a temperature in Celsius and returns the temp in Fahrenheit
      '''
        fahrenheit = (temp * (9.0 / 5.0) + 32)
        return fahrenheit

    def f_to_c(self, temp):
        '''
      This function takes a temperature in Fahrenheit and returns the temp in Celsius
      '''
        celsius = ((temp - 32) * (5 / 9.0))
        return celsius


class BCC_Math(object):
    # Function to multiply all numbers in a list

    def __init__(self):
        pass

    def multiply(self, numbers):
        '''
        Take in a set of numbers and multiple all together.
        Return the total.
        '''
        total = numbers[0]
        for num in numbers:
            total = total * num
        return total

    def better_prime(self, num):
        '''
        This is a more preferred method of checking for a prime number.
        Input:  an integer
        Output:  message about number being prime or not.
        This function checks to see if the number is divisible by 2 with no remainder, and greater
        than 2; if so, it's NOT prime.  Otherwise, we use the all() to evaluate the number modulus of
        a number range from 3 to the interger of square root of the number plus 1; in steps of 2.
        '''
        if num % 2 == 0 and num > 2:
            statement = (str(num) + ' is Not Prime!')
        elif all(num % i for i in range(3, int(math.sqrt(num)) + 1, 2)) is True:
            statement = (str(num) + ' is Prime!')
        else:
            statement = (str(num) + ' is Not Prime!')
        return statement

    def vol(self, rad):
        '''
        Takes in a radius value and returns a float to four decimal places.
        '''
        return round(((4 / 3.0 * (math.pi)) * rad ** 3), 4)

    def ran_check(self, num, low, high):
        return num in range(low, high)

    def fibonacci(self,start_a,start_b,r):
        '''
        This generator method creates a Fibonacci number sequence based on start values passed to it.
        :param start_a: start value - 1 in classic; 0 in modern
        :param start_b: start value - usually 1
        :param r: range of values
        :return: yield value
        '''
        a,b = start_a,start_b  #tuple unpacking
        for i in range(r):     #Only create r number of results
            yield a
            a,b = b, a+b       #tuple packing


class Misc_Functions(object):

    def __init__(self):
        pass

    def up_low(self, s):
        """
        Take a string input, and counts the number of uppercase and lowercase letters.
        Returns a print statement with Original Message, Uppercase count, and Lowercase count.
        """
        up = 0
        low = 0
        for letter in s:
            if letter.isupper():
                up += 1
            elif letter.islower():
                low += 1
            else:
                pass
        print('The original string was: ' + s)
        print('The number of Upper Case letters: ' + str(up))
        print('The number of Lower Case letters: ' + str(low))

        # Return a unique list of values

    def unique_list(self, list):
        '''
        Return an unique list of values for a given list as an array.
        '''
        return set(list)

    # check to see if a string is a palindrome - use [::-1]

    def palindrome(self, s):
        '''
        Take a string input and evaluate to see if its a palidrome.
        Return a bool True or False.
        '''
        s = s.replace(' ', '')  # Removes spaces in string - think, "nurses run"
        return s == s[::-1]

    # Check to see if a string contains all letters in the alphabet at least once.


    def ispangram(self, str1, alphabet=string.ascii_lowercase):
        '''
        Takes a string input and compares it to see if all the letters of the alphabet are used
        at least once.  Uses the set() function to create a list of unique letters.
        Returns a bool True or False
        '''
        alphaset = set(alphabet)  # Set creates a unique list of values in a string
        return alphaset <= set(str1.lower())

    #Function for finding multiple regular expressions

    def multi_re_find(patterns,phrase):
        '''
        Takes in a list of regex patterns
        Prints a list of all matches
        '''
        for pattern in patterns:
            print 'Searching the phrase using the re check: %r' %pattern
            print re.findall(pattern,phrase)
            print '\n'

class Cylinder(object):

    #Class attributes
    pi = 3.14

    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        #V=Pi*r2h
        r = self.radius
        h = self.height
        return (Cylinder.pi*r**2*h)

    def surface_area(self):
        #A=2Pi*rh+2Pi*r2
        r = self.radius
        h = self.height
        return ((2*Cylinder.pi*r*h) + (2*Cylinder.pi*r**2))

class Line(object):

    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        #Distance between 2 points = square root((x2 -x1)^2 + (y2 -y1)^2)
        x1 = self.coor1[0]
        x2 = self.coor2[0]
        y1 = self.coor1[1]
        y2 = self.coor2[1]
        return ((y2 -y1)**2 + (x2 - x1)**2)**0.5

    def slope(self):
        #Slope:  m = (y2 - y1)/(x2 - x1)
        x1 = self.coor1[0]
        x2 = self.coor2[0]
        y1 = self.coor1[1]
        y2 = self.coor2[1]
        return ((float(y2 - y1)/float(x2 - x1)))  #need to cast as float to get accuracy