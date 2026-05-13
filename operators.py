
"""

Operator.43

1. Arithmetic Operators(9)
2. Comparison Operators(6)
3. Logical Operators (3)

##########################################

1. Arithmetic Operators(9)  (e u */ +-)

1. exponent        **
2. negative        -
3. positive        +
4. multiplication  *
5. true division   /       2.5
6. floor division  //      2
7. modulus         %       1
8. addition        +
9. substraction    -

Exercises
1. age = 2026 - Birth year , "You are 26 years old."
2. kyats to dollar, "10000 kyats is equal to 2 dollars."
3. 350 seconds is equal to 5 minutes and 50 seconds.
4. 90350 seconds is equal to 1 days 1 hours 5 minutes and 50 seconds.

##########################################

2. Comparison Operators(6) (True, False)

1. equal                   ==
2. not equal               !=
3. greater than            >
4. less than               <
5. greater than or equal   >=
6. less than or equal      <=

Exercises
1. If mark is greater than or equal to 40, exam pass.
2. If mark is less than 40, exam fail.
3. If mark is greater than or equal to 40, exam pass.
   Else, exam fail.
4. one from one (if)
5. one from two (if + else)

##########################################

3. Logical Operators (3) (logical value, boolean value) (True, False)

1. not   =>  opposite
2. and   =>  all
3. or    =>  any

1. If mark is greater than 40 or mark is equal to 40, exam pass.                          or
2. If username is equal to "Mg Mg" and password is equal to "12345", login successful.    and
3. if full water, Motor Stop.
4. if not full water, Motor ON.

##########################################

1. print
2. input
3. TypeCasting
4. String concatination
5. string formatting
6. Selection
   - if True
   - else False
   - one from two => if + else

##########################################

Exercises of Arithmetic Operators

1. age = 2026 - Birth year , "You are 26 years old."
2. kyats to dollar, "10000 kyats is equal to 2 dollars."
3. 350 seconds is equal to 5 minutes and 50 seconds.
4. 90350 seconds is equal to 1 days 1 hours 5 minutes and 50 seconds.

##########################################

1. age = 2026 - Birth year , "You are 26 years old."

x = input("Birth year = ")
age = 2026 - int(x)
ans = "You are " + str(age) + " years old."
print(ans)

##########################################

2. kyats to dollar, "10000 kyats is equal to 2 dollars."


kyat = int(input("Kyats = "))
dollar = kyat / 5000
ans = str(kyat) + " kyats is equal to " + str(dollar) + " dollars."

print(ans)

##########################################

3. 350 seconds is equal to 5 minutes and 50 seconds.

total_seconds = int(input("Total seconds = "))
minutes = total_seconds // 60
seconds = total_seconds % 60

ans = f"{total_seconds} seconds is equal to {minutes} minutes and {seconds} seconds."

print(ans)

##########################################

4. 90350 seconds is equal to 1 days 1 hours 5 minutes and 50 seconds.

                   90350  seconds

                 1505 min  +   50 sec

               25 hour + 5 min

             1 day + 1 hour

total_seconds = int(input("Total seconds = "))
total_minutes = total_seconds // 60     # 1505
seconds = total_seconds % 60            # 50

total_hour = total_minutes // 60        # 25
minutes = total_minutes % 60            # 5

day = total_hour // 24                  # 1
hour = total_hour % 24                  # 1

ans = f"{total_seconds} seconds is equal to {day} days {hour} hours {minutes} minutes and {seconds} seconds."

print(ans)

####################################################################################

Exercises of Comparison Operators

1. If mark is greater than or equal to 40, exam pass.
2. If mark is less than 40, exam fail.
3. If mark is greater than or equal to 40, exam pass.
Else, exam fail.
4. one from one (if)
5. one from two (if + else)

##########################################

1. If mark is greater than or equal to 40, exam pass.

if mark >= 40: print("exam pass")

##########################################

2. If mark is less than 40, exam fail.

if mark < 40: print("exam fail")

##########################################

3. If mark is greater than or equal to 40, exam pass.
Else, exam fail.

if mark >= 40: print("exam pass")
else: print("exam fails")

##########################################

4. one from one

mark = int(input("Mark = "))
if mark >= 40: print("exam pass")
if mark < 40: print("exam fail")

##########################################

5. one from two

mark = int(input("Mark = "))
if mark >= 40: print("exam pass")
else: print("exam fails")

####################################################################################

Exercises of Logical Operators

1. If mark is greater than 40 or mark is equal to 40, exam pass.                          or
2. If username is equal to "Mg Mg" and password is equal to "12345", login successful.    and
3. if full water, Motor Stop.
4. if not full water, Motor ON.                                                           not

####################################################################################

1. If mark is greater than 40 or mark is equal to 40, exam pass.

if mark > 40 or mark == 40: print("exam pass")

##########################################

2. If username is equal to "Mg Mg" and password is equal to "12345", login successful.

if username == "Mg Mg" and password == "12345": print("login successful.")

##########################################

3. if full water, Motor Stop.

if sensor: print("Motor Stop.")

##########################################

4. If not full water, Motor ON.

if not sensor: print("Motor On.")

####################################################################################

"""
