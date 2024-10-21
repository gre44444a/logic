import random
import logging

logging.basicConfig(filename='game_log.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_event(event):
    logging.info(event)

def get_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError("Значение должно быть натуральным числом.")
            return value
        except ValueError as e:
            log_event(f"Ошибка ввода: {e}")
            print("Неверный ввод. Пожалуйста, введите натуральное число.")


def main():
    N = get_input("Введите натуральное число N: ")
    k = get_input("Введите количество попыток k: ")

    secret_number = random.randint(1, N)
    log_event(f"Сгенерировано случайное число: {secret_number}")

    attempts = 0

    while attempts < k:
        guess = get_input(f"Попытка {attempts + 1}: Угадайте число (от 1 до {N}): ")

        log_event(f"Попытка пользователя: {guess}")

        if guess < secret_number:
            print("Загаданное число больше.")
            log_event("Ответ программы: Загаданное число больше.")
        elif guess > secret_number:
            print("Загаданное число меньше.")
            log_event("Ответ программы: Загаданное число меньше.")
        else:
            print(f"Поздравляем! Вы угадали число {secret_number}.")
            log_event("Поздравление: Пользователь угадал число.")
            break

        attempts += 1

        if attempts == k:
            print(f"Попытки закончились. Загаданное число было {secret_number}.")
            log_event(f"Игра окончена. Загаданное число было {secret_number}.")


if __name__ == "__main__":
    main()