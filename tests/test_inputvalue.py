# content of test_sample.py
def func(x):
    return x + 1
def test_answer():
    assert func(3) == 4

def user_input_dialogue():
    IsNotAnInteger = True
    input_value = None
    while IsNotAnInteger:
        input_value = input("Please input a team size: ")
        match_val = re.match("[-+]?\\d+$", input_value)
        if match_val is None:
            print("Please enter a valid integer.")
        else:
            IsNotAnInteger = False
    return int(input_value)

def test_user_input_dialogue():
    assert user_input_dialogue() == 3