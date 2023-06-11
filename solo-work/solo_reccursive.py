#find_max
def find_max(tablica):
    if len(tablica) == 0:
        return "The array is empty"
    elif len(tablica) == 1:
        return tablica[0]
    else:
        current = tablica[0]
        rest_max = find_max(tablica[1:])
        return max(current, rest_max)


#pseudokod do find_max:
#
# find_max(tablica)
#     jeśli tablica ma 0 elementów --> zwróć string "The array is empty"
#     jeśli tablica ma 1 element --> zwróć pierwszy element
#     jeśli tablica ma więcej niż 1 element -->
#           przypisz do zmiennej current wartość pierwszego elementu
#           przypisz do zmiennej rest_max wynik wykonania funkcji find_max z argumentem tablica skróconym o pierwszy element
#           zwróć większą z current i rest_max

moja_tablica = [1, 5, 6, 7, 10, 89, 2]
print("Found max: ", find_max(moja_tablica))


def sum_list(l):
    if len(l) == 0:
        return 0
    else:
        data = l[0]
        l.pop(0)
        return data + sum_list(l)

# pseudokod do sum_list(l)
#     czy l jest puste?
#         jeśli tak --> zwróć 0
#         jeśli nie --> zwróć sumę pierwszego elementu tablicy i wyniku funkcji sum_list z argumentem l skróconym o pierwszy element


l = [10, 20, 30, 40, 50]
print(str(sum_list(l)))

#silnia

def factorial(liczba):
    if liczba == 1:
        return 1
    else:
        return liczba * factorial(liczba - 1)

#dla liczby n mnożymy każdą liczbę od 1 do n, czyli 5! = 1*2*3*4*5
# Pseudokod:
# def factorial(n):
#       jeśli n wynosi 1 --> zwróć 1
#       w przeciwnym wypadkku --> zwróć sumę n oraz factorial(n-1)

print(factorial(5))

#ciąg Fiboniacciego

def fibonacci(fib):
    if fib <= 0:
        return "Input must be a positive number and yours apparently isn't"
    elif fib == 1 or fib == 2:
        return 0
    else:
        return fibonacci(fib - 1) + fibonacci(fib - 2)

# Pseudokod:
# funckja fibonacci(fib)
#     jeśli fib jest mniejsze/równe zero --> zwróć string "Input must be a positive number and yours apparently isn't"
#     jeśli fib równa się 1 lub 2 --> zwróć 0
#     jeśli jest inaczej --> zwróć sumę fibonacci(fib - 1) oraz fibonacci(fib - 2)


abc = 8
fib_try = fibonacci(abc)
print(f"Your result: {fib_try}")

#sudoku 4x4

Board = list[list[int]]
# Typ Board jest listą list liczb całkowitych - planszą sudoku


def is_legal(board: Board, sub_cell_size: int) -> bool:
    return len(board) == len(board[0]) and len(board) % sub_cell_size == 0
# Pseudokod dla funkcji is_legal(board, sub_cell_size):
#     zwróć prawdę jeśli:
#         - liczba wierszy jest równa liczbie kolumn i jest podzielna przez rozmiar komórki
#     zwróć fałsz w przeciwnym wypadku


def is_solved(board: Board) -> bool:
    return all(all(cell != 0 for cell in row) for row in board)
# Pseudokod dla funkcji is_solved(board):
#     zwróć prawdę jeśli:
#         - każda komórka w każdym wierszu jest różna od 0
#     zwróć fałsz w przeciwnym wypadku


def is_row_completed(board: Board, row: int) -> bool:
    return len(set(board[row])) == len(board)
# Pseudokod dla funkcji is_row_completed(board, row):
#     zwróć prawdę jeśli:
#         - liczba unikalnych wartości w wierszu jest równa liczbie kolumn
#     zwróć fałsz w przeciwnym wypadku


def is_col_completed(board: Board, col: int) -> bool:
    return len(set(row[col] for row in board)) == len(board)
# Pseudokod dla funkcji is_col_completed(board, col):
#     zwróć prawdę jeśli:
#         - liczba unikalnych wartości w kolumnie jest równa liczbie kolumn
#     zwróć fałsz w przeciwnym wypadku


def is_sub_cell_completed(board: Board, sub_cell_size: int, row: int, col: int) -> bool:
    return len(set(board[i][j] for i in range(row // sub_cell_size * sub_cell_size, row // sub_cell_size * sub_cell_size + sub_cell_size) for j in range(col // sub_cell_size * sub_cell_size, col // sub_cell_size * sub_cell_size + sub_cell_size))) == (len(board) / sub_cell_size) ** 2
# Pseudokod dla funkcji is_sub_cell_completed(board, sub_cell_size, row, col):
#     zwróć prawdę jeśli:
#         - liczba unikalnych wartości w komórce jest równa rozmiarowi komórki podniesionemu do kwadratu (np. dla rozmiaru komórki 3x3 będzie to 9)
#     zwróć fałsz w przeciwnym wypadku


def is_completed(board: Board, sub_cell_size: int) -> bool:
    return all(is_row_completed(board, row) and is_col_completed(board, col) for row in range(len(board)) for col in range(len(board))) and all(is_sub_cell_completed(board, sub_cell_size, row, col) for row in range(0, (len(board) // sub_cell_size)) for col in range(0, (len(board) // sub_cell_size)))
# Pseudokod dla funkcji is_completed(board, sub_cell_size):
#     zwróć prawdę jeśli:
#         - każdy wiersz i kolumna jest ukończona (funkcje is_row_completed i is_col_completed) oraz każda komórka jest ukończona (funkcja is_sub_cell_completed)
#     zwróć fałsz w przeciwnym wypadku


def get_fields_domain(board: Board, sub_cell_size: int, field_coords: tuple[int, int]) -> list[int]:
    initial_domain = set(range(1, len(board) + 1))

    row_domain = set(board[field_coords[0]])
    col_domain = set(row[field_coords[1]] for row in board)
    sub_cell_domain = set(board[i][j] for i in range(field_coords[0] // sub_cell_size * sub_cell_size, field_coords[0] // sub_cell_size * sub_cell_size + sub_cell_size)
                          for j in range(field_coords[1] // sub_cell_size * sub_cell_size, field_coords[1] // sub_cell_size * sub_cell_size + sub_cell_size))

    final_domain = initial_domain - row_domain - col_domain - sub_cell_domain
    return list(final_domain)
# Pseudokod dla funkcji get_fields_domain(board, sub_cell_size, field_coords):
#     stwórz zbiór initial_domain zawierający liczby od 1 do rozmiaru planszy
#     stwórz zbiór row_domain zawierający wartości z wiersza o indeksie field_coords[0]
#     stwórz zbiór col_domain zawierający wartości z kolumny o indeksie field_coords[1]
#     stwórz zbiór sub_cell_domain zawierający wartości z komórki o indeksie field_coords[0] i field_coords[1]
#     stwórz zbiór final_domain będący różnicą zbioru initial_domain i zbiorów row_domain, col_domain oraz sub_cell_domain
#     zwróć listę final_domain


def is_domain_solved(domain: list[int]) -> bool:
    return len(domain) == 1
# Pseudokod dla funkcji is_domain_solved(domain):
#     zwróć prawdę jeśli:
#         - liczba elementów w zbiorze jest równa 1
#     zwróć fałsz w przeciwnym wypadku


def recursive_solve(board: Board, sub_cell_size: int) -> bool:
    if is_solved(board):
        return True

    iteration_solved = False

    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == 0:
                current_field_coords = (x, y)
                field_domain = get_fields_domain(
                    board, sub_cell_size, current_field_coords)
                if is_domain_solved(field_domain):
                    board[x][y] = field_domain[0]
                    iteration_solved = True

    if iteration_solved:
        return recursive_solve(board, sub_cell_size)
    else:
        return False
# Pseudokod dla funkcji recursive_solve(board, sub_cell_size):
#     jeśli plansza jest ukończona (funkcja is_completed):
#         zwróć prawdę
#     przypisz do zmiennej iteration_solved wartość fałsz
#     dla każdego x od 0 do rozmiaru planszy:
#         dla każdego y od 0 do rozmiaru planszy:
#             jeśli wartość w polu o indeksie (x, y) jest równa 0:
#                 przypisz do zmiennej current_field_coords krotkę (x, y)
#                 przypisz do zmiennej field_domain zbiór wartości zwrócony przez funkcję get_fields_domain dla argumentów board, sub_cell_size oraz current_field_coords
#                 jeśli zbiór field_domain zawiera tylko jedną wartość (funkcja is_domain_solved):
#                     przypisz do pola o indeksie (x, y) wartość zwróconą wcześniej przez funkcję get_fields_domain
#                     przypisz do zmiennej iteration_solved wartość prawda
#     jeśli iteration_solved jest prawdą:
#         zwróć wynik funkcji recursive_solve dla argumentów board oraz sub_cell_size
#     w przeciwnym wypadku:
#         zwróć fałsz


board_4x4 = [
    [0, 4, 0, 2],
    [0, 0, 3, 4],
    [1, 2, 0, 0],
    [4, 0, 2, 0]
]
sub_cell_size_4x4 = 2

board_9x9 = [
    [1, 0, 0, 4, 8, 9, 0, 0, 6],
    [7, 3, 0, 0, 0, 0, 0, 4, 0],
    [0, 0, 0, 0, 0, 1, 2, 9, 5],
    [0, 0, 7, 1, 2, 0, 6, 0, 0],
    [5, 0, 0, 7, 0, 3, 0, 0, 8],
    [0, 0, 6, 0, 9, 5, 7, 0, 0],
    [9, 1, 4, 6, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 0, 3, 7],
    [8, 0, 0, 5, 1, 2, 0, 0, 4]
]
sub_cell_size_9x9 = 3

if is_legal(board_4x4, sub_cell_size_4x4):
    if recursive_solve(board_4x4, sub_cell_size_4x4):
        if is_completed(board_4x4, sub_cell_size_4x4):
            print("Solution found and valid:")
            print(board_4x4)
        else:
            print("Solution invalid")
    else:
        print("No solution found")

print()

#sudoku 9x9

if is_legal(board_9x9, sub_cell_size_9x9):
    if recursive_solve(board_9x9, sub_cell_size_9x9):
        if is_completed(board_9x9, sub_cell_size_9x9):
            print("Solution found and valid:")
            print(board_9x9)
        else:
            print("Solution invalid")
    else:
        print("No solution found")

