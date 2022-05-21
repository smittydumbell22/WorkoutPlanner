from interface import *
from startup import *
from workout import *
from view import *



def main():
    cnn = create_cnn(r"workouts.db")

    with cnn:
        # if first starting out, otherwise remove
        create_tables(cnn)
        insert_known_table_values(cnn)
        
        # enter option menu
        ans = get_user_input()
        
        #### If user wants to enter a workout ####
        if ans == 'enter':        
            workout_name = get_workout_name()
            weight_type = get_weight_type()
            muscle_group = get_muscle_group()

            workout = Workout(workout_name, muscle_group, weight_type)

            workout.insert_workout(cnn)
            
         #### If user wants to remove a workout ####
        if ans == 'remove':        
            workout_name = get_workout_name()
            

            Workout.remove_workout(cnn, workout_name)

        
        #### If user wants to view workouts ####
        if ans == 'view':
            ans_all = input("view all workouts?")
            if ans_all == "yes":
                workout_df = print_all_workouts(cnn)
            else:
                
                criteria_tuple = get_filter_criteria()
                workout_df = print_filtered_workouts(cnn, *criteria_tuple) 
            if workout_df.empty:
                print("No workouts to display")
            else:
                print(workout_df)
            
            return workout_df

if __name__ == '__main__':
     main()