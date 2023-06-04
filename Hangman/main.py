with open('game_data.py', 'r') as file:
    new_file_contents = file.read()

global_vars = {}
exec(new_file_contents, global_vars)
my_variable = global_vars.get('data')
print(my_variable)