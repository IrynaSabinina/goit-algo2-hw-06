import hashlib

class BloomFilter:
    def __init__(self, size: int, num_hashes: int):
        """
        Ініціалізація фільтра Блума.
        :param size: розмір бітового масиву
        :param num_hashes: кількість хеш-функцій
        """
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = [0] * size

    def _hashes(self, item: str):
        """
        Генерує num_hashes різних хешів для елемента.
        Використовує hashlib з різними сілтами.
        """
        item = str(item)
        for i in range(self.num_hashes):
            # створюємо різні хеші через додавання різних сілт
            hash_value = int(hashlib.md5((item + str(i)).encode('utf-8')).hexdigest(), 16)
            yield hash_value % self.size

    def add(self, item: str):
        """
        Додає елемент до фільтра Блума.
        """
        if not isinstance(item, str) or item.strip() == "":
            return  # пропускаємо некоректні значення
        for hash_val in self._hashes(item):
            self.bit_array[hash_val] = 1

    def __contains__(self, item: str) -> bool:
        """
        Перевіряє, чи може елемент бути у фільтрі.
        Може дати false positive, але не false negative.
        """
        if not isinstance(item, str) or item.strip() == "":
            return False
        return all(self.bit_array[hash_val] for hash_val in self._hashes(item))


def check_password_uniqueness(bloom: BloomFilter, new_passwords: list[str]) -> dict[str, str]:
    """
    Перевіряє список нових паролів на унікальність, використовуючи фільтр Блума.
    :param bloom: екземпляр BloomFilter
    :param new_passwords: список паролів для перевірки
    :return: словник {пароль: статус}
    """
    results = {}

    for password in new_passwords:
        if not isinstance(password, str) or password.strip() == "":
            results[password] = "некоректний пароль"
            continue

        if password in bloom:
            results[password] = "вже використаний"
        else:
            results[password] = "унікальний"
            bloom.add(password)

    return results


# 🔹 Приклад використання (як у завданні)
if __name__ == "__main__":
    print("Starting the Bloom Filter Test...")  # Add this to check if it runs
    # Ініціалізація фільтра Блума
    bloom = BloomFilter(size=1000, num_hashes=3)

    # Додавання існуючих паролів
    existing_passwords = ["password123", "admin123", "qwerty123"]
    for password in existing_passwords:
        bloom.add(password)

    # Перевірка нових паролів
    new_passwords_to_check = ["password123", "newpassword", "admin123", "guest"]
    results = check_password_uniqueness(bloom, new_passwords_to_check)

    # Виведення результатів
    for password, status in results.items():
        print(f"Пароль '{password}' — {status}.")
