example_list = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

def sum_value(user_list):
    for value in user_list:
        try:
            numbers = value.split(",")
            sum_numbers = sum(int(number) for number in numbers)
            print(sum_numbers)
        except:
            print("Не можу це зробити!")

sum_value(example_list)
