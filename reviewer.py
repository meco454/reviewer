import random

# Checks if the pair of quez-answers are same length
def check_lengths(list1, list2):
    if len(list1) != len(list2):
        print("Warning!!! Not equal question to answer lists!")

    #UNCOMMENT THIS CODE BLOCK TO CHECK FOR LIST LENGTH RELATED ISSUES
    # print(f"list1 length: {len(list1)}")
    # print(f"list2 length: {len(list2)}")

# Variable quez_num refers to the index of question/answer in the list
# answers_copy is a list of the possible answers it'll use
def create_choices(quez_num, answers_copy, ans_choice):
    
    #argument is original answers list, not the copy (to avoid weird behavior as list grows smaller)
    choice_list = random.choices(ans_choice, k = 4)
    if answers_copy[quez_num] not in choice_list:
        choice_list[random.randint(0, 3)] = answers_copy[quez_num]
    
    while(True):
        choice_list = list(set(choice_list))
        if len(choice_list) < 4:
            choice_list.insert(random.randint(0, len(choice_list)), random.choice(ans_choice))
        else:
            break
    
    return choice_list

# Function to create a round of review
def start_round(quez_choice, ans_choice):
    quez_copy = quez_choice.copy()
    answers_copy = ans_choice.copy()

    correct_answers = 0
    wrong_answers = 0
    counter = 1
    for x in range(len(quez_copy)):


        if counter % 50 == 0:
            input("Break time! Input any character to continue: ")

        # Picks a random item number based on quez length
        quez_num = random.choice(range(0, len(quez_copy)))
        print("Question # {}, {}".format(counter, quez_copy[quez_num]))

        # Create the choices for MC type
        # added another argument so that choices will be from original answers list not the copy to avoid weird behavior later on
        choice_list = create_choices(quez_num, answers_copy, ans_choice)
        
        print("Choices: ", choice_list)
        user_answer = input("Enter your answer: ")

        # Check if answers are correct
        if user_answer.upper() == answers_copy[quez_num].upper():
            print("Correct!")
            correct_answers += 1
        else:
            print("Wrong! Answer is: " , answers_copy[quez_num])
            wrong_answers += 1

        quez_copy.pop(quez_num)
        answers_copy.pop(quez_num)

        counter+=1

    else: # End questions
        print("Good Work!!")
        print("Stats: Correct answers:", correct_answers)
        print("Wrong Answers:", wrong_answers)
        print("Number of questions", len(quez_choice))

# Input: name of the subject/file to be loaded
# Output: 2 lists: the quez list and ans list
def load_items(quezname, ansname):
    quez_list = []
    ans_list = []
    
    f_quez = open(quezname, "r", encoding = "utf8")
    for item in f_quez:
        quez_list.append(str(item).strip())
    f_quez.close()

    f_ans = open(ansname, "r", encoding = "utf8")
    for item in f_ans:
        ans_list.append(str(item).strip())
    f_ans.close()

    return quez_list, ans_list

# = = = = = = = = = = = =
# MAIN FUNCTION GOES HERE
# = = = = = = = = = = = = 

def main():
    print("Choose which question set you'd like to use:")
    print("1 - SEN02 Midterms")
    print("2 - IAS01 Midterms")
    print("3 - PTF03 Midterms")
    print("4 - SEN02 Module 4 & 5")
    print("5 - SEN02 Mod 6 Azure PPT 1")
    print("Any other input - Enter your own file")
    
    # I'm too lazy to handle error checking, just assume they put a number
    choicenum = int(input("Enter: "))
    
#    if choicenum == 1:
#        questions, answers = load_items("quez1.txt", "ans1.txt")
#    elif choicenum == 2:
#        questions, answers = load_items("quez2.txt", "ans2.txt")
#    elif choicenum == 3:
#        questions, answers = load_items("quez3.txt", "ans3.txt")
#    else:
#        print("Haiyaaaa, you fucked up")
#        exit()

#    The above part looks like it can be made less redundant with the following code:

    if choicenum <= 0 or choicenum > 5:
        print("Haiyaaaa, you fucked up")
        exit()
    else:
        # Used f-string to insert the choicenum
        questions, answers = load_items(f"quez{choicenum}.txt", f"ans{choicenum}.txt")
    
    check_lengths(questions, answers)
    start_round(questions, answers)

main()
