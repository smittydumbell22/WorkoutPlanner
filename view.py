import pandas as pd

def print_all_workouts(cnn): 
    sql =  """SELECT workout_name, 
                muscle_group, 
                weight_type
                FROM workout
                INNER JOIN muscle_group USING (muscle_group_id), 
                    weight_type USING (weight_type_id)
             """ 
    workout_df = pd.read_sql_query(sql, cnn) 
    return workout_df        
def print_filtered_workouts(cnn, muscle_group, weight_type):               
    sql =  """SELECT workout_name, 
                muscle_group, 
                weight_type
                FROM workout
                INNER JOIN muscle_group USING (muscle_group_id), 
                    weight_type USING (weight_type_id)
                WHERE muscle_group = "{0}" AND weight_type = "{1}"   
             """.format(muscle_group, weight_type)
    workout_df = pd.read_sql_query(sql, cnn) 
    return workout_df              
def print_workouts(cnn, **database):
    """Use a SQL SELECT statement to retrieve workouts based on selections in your database"""

    sql = """SELECT workout.workout_id, 
                workout.workout_name, 
                muscle_group.muscle_group,
                weight_type.weight_type"""
    
    if len(database) == 1: # if there is only one search key, sql string is different
        values = database.popitem()
        if isinstance(values[1], str): # if search parameter is a string, need to format as such in the sql query
            sql2 = "WHERE {column} = '{selection}'".format(column=values[0], selection=values[1].lstrip())
        else:
            sql2 = "WHERE {column} = {selection}".format(column=values[0], selection=values[1])
        sql = sql + sql2

    count = 0
    if len(database) > 1:
        li = []
        # iterate through all the search parameters in kwargs, format search query accordingly 
        for key, value in database.items():
            if isinstance(value, str): 
                string = "{column} = '{selection}'".format(column = key, selection = value.lstrip())
            else:
                string = "{column} = {selection}".format(column = key, selection = value)
            li.append(string)
        count = 0
        concatstring = ""
        while count < len(li) - 1:
            concatstring = concatstring + li[count] + " OR " #concatenate all the search requirements with an "OR"
            count = count + 1

        concatstring = concatstring + li[len(li) -1]

        sql2 = "WHERE " + concatstring

        sql = sql + sql2

    workout_df = pd.read_sql_query(sql, cnn)

    return workout_df
        


 
    
  
    
