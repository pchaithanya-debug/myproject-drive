class Pattern_programming:
    def single_star(self):      
        print("+-----------+")
        print("|Single star|")
        print("+-----------+")  
        print("*")
        print("\n\n")
    def horizontal_stars(self):
        print("+----------------+")
        print("|horizontal stars|")
        print("+----------------+")  
        n=int(input("enter number of stars do you want to print:"))
        for i in range(n):
            print("*",end=" ")
        print("\n\n")
    def vertical_stars(self):
        print("+--------------+")
        print("|vertical stars|")
        print("+--------------+")  
        n=int(input("enter number of stars do you want to print:"))
        for i in range(n):
            print("*")
        print("\n\n")
    def solid_square(self):
        print("+------------+")
        print("|Solid Square|")
        print("+------------+")  
        n=int(input("enter size of the square:"))
        for i in range(n):
            for j in range(n):
                print("*",end=" ")
            print()
        print("\n\n")
    def hollow_square(self):
        print("+-------------+")
        print("|Hollow Square|")
        print("+-------------+")  
        n=int(input("enter size of the square:"))
        for i in range(n):
            for j in range(n):
                if i==0 or i==n-1 or j==0 or j==n-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
        print("\n\n")
    def solid_rectangle(self):
        print("+---------------+")
        print("|Solid Rectangle|")
        print("+---------------+") 
        len=int(input("Enter the length of rectangle:"))
        bre=int(input("Enter the breadth of rectangle:"))
        for i in range(bre):
            for j in range(len):
                print("*",end=" ")
            print()
        print("\n\n")
    def hollow_rectangle(self):
        print("+----------------+")
        print("|Hollow Rectangle|")
        print("+----------------+") 
        len=int(input("Enter the length of rectangle:"))
        bre=int(input("Enter the breadth of rectangle:"))
        for i in range(bre):
            for j in range(len):
                if i==0 or i==bre-1 or j==0 or j==len-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
        print("\n\n")
    def solid_parallelogram(self):
        print("+-------------------+")
        print("|Solid Parallelogram|")
        print("+-------------------+") 
        len=int(input("Enter the length of parallelogram:"))
        bre=int(input("Enter the breadth of parallelogram:"))
        for i in range(bre):
            for k in range(bre-1-i):
                print(" ",end=" ")
            for j in range(len):
                    print("*",end=" ")
            print()
        print("\n\n")
    def hollow_parallelogram(self):
        print("+--------------------+")
        print("|Hollow Parallelogram|")
        print("+--------------------+") 
        len=int(input("Enter the length of parallelogram:"))
        bre=int(input("Enter the breadth of parallelogram:"))
        for i in range(bre):
            for k in range(bre-1-i):
                print(" ",end=" ")
            for j in range(len):
                if i==0 or i==bre-1 or j==0 or j==len-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
        print("\n\n")
    def solid_right_angle_triangle_1(self):
        print("+----------------------------+")
        print("|Solid right angle triangle 1|")
        print("+----------------------------+") 
        n=int(input("Enter rowsize:"))
        for i in range(n):
            for k in range(i+1):
                print("*",end=" ")
            print()
        print("\n\n")
    def hollow_right_angle_triangle_1(self):
        print("+-----------------------------+")
        print("|Hollow right angle triangle 1|")
        print("+-----------------------------+") 
        n=int(input("Enter rowsize:"))
        for i in range(n):
            for k in range(i+1):
                if i==n-1 or k==0 or i==k:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
        print("\n\n")
    def solid_right_angle_triangle_2(self):
        print("+----------------------------+")
        print("|Solid right angle triangle 2|")
        print("+----------------------------+") 
        n=int(input("Enter row size: "))
        for i in range(n):
            for k in range(n-i):
                print("*",end=" ")
            print()
        print("\n\n")
    def hollow_right_angle_triangle_2(self):
        print("+-----------------------------+")
        print("|Hollow right angle triangle 2|")
        print("+-----------------------------+") 
        n=int(input("Enter row size: "))
        for i in range(n):
            for k in range(n-i):
                if k==n-1-i or i==0 or k==0:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
        print("\n\n")
    def solid_right_angle_triangle_3(self):
        print("+----------------------------+")
        print("|Solid right angle triangle 3|")
        print("+----------------------------+") 
        n=int(input("Enter row size: "))
        for i in range(n):
            for k in range(n-i-1):
                print(" ",end=" ")
            for j in range(n-1-i,n):
                print("*",end=" ")
            print()
        print("\n\n")
    def hollow_right_angle_triangle_3(self):
        print("+-----------------------------+")
        print("|Hollow right angle triangle 3|")
        print("+-----------------------------+") 
        n=int(input("Enter row size: "))
        for i in range(n):
            for k in range(n-i-1):
                print(" ",end=" ")
            for j in range(n-1-i,n):
                if j==n-1-i or j==n-1 or i==n-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
        print("\n\n")
    def solid_right_angle_triangle_4(self):
        print("+----------------------------+")
        print("|Solid right angle triangle 4|")
        print("+----------------------------+") 
        n=int(input("Enter row size: "))
        for i in range(n):
            for k in range(i):
                print(" ",end=" ")
            for j in range(i,n):
                print("*",end=" ")
            print()
        print("\n\n")
    def hollow_right_angle_triangle_4(self):
        print("+-----------------------------+")
        print("|Hollow right angle triangle 4|")
        print("+-----------------------------+") 
        n=int(input("Enter row size: "))
        for i in range(n):
            for k in range(i):
                print(" ",end=" ")
            for j in range(i,n):
                if i==j or i==0 or j==n-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
        print("\n\n")
    def solid_isosceles_triangle_1(self):
        print("+--------------------------+")
        print("|Solid Isosceles Triangle 1|")
        print("+--------------------------+") 
        n=int(input("Enter the rowsize: "))
        for i in range(n):
            for k in range(n-1-i):
                print(" ",end=" ")
            for j in range(n-1-i,n+i):
                print("*",end=" ")
            print()
        print("\n\n")
    def hollow_isosceles_triangle_1(self):
        print("+---------------------------+")
        print("|Hollow Isosceles Triangle 1|")
        print("+---------------------------+") 
        n=int(input("Enter the rowsize: "))
        for i in range(n):
            for k in range(n-1-i):
                print(" ",end=" ")
            for j in range(n-1-i,n+i):
                if j==n-1-i or j==n-1+i or i==n-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
        print("\n\n")
    def solid_isosceles_triangle_2(self):
        print("+--------------------------+")
        print("|Solid Isosceles Triangle 2|")
        print("+--------------------------+") 
        n=int(input("Enter the rowsize: "))
        for i in range(n):
            for k in range(i):
                print(" ",end=" ")
            for j in range(i,(n-1)*2-i+1):
                print("*",end=" ")
            print()
        print("\n\n")
    def hollow_isosceles_triangle_2(self):
        print("+---------------------------+")
        print("|Hollow Isosceles Triangle 2|")
        print("+---------------------------+") 
        n=int(input("Enter the rowsize: "))
        for i in range(n):
            for k in range(i):
                print(" ",end=" ")
            for j in range(i,(n-1)*2-i+1):
                if j==(n-1)*2-i or i==j or i==0:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
        print("\n\n")
    def solid_isosceles_triangle_3(self):
        print("+--------------------------+")
        print("|Solid Isosceles Triangle 3|")
        print("+--------------------------+") 
        n=int(input("Enter the rowsize:"))
        for i in range(n):
            for j in range(i+1):
                print("*",end=" ")
            print()
        for i in range(n-1):
            for j in range(n-i-1):
                print("*",end=" ")
            print()
        print("\n\n")
    def hollow_isosceles_triangle_3(self):
        print("+---------------------------+")
        print("|Hollow Isosceles Triangle 3|")
        print("+---------------------------+") 
        n=int(input("Enter the rowsize:"))
        for i in range(n):
            for j in range(i+1):
                if i==j or j==0:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
        for i in range(n-1):
            for j in range(n-i-1):
                if j==0 or j==n-2-i:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
        print("\n\n")
    def solid_isosceles_triangle_4(self):
        print("+--------------------------+")
        print("|Solid Isosceles Triangle 4|")
        print("+--------------------------+") 
        n=int(input("Enter rowsize: "))
        for i in range(n):
            for k in range(n-1-i):
                print(" ",end=" ")
            for j in range(n-1-i,n):
                print("*",end=" ")
            print()
        for i in range(n-1):
            for k in range(i+1):
                print(" ",end=" ")
            for j in range(i+1,n):
                print("*",end=" ")
            print()
        print("\n\n")
    def hollow_isosceles_triangle_4(self):
        print("+---------------------------+")
        print("|Hollow Isosceles Triangle 4|")
        print("+---------------------------+") 
        n=int(input("Enter rowsize: "))
        for i in range(n):
            for k in range(n-1-i):
                print(" ",end=" ")
            for j in range(n-1-i,n):
                if j==n-1 or j==n-1-i:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
        for i in range(n-1):
            for k in range(i+1):
                print(" ",end=" ")
            for j in range(i+1,n):
                if j==n-1 or j==i+1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
        print("\n\n")
    def solid_rhombus(self):
        print("+-------------+")
        print("|Solid Rhombus|")
        print("+-------------+") 
        n=int(input("Enter the rowsize: "))
        for i in range(n):
            for k in range(n-1-i):
                print(" ",end=" ")
            for j in range(n-1-i,n+i):
                print("*",end=" ")
            print()
        for i in range(n-1):
            for k in range(i+1):
                print(" ",end=" ")
            for j in range(i+1,(n-1)*2-i):
                print("*",end=" ")
            print()
        print("\n\n")
    def hollow_rhombus(self):
        print("+--------------+")
        print("|Hollow Rhombus|")
        print("+--------------+") 
        n=int(input("Enter the rowsize: "))
        for i in range(n):
            for k in range(n-1-i):
                print(" ",end=" ")
            for j in range(n-1-i,n+i):
                if j==n-1-i or j==n-1+i:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
        for i in range(n-1):
            for k in range(i+1):
                print(" ",end=" ")
            for j in range(i+1,(n-1)*2-i):
                if j==i+1 or j==(n-1)*2-i-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
        print("\n\n")
    def solid_hour_glass(self):
        print("+----------------+")
        print("|Solid Hour Glass|")
        print("+----------------+") 
        n=int(input("Enter the rowsize: "))
        for i in range(n):
            for j in range(i):
                print(" ",end=" ")
            for k in range(i,(n-1)*2-i+1):
                print("*",end=" ")
            print()
        for i in range(n):
            for k in range(n-1-i):
                print(" ",end=" ")
            for j in range(n-1-i,n+i):
                print("*",end=" ")
            print()
        print("\n\n")
    def hollow_hour_glass(self):
        print("+-----------------+")
        print("|Hollow Hour Glass|")
        print("+-----------------+") 
        n=int(input("Enter the rowsize: "))
        for i in range(n):
            for j in range(i):
                print(" ",end=" ")
            for k in range(i,(n-1)*2-i+1):
                if i==0 or k==i or k==((n-1)*2-i):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
        for i in range(n):
            for k in range(n-1-i):
                print(" ",end=" ")
            for j in range(n-1-i,n+i):
                if i==n-1 or j==n-1-i or j==n-1+i:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
        print("\n\n")

    def menu_card(self):
        print("\t+---------------------------------+")
        print("\t|           MENU CARD             |")               
        print("\t+---------------------------------+")
        print("\t|1.single star                    |")
        print("\t|2.horizontal stars               |")
        print("\t|3.vertical stars                 |")
        print("\t|4.solid square                   |")
        print("\t|5.hollow square                  |")
        print("\t|6.solid rectangle                |")
        print("\t|7.hollow rectangle               |")
        print("\t|8.solid parallelogram            |")
        print("\t|9.hollow parallelogram           |")
        print("\t|10.solid right angle triangle 1. |")
        print("\t|11.hollow right angle triangle 1.|")
        print("\t|12.solid right angle triangle 2. |")
        print("\t|13.hollow right angle triangle 2.|")
        print("\t|14.solid right angle triangle 3. |")
        print("\t|15.hollow right angle triangle 3.|")
        print("\t|16.solid right angle triangle 4. |")
        print("\t|17.hollow right angle triangle 4.|")
        print("\t|18.Solid Isosceles triangle 1.   |")
        print("\t|19.Hollow Isosceles triangle 1.  |")
        print("\t|20.Solid Isosceles triangle 2.   |")
        print("\t|21.Hollow Isosceles triangle 2.  |")
        print("\t|22.solid Isosceles triangle 3.   |")
        print("\t|23.Hollow Isosceles triangle 3.  |")
        print("\t|24.solid Isosceles triangle 4.   |")
        print("\t|25.Hollow Isosceles triangle 4.  |")
        print("\t|26.Solid Rhombus.                |")
        print("\t|27.Hollow Rhombus.               |")
        print("\t|28.Solid Hour Glass.             |")
        print("\t|29.Hollow Hour Glass.            |")
        print("\t|30.Exit                          |")
        print("\t+--------------------------------+")
obj=Pattern_programming()
try: 
    obj.menu_card()
    number_of_patterns=int(input("enter how many patterns do you want to print among all the above 30 options including exit:"))
    if number_of_patterns>30:
        print("Number of patterns you want are more than that of the patterns that are in the menu card.")
    else:
        for i in range(number_of_patterns):
            option=int(input("enter a valid option:"))
            match option:
                case 1:
                    obj.single_star()
                case 2:
                    obj.horizontal_stars()
                case 3:
                    obj.vertical_stars()
                case 4:
                    obj.solid_square()
                case 5:
                    obj.hollow_square()
                case 6:
                    obj.solid_rectangle()
                case 7:
                    obj.hollow_rectangle()
                case 8:
                    obj.solid_parallelogram()
                case 9:
                    obj.hollow_parallelogram()
                case 10:
                    obj.solid_right_angle_triangle_1()
                case 11:
                    obj.hollow_right_angle_triangle_1()
                case 12:
                    obj.solid_right_angle_triangle_2()
                case 13:
                    obj.hollow_right_angle_triangle_2()
                case 14:
                    obj.solid_right_angle_triangle_3()
                case 15:
                    obj.hollow_right_angle_triangle_3()
                case 16:
                    obj.solid_right_angle_triangle_4()
                case 17:
                    obj.hollow_right_angle_triangle_4()
                case 18:
                    obj.solid_isosceles_triangle_1()
                case 19:
                    obj.hollow_isosceles_triangle_1()
                case 20:
                    obj.solid_isosceles_triangle_2()
                case 21:
                    obj.hollow_isosceles_triangle_2()
                case 22:
                    obj.solid_isosceles_triangle_3()
                case 23:
                    obj.hollow_isosceles_triangle_3()
                case 24:
                    obj.solid_isosceles_triangle_4()
                case 25:
                    obj.hollow_isosceles_triangle_4()
                case 26:
                    obj.solid_rhombus()
                case 27:
                    obj.hollow_rhombus()
                case 28:
                    obj.solid_hour_glass()
                case 29:
                    obj.hollow_hour_glass()
                case 30:
                    print("Exited successfully.....")
                    break
                case _:
                    print("enter a valid option between 1 and 30 (inclusive):")          
except ValueError:
    print("Enter number of patterns you want as an integer.")


            
                