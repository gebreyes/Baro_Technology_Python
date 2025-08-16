
Q1 = """What is the powerhouse of the cell?
a. Nucleus
b. Mitochondria
c. Ribosome
d. Chloroplast 
"""

Q2 = """Which gas do plants absorb during photosynthesis?
a. Oxygen
b. Carbon dioxide
c. Nitrogen
d. Hydrogen
"""

Q3 = """Which part of the plant helps in absorbing water and minerals?
a. Leaves
b. Stem
c. Roots
d. Flowers
"""

Q4 = """What is the largest organ in the human body?
a. Heart
b. Liver
c. Skin
d. Brain
"""

Q5 = """Which blood type is known as the universal donor?
a. A
b. B
c. AB
d. O
"""


Q6 = """What is the chemical symbol for gold?
a. Ag
b. Au
c. Gd
d. Go
"""

Q7 = """Which gas is most abundant in Earth's atmosphere?
a. Oxygen
b. Carbon dioxide
c. Nitrogen
d. Hydrogen
"""

Q8 = """What is the pH value of pure water?
a. 5
b. 7
c. 10
d. 0
"""

Q9 = """Which of these is NOT a noble gas?
a. Helium
b. Neon
c. Argon
d. Chlorine
"""

Q10 = """What is the main component of vinegar?
a. Citric acid
b. Acetic acid
c. Sulfuric acid
d. Hydrochloric acid
"""


Q11 = """What is the SI unit of force?
a. Joule
b. Watt
c. Newton
d. Pascal
"""

Q12 = """Which law states that "every action has an equal and opposite reaction"?
a. Newton’s First Law
b. Newton’s Second Law
c. Newton’s Third Law
d. Ohm’s Law 
"""

Q13 = """What type of energy is stored in a stretched rubber band?
a. Kinetic energy
b. Potential energy
c. Thermal energy
d. Electrical energy
"""

Q14 = """Which color of light has the longest wavelength?
a. Violet
b. Green
c. Red
d. Blue
"""

Q15 = """What is the speed of light in a vacuum?
a. 300,000 km/s
b. 150,000 km/s
c. 500,000 km/s
d. 1,000,000 km/s
"""


Q16 = """What is the value of π (pi) approximately?
a. 2.14
b. 3.14
c. 4.14
d. 1.14
"""

Q17 = """If a triangle has angles 90°, 45°, and 45°, what type of triangle is it?
a. Equilateral
b. Isosceles
c. Scalene
d. Obtuse"""

Q18 = """What is 25% of 200?
a. 25
b. 50
c. 75
d. 100
"""

Q19 = """Solve: 8 × (7 – 3) + 10
a. 42
b. 50
c. 32
d. 60
"""

Q20 = """If x + 5 = 12, what is the value of x?
a. 5
b. 7
c. 12
d. 17 
"""


Q21 = """Choose the correct synonym for "happy":
a. Sad
b. Joyful
c. Angry
d. Tired
"""

Q22 = """Which word is a noun in this sentence: "The cat jumped over the fence."
a. Jumped
b. Over
c. Cat
d. The
"""

Q23 = """What is the past tense of "run"?
a. Ran
b. Runned
c. Running
d. Runs
"""

Q24 = """Identify the correct spelling:
a. Recieve
b. Receive
c. Receeve
d. Reseive
"""

Q25 = """What is the opposite of "begin"?
a. Start
b. End
c. Continue
d. Pause
"""


Q26 = """If all cats are dogs and some dogs are birds, which statement is true?
a. All cats are birds
b. Some cats are birds
c. No cats are birds
d. Cannot be determined
"""

Q27 = """Find the next number: 2, 4, 8, 16, ___
a. 20
b. 24
c. 32
d. 64
"""

Q28 = """If "PEN" is written as "OXM", how is "BOOK" written?
a. ANNI
b. ANLI
c. ANLJ
d. ANLJ
"""

Q29 = """A man walks 5 km south, then 3 km east. How far is he from his starting point?
a. 4 km
b. 5 km
c. 6 km
d. 8 km
"""

Q30 = """If 5 workers complete a task in 10 days, how many days will 10 workers take?
a. 2
b. 5
c. 10
d. 20
"""


questions = {
    Q1:'b',Q2:'b',Q3:'c',Q4:'c',Q5:'d',
    Q6:'b',Q7:'c',Q8:'b',Q9:'d',Q10:'b',
    Q11:'c',Q12:'c',Q13:'b',Q14:'c',Q15:'a',
    Q16:'b',Q17:'b',Q18:'b',Q19:'a',Q20:'b',
    Q21:'b',Q22:'c',Q23:'a',Q24:'b',Q25:'b',
    Q26:'b',Q27:'c',Q28:'a',Q29:'b',Q30:'b'
}

print("Welcome to General Quiz")
name = input("Enter your full name: ")
print(f"Dear {name}, Welcome to Exam Hall")
print("Please ready carefully the following instructions")
print("Instr. 1: Don't forgot to write your full name")
print("Instr. 2: Cheating will nullify your total result")

mark = 0
list = ['a', 'b', 'c', 'd']
for item in questions:
    print(item)
    answer = input("Choose the correct answer a/b/c/d: ").lower()
   
    if answer==questions[item]:
        print(f" {answer} is correct answer, you got 2 pts.")
        mark = mark+2
    else:
        print(f"{answer} is incorrect, {questions[item]} is the correct answer")
        mark = mark
    



if mark >= 55:
    print(f"{mark}/60, Excellent")
elif mark >=50:
    print(f"{mark}/60, V.good!")
elif mark >=40:
    print(f"{mark}/60, Gooooood")
elif mark >=50:
    print(f"{mark}/60, Satisfactory")
else:
    print(f"{mark}/60, Failed")


