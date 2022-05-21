class Workout:
    def __init__(self, workout_name, weight_type, muscle_group):
        self.workout_name = workout_name
        self.type = weight_type
        self.group = muscle_group
        
    #################
    # inserting workouts
    #################

    # #def insert_workout(self, cnn):
    #     cur = cnn.cursor()

    #     sql = "INSERT INTO workout (workout) SELECT (?) WHERE NOT EXISTS (SELECT 1 FROM workout WHERE workout = ?)"
    #     values = (self.workout, self.workout)
        
    #     cur.execute(sql, values)
    #     cnn.commit()
        
        
    def insert_workout(self, cnn):
        cur = cnn.cursor()

        sql = """INSERT INTO workout(workout_name, weight_type_id, muscle_group_id)
                    VALUES (?,  
                        (SELECT weight_type_id FROM weight_type  WHERE weight_type = ?),
                        (SELECT muscle_group_id FROM muscle_group WHERE muscle_group = ?))"""
        
        values = (self.workout_name, self.group, self.type)

        cur.execute(sql, values)
        cnn.commit()
    
    def workout_exists(workout_name, cnn):
        cur = cnn.cursor()
        sql = """SELECT count(workout_name)
                FROM workout
                WHERE workout_name = ? """
        
        values = (workout_name, )

        cur.execute(sql, values)
        data_count = cur.fetchone()[0]
        if data_count != 0:
            return True
        else:
            return False
        
    def remove_workout(cnn, workout_name):
        cur = cnn.cursor()
        workout_name_exists = Workout.workout_exists(workout_name, cnn)  
        if workout_name_exists == True:
            print(f"removing {workout_name}")
            sql = """DELETE FROM workout
                    WHERE workout_name = ? """
                    
            
            values = (workout_name, )

            cur.execute(sql, values)
            cnn.commit()
        else:
            print(f"{workout_name} does not exist!")
            
        
  