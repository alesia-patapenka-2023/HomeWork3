if __name__=='__main__':
    def sum_of_digits(n):
        digits = [int(digit) for digit in str(n)]  # Преобразуем число в список цифр
        digits_sum = sum(digits)  # Суммируем все цифры из списка
        return digits_sum

with open('test_numbers.csv', 'r') as file:
    numbers = [int(line.strip()) for line in file]
    for number in numbers:
        sum_of_number = sum_of_digits(number)
        print(f'Input number: {number}, Sum of digits: {sum_of_number}')