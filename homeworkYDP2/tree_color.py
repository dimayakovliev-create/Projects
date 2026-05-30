import sys
from pathlib import Path
from colorama import init, Fore, Style

init()  # Ініціалізуємо colorama

def colorful_tree(directory_path: Path, indent: str = "") -> None: 
# Рекурсивна функція для візуалізації структури директорії з кольорами (відступу немає, якщо це коренева директорія: ident = "")
    try:
        # Дістаємо папки та файли із шляху та сортуємо спочатку за типом (директорії вгору), потім за назвою (без врахування регістру): папки виводяться першими (False = 0), потім файли (True = 1), і все це в алфавітному порядку
        items = sorted(directory_path.iterdir(), key=lambda x: (x.is_file(), x.name.lower())) 
        for item in items:
            if item.is_dir():
                # Виводимо назву папки синім кольором із косою рисою на кінці
                print(f"{indent}{Fore.BLUE}{Style.BRIGHT}{item.name}{Style.RESET_ALL}/")
                # Для підпапок збільшуємо відступ на 4 пробіли
                colorful_tree(item, indent + "    ")
            else:
                # Виводимо назву файлу зеленим кольором
                print(f"{indent}{Fore.GREEN}{item.name}{Style.RESET_ALL}")
                
    except PermissionError:
        # Якщо виникає помилка доступу до каталогу, виводимо повідомлення червоним кольором
        print(f"{indent}{Fore.RED}[Помилка доступу: {directory_path.name}]{Style.RESET_ALL}")

def main():
    # Перевірка наявності файла та введеного шляху до директорії
    if len(sys.argv) < 2:
        print(f"{Fore.YELLOW}Використання: python goit-pycore-hw-04/tree_color.py <шлях_до_директорії>{Style.RESET_ALL} ")
        sys.exit(1) # Завершуємо програму з кодом помилки 1, якщо аргумент не надано
        
    target_path = Path(sys.argv[1])
    
    # Перевірка існування шляху та чи є він директорією
    if not target_path.exists():
        print(f"{Fore.RED}Помилка: Шлях '{target_path}' не існує.{Style.RESET_ALL}")
        sys.exit(1) # Завершуємо програму з кодом помилки 1, якщо шлях не існує
        
    if not target_path.is_dir():
        print(f"{Fore.RED}Помилка: Шлях '{target_path}' не є директорією.{Style.RESET_ALL}")
        sys.exit(1) # Завершуємо програму з кодом помилки 1, якщо шлях не є директорією
        
    # Якщо все вірно, виводимо кореневу директорію синім кольором із косою рисою на кінці
    print(f"{Fore.BLUE}{Style.BRIGHT}{target_path.absolute()}{Style.RESET_ALL}/")
    # Запускаємо вже саму рекурсивну функцію для візуалізації структури директорії
    colorful_tree(target_path, indent="    ")

if __name__ == "__main__":
    main()
