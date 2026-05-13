
"""
Selection

1. Normal Statement 
   - motor on
   - motor off
   - pass
   - fail

2. Conditional Statement
   - If water level is low, motor on.
   - If water level is high, motor off.
   - if exam pass, show "pass".
   - if exam fail, show "fail".

3. Conditional if Statement
   - boolean data type
   - True

3. Conditional else Statement
   - boolean data type
   - False
   
Conditional if Statement
1. depend on condition
2. True

Conditional else Statement
1. depend on condition
2. False

################################################

1. Conditional if, if
2. Code block
3. Conditional code block
4. Conditional if code block, if code block, if block
5. Conditional else code block, else code block, else block
6. Condition
7. Boolean value
   - empty => False
   - any   => True
8. program flow
9. control flow
10. : (code block)
11. pass (keyword name for pass)

################################################

7. Boolean value
   - empty => False
   - any   => True

fruits = ["apple", "banana", "orange"]

if fruits:
    print("You can buy fruits.")

else:
    print("You can not buy fruits.")
    
################################################

8. program flow

1. input
2. assign
3. input
4. assign
5. if
6. eq l
7. eq r
8. and
9. print

username = input("username = ")
password = input("password = ")
if username == "Mg Mg" and password == "12345": print("login successful.")

################################################

Nested if

Step.1 (condition => output?) (flow)

- 1 1 1     =>  a c
- 0 0 0     =>  b f
- 1 0 1     =>  a d e
- 1 0 0     =>  a d f

001   be
010   bf
110   ac

################################################

c1 = 1
c2 = 1
c3 = 1

if c1:
    print("a")
    if c2:
        print("c")
    else:
        print("d")
        if c3:
            print("e")
        else:
            print("f")
else:
    print("b")
    if c3:
        print("e")
    else:
        print("f")

################################################

Step.2 (output => condition ?) (control)

KHK => 101

c1 = 1
c2 = 0
c3 = 1

if c1:
    print("a")
    if c2:
        print("c")
    else:
        print("d")
        if c3:
            print("e")
            print("KHK")
        else:
            print("f")
else:
    print("b")
    if c3:
        print("e")
    else:
        print("f")

################################################

Step.3 (condition => new code) 

- 101    =>  print("new")
- 100    =>  print("new2")
- 0-1    =>  print("new3")
- 0-0    =>  print("new4")
- 111    =>  print("new5")
- 110    =>  print("new6")
-
- 011    => print("new7")
- 00-    => print("new8")
- 010    => print("new9")

if c3:print("new5")


if c2:
    if c3:
        print("new7")
        
################################################

c1 = 0
c2 = 1
c3 = 0

if c1:
    print("a")
    if c2:
        print("c")
        if c3:
            print("new5")
        else:
            print("new6")
    else:
        print("d")
        if c3:
            print("e")
            print("new")
        else:
            print("f")
            print("new2")
else:
    print("b")
    if c2:
        if c3:
            print("new7")
        else:
            print("new9")
    else:
        print("new8")
    if c3:
        print("e")
        print("new3")
    else:
        print("f")
        print("new4")
 
################################################
 
Step.4 (idea =>  code) 

################################################

1. low level

if low_level:
    print("motor on.")
   
################################################

2. electric, not electric 

1 1
low_level + electric    -> print("motor on.")

1 0
low_level + not electric    -> print("generator on."); print("motor on.")


if low_level:
    if electric:
        print("motor on.")
    else:
        print("generator on.")
        print("motor on.")
        
################################################

3. Short circuit

1 1 0
low_level + electric + not short circuit       => print("motor on.")

1 0 0
low_level + not electric + not short circuit   =>  print("motor on.")


1 1 1
low_level + electric + short circuit           =>   print("call mechanic")

1 0 1
low_level + not electric + short circuit       =>   print("call mechanic")


1 0     =>  print("generator on.")

1 0 1   =>  print("generator off.")

################################################ 

low_level = 1
electric = 0
short_circuit = 1

if low_level:
    if electric:
        if short_circuit:
            print("call mechanic")
        else:
            print("motor on.")
    else:
        print("generator on.")
        if short_circuit:
            print("call mechanic")
            print("generator off.")
        else:
            print("motor on.")


################################################

4. Motor 2

1 1 1
low_level + electric + short circuit           =>   print("call mechanic");print("M2 on.")

1 0 1
low_level + not electric + short circuit       =>   print("call mechanic");print("M2 on.")

################################################

low_level = 1
electric = 1
short_circuit = 1

if low_level:
    if electric:
        if short_circuit:
            print("call mechanic")
            print("M2 on.")
        else:
            print("motor on.")
    else:
        print("generator on.")
        if short_circuit:
            print("call mechanic")
            print("M2 on.")
        else:
            print("motor on.")
  
################################################

5. not short_circuit2 + short_circuit2

################################################

not short_circuit2

1 1 1 0
low_level + electric + short circuit + not short circuit       =>   print("M2 on.")

1 0 1 0
low_level + not electric + short circuit + not short circuit   =>   print("M2 on.")

low_level = 1
electric = 1
short_circuit = 1
short_circuit2 = 0

if low_level:
    if electric:
        if short_circuit:
            print("call mechanic")
            if short_circuit2:
                pass
            else:
                print("M2 on.")
                
        else:
            print("motor on.")
    else:
        print("generator on.")
        if short_circuit:
            print("call mechanic")
            if short_circuit2:
                pass
            else:
                print("M2 on.")
        else:
            print("motor on.")


################################################

short_circuit2

1 1 1 1
low_level + electric + short circuit + short circuit       =>   print("call mechanic for m2")

1 0 1 1
low_level + not electric + short circuit + short circuit   =>   print("call mechanic for m2")


1 0      =>  print("generator on.")

1 0 1 1  =>  print("generator off.")

################################################

low_level = 1
electric = 0
short_circuit = 1
short_circuit2 = 1

if low_level:
    if electric:
        if short_circuit:
            print("call mechanic for m1")
            if short_circuit2:
                print("call mechanic for m2")
            else:
                print("M2 on.")

        else:
            print("motor on.")
    else:
        print("generator on.")
        if short_circuit:
            print("call mechanic for m1")
            if short_circuit2:
                print("call mechanic for m2")
                print("generator off.")
            else:
                print("M2 on.")
        else:
            print("motor on.")

################################################

6. m3

1111     print("M3 on.")
1011     print("M3 on.")


low_level = 1
electric = 0
short_circuit = 1
short_circuit2 = 1

if low_level:
    if electric:
        if short_circuit:
            print("call mechanic for m1")
            if short_circuit2:
                print("call mechanic for m2")
                print("M3 on.")
            else:
                print("M2 on.")

        else:
            print("motor on.")
    else:
        print("generator on.")
        if short_circuit:
            print("call mechanic for m1")
            if short_circuit2:
                print("call mechanic for m2")
                print("M3 on.")
            else:
                print("M2 on.")
        else:
            print("motor on.")
            
################################################

7. short circuit3

low_level = 1
electric = 0
short_circuit = 1
short_circuit2 = 1
short_circuit3 = 1

if low_level:
    if electric:
        if short_circuit:
            print("call mechanic for m1")
            if short_circuit2:
                print("call mechanic for m2")
                if short_circuit3:
                    print("call mechanic for m3")
                else:
                    print("M3 on.")
            else:
                print("M2 on.")

        else:
            print("motor on.")
    else:
        print("generator on.")
        if short_circuit:
            print("call mechanic for m1")
            if short_circuit2:
                print("call mechanic for m2")
                if short_circuit3:
                    print("call mechanic for m3")
                    print("generator off.")
                else:
                    print("M3 on.")
            else:
                print("M2 on.")
        else:
            print("motor on.")

################################################

8. M4

11111  => m4
10111  => m4


if low_level:
    if electric:
        if short_circuit:
            print("call mechanic for m1")
            if short_circuit2:
                print("call mechanic for m2")
                if short_circuit3:
                    print("call mechanic for m3")
                    print("M4 on.")
                else:
                    print("M3 on.")
            else:
                print("M2 on.")

        else:
            print("motor on.")
    else:
        print("generator on.")
        if short_circuit:
            print("call mechanic for m1")
            if short_circuit2:
                print("call mechanic for m2")
                if short_circuit3:
                    print("call mechanic for m3")
                    print("M4 on.")
                else:
                    print("M3 on.")
            else:
                print("M2 on.")
        else:
            print("motor on.")

################################################

9. short_circuit4 

################################################

low_level = 1
electric = 0
short_circuit = 1
short_circuit2 = 1
short_circuit3 = 0
short_circuit4 = 0

if low_level:
    if electric:
        if short_circuit:
            print("call mechanic for m1")
            if short_circuit2:
                print("call mechanic for m2")
                if short_circuit3:
                    print("call mechanic for m3")
                    if short_circuit4:
                        print("call mechanic for m4")
                    else:
                        print("M4 on.")
                else:
                    print("M3 on.")
            else:
                print("M2 on.")

        else:
            print("motor on.")
    else:
        print("generator on.")
        if short_circuit:
            print("call mechanic for m1")
            if short_circuit2:
                print("call mechanic for m2")
                if short_circuit3:
                    print("call mechanic for m3")
                    if short_circuit4:
                        print("call mechanic for m4")
                        print("generator on.")
                    else:
                        print("M4 on.")
                else:
                    print("M3 on.")
            else:
                print("M2 on.")
        else:
            print("motor on.")

################################################################################################

"""
