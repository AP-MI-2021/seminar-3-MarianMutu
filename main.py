"""
Scrieți un program cu meniu (meniul va conține o opțiune care oprește programul) care suportă operațiile:

- Citirea unei liste de float-uri. Citirile repetate suprascriu listele precedente.
- Afișarea tuturor numerelor întregi din listă.
- Afișarea celui mai mare număr divizibil cu un număr citit de la tastatură.
- Afișarea tuturor float-urilor ale căror parte fracționară este palindrom.
- Afișarea listei obținute din lista inițială în care float-urile cu partea
întreagă a radicalului număr prim sunt puse ca string-uri cu caracterele în ordine inversă.
"""
import math


def get_int_elements(lst):
    """
    Determinarea tuturor numerelor întregi din listă
    :param lst: float
    :return: int
    """
    rez = []
    for x in lst:
        if x == int(x):
            rez.append(int(x))
    return rez


def test_get_int_elements():
    assert get_int_elements([12.0, 6, 8.9, 9.0, 10]) == [12, 6, 9, 10]
    assert get_int_elements([]) == []


def get_max_div_k(lst, k):
    """
    determina cel mai mare numar din lst divizibil cu k
    :param lst: float
    :param k: int
    :return: int
    """
    max_div = None
    for x in get_int_elements(lst):
        if x % k == 0:
            if max_div == None or x > max_div:
                max_div = x
    return max_div


def test_get_max_div_k():
    assert get_max_div_k([12.0, 14.5, 78.0, 8], 2) == 78
    assert get_max_div_k([16.8, 9, 78.9, 67, -50], 10) == -50
    assert get_max_div_k([], 8) == None


def is_palindrome(x):
    """
determina daca un nr x scris ca sir de caractere e palindrom sau nu
    :param x: string
    :return: true or false
    """
    og = x[::-1]
    if x == og:
        return True
    return False


def test_is_palindrome():
    assert is_palindrome('123') == False
    assert is_palindrome('121') == True
    assert is_palindrome('8') == True


def get_fractional_part(x):
    """
    Determina partea fractionara a unui nr real
    :param x: float
    :return: int
    """
    float_x = float(x)
    str_float_x = str(float_x)
    poz = str_float_x.find(".")
    return str_float_x[poz+1:len(str_float_x)]


def test_get_fractional_part():
    assert get_fractional_part(1.45) == '45'
    assert get_fractional_part(9.0) == '0'
    assert get_fractional_part(8) == '0'
    assert get_fractional_part(-3.87) == '87'


def palindrome_fractional_part(lst):
    """
    determina daca un float are partea fracționară palindrom
    :param lst: float
    :return: float
    """
    rez = []
    for x in lst:
        fractional_part = get_fractional_part(x)
        if is_palindrome(fractional_part):
            rez.append(x)
    return rez


def test_palindrome_fractional_part():
    assert palindrome_fractional_part([12.121, 1.1, 13.01]) == [12.121, 1.1]
    assert palindrome_fractional_part([12.0, 1.1, 8.98]) == [12.0, 1.1]
    assert palindrome_fractional_part([]) == []


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0 and n != 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def test_is_prime():
    assert is_prime(34) == False
    assert is_prime(3) == True
    assert is_prime(-4) == False
    assert is_prime(1) == False


def get_sqrt_n_prime_in_reverse(lst):
    """
    detereminarea float-urilor cu partea întreagă a radicalului număr prim care
    sunt puse ca string-uri cu caracterele în ordine inversă
    :param lst:
    :return:
    """
    rez = []
    for x in lst:
        if is_prime(int(math.sqrt(x))):
            val = str(x)
            val = val[::-1]
            rez.append(val)
        else:
            rez.append(x)
    return rez

def test_get_sqrt_n_prime_in_reverse():
    assert get_sqrt_n_prime_in_reverse([10.0, 100.0, 12.45]) == ['0.01', 100.0, '54.21']
    assert get_sqrt_n_prime_in_reverse([50.0, 101.2]) == ['0.05', 101.2]
    assert get_sqrt_n_prime_in_reverse([]) == []


def read_list():
    """
    Citirea unei liste de float-uri.
    :return: lst
    """
    list_str = input("Introduceti termenii listei: ").split(" ")
    lst = []
    for x in list_str:
        lst.append(float(x))
    return lst


def show_menu():
    print("""
1. Citirea unei liste de float-uri. Citirile repetate suprascriu listele precedente.
2. Afișarea tuturor numerelor întregi din listă.
3. Afișarea celui mai mare număr divizibil cu un număr citit de la tastatură.
4. Afișarea tuturor float-urilor ale căror parte fracționară este palindrom.
5. Afișarea listei obținute din lista inițială în care float-urile cu partea
întreagă a radicalului număr prim sunt puse ca string-uri cu caracterele în ordine inversă.
x. Iesire
    """)


def main():
    lst = []
    while True:
        show_menu()
        cmd = input("Introduceti o comanda: ")
        if cmd == '1':
            lst = read_list()
        elif cmd == '2':
            print(get_int_elements(lst))
        elif cmd == '3':
            k = int(input("Introduceti k: "))
            print(get_max_div_k(lst, k))
        elif cmd == '4':
            print(palindrome_fractional_part(lst))
        elif cmd == '5':
            print(get_sqrt_n_prime_in_reverse(lst))
        elif cmd == 'x':
            break
        else:
            print("Comanda invalida")


if __name__ == '__main__':
    test_get_int_elements()
    test_get_max_div_k()
    test_palindrome_fractional_part()
    test_is_palindrome()
    test_get_fractional_part()
    test_is_prime()
    test_get_sqrt_n_prime_in_reverse()
    main()
