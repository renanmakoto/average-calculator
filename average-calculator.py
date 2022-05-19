grade1 = float(input('\033[1;30mType your mid-test grade: '))
grade2 = float(input('\033[1;30mType you final test grade: '))
grade3 = (grade1 + grade2) / 2
if grade3 >= 7.0:
    print('\033[1;30mYour final grade is \033[1;34m{:.2f}\033[1;30m. Congratulations, you have passed to the next level.'.format(grade3))
elif grade3 < 7.0:
    print('\033[1;30mUnfortunately, your final grade is \033[1;31m{:.2f}\033[1;30m. You did not reach the minimum to pass. \033[4;30mTalk to you coordinator.'.format(grade3))
