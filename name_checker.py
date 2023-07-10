from ValidationException import ValidationException

def validate_file(file_path):
    pass #TODO: Only add code inside this function.
    with open(file_path, 'r') as file:
        next(file)
        for line in file:
            first_name = line.split(',')[0]
            if any(char.isdigit() for char in first_name):
                raise ValidationException(f"Invalid first name: {first_name}")

def name_checker():
    try:
        validate_file('users.txt')
    except ValidationException as validation:
        print(validation)

name_checker()