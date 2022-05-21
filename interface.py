def get_user_input():
    while True:
        answer = input("Do you want to enter or view workouts? Type 'enter', 'remove', or  'view'. ")
        if answer.lower() not in ('enter', 'remove', 'view'):
            print("Please type 'enter', 'remove', or 'view'. ")
            continue
        else:
            break
    return answer.lower()
    
def get_workout_name():
    workout_name = input("Enter workout name: ")
    return workout_name



def get_weight_type():
    weight_type = input("Enter weight type: ")
    return weight_type

def get_muscle_group():
    while True:
        muscle_group = input("Enter muscle group (legs, back, upper body, core, whole body): ")
        if muscle_group not in ('legs', 'back', 'upper body', 'core', 'whole body'): 
            print("Please enter a valid muscle group.")
            continue
        else:
            break
    return muscle_group

def get_reps():
    reps = input("Enter the number of reps.")
    return reps()

def get_sets():
    sets = input("Enter the number of sets.")
    return sets()

def get_weight():
    weight = input("Enter the amount of weight you will be lifting for this segment of the workout.")

def get_filter_criteria():
    muscle_group = get_muscle_group()
    weight_type = get_weight_type()
    return(muscle_group, weight_type)

def get_search_criteria():
    criteria_li = []
    criteria_dict = {}
    while True:
        criteria = input("Enter each search criteria by [type, group] (e.g. barbell, upper body). Enter 'q' to quit. ")
        if criteria == 'q':
            break
        elif len(list(criteria.split(','))) != 2:
            print("Please enter one type with one group. ")
            continue
        else:
            criteria_li.append(list(criteria.split(',')))
            continue

    for entry in criteria_li:
        criteria_dict[entry[0]] = entry[1]
 
    return criteria_dict