class Odd_or_Even:
    def odd_even (self,):
        num = int ( input ( "digite un numero positivo "))
        if num % 2 > 0:
            print ("su numero es impar")
        else: 
            print ("su numero es par")
            if num % 4 == 0: 
                print (" ademas es multiplo de 4")
        num_1= int (input ("digite un numero y despues digite otro numero para comprobar si el primero es un divisible entero entre el segundo"))
        num_2 = int (input ("digite el segundo numero "))
        if num_1 % num_2 == 0:
            print ("es un numero entero divisible")




sol = Odd_or_Even ()
print (sol.odd_even ())
