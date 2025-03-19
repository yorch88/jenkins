import random
from find_min_max import find_min_max_even
def create_random_number_list():
    lista = [random.randint(0,1000) for _ in range(300)]
    even_numbers = [i for i in lista if i%2 == 0]
    percentage_even_numbers = (len(even_numbers)*100)/len(lista)
    if percentage_even_numbers >= 50.00:
        return f"Even min number: {find_min_max_even(even_numbers)[0]}", f"Even max number: {find_min_max_even(even_numbers)[1]}"
    else:
        return "Even numbers shoulbe equal major than 50%"

if __name__ == "__main__":
    print(create_random_number_list())