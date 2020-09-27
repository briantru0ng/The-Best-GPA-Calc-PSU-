# Author: Brian Truong bqt5199@psu.edu

def useLettergrade(n):
  topGPA=0
  bottomGPA=0
  factor=1
  while (0<factor<=(n)):
    lgrade = input(f"Enter your course {factor} letter grade: ")
    credit= float(input(f"Enter your course {factor} credit: "))
    print(f"Grade point for course {factor} is: {getLetterpoint(lgrade)}")
    factor+=1

    topGPA+= getLetterpoint(lgrade)*credit 
    bottomGPA+=credit
    GPA= topGPA/bottomGPA
  return (GPA)


def usePointgrade(n):
  topGPA=0
  factor=1
  while (0<factor<=(n)):
    pgrade = int (input(f"Enter your course {factor} point grade: "))
    topGPA += pgrade
    print(f"Grade point for course {factor} is: {topGPA}")
    GPA= topGPA/factor
    factor+=1
  return (GPA)


def getLetterpoint(lgrade):

  if lgrade=="A" or lgrade=="a":
    pgrade= float(4.0)
  elif lgrade=="A-" or lgrade=="a-":
    pgrade= float (3.67)
  elif lgrade=="B+" or lgrade=="b+":
    pgrade= float (3.33)
  elif lgrade=="B" or lgrade=="b":
    pgrade= float (3.0)
  elif lgrade == "B-" or lgrade=="b-":
    pgrade= float (2.67)
  elif lgrade == "C+" or lgrade=="c+":
    pgrade= float (2.33)
  elif lgrade == "C" or lgrade=="c":
    pgrade= float (2.0)
  elif lgrade == "D" or lgrade=="d":
    pgrade= float (1.0)
  else:
    pgrade= float(0.0)
    
  return (pgrade)


def run():

  what_kind_of_grades=1
  go_again=1

  if go_again==1:
  
    how_many_classes= int( input ("How many classes are you taking: "))
    what_kind_of_grades= int(input("Are you using point grades(1) or letter grades(2)?: "))

    while 0>what_kind_of_grades >= 3:
      what_kind_of_grades= int(input("Are you using point grades(1) or letter grades(2)?: "))
    
    if what_kind_of_grades==1:
      print (f"Your GPA is: {usePointgrade(how_many_classes)}")
    elif what_kind_of_grades==2:
      print (f"Your GPA is: {useLettergrade(how_many_classes)}")
   

    if go_again!=2:
      go_again=int(input("Do you want to go again? "))
      


if __name__ == "__main__":
  run()
