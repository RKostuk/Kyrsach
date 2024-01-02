import os

from app.services.file_controller import FileController
def test_file_controller():
    test_directory = 'test_files'
    os.makedirs(test_directory, exist_ok=True)
    test_file = 'test.txt'
    test_content = 'Це тестовий файл.'

    with open(os.path.join(test_directory, test_file), 'w', encoding='utf-8') as f:
        f.write(test_content)

    file_controller = FileController(test_directory)

    try:
        assert file_controller.main_directory == test_directory, "Помилка ініціалізації"

        content = file_controller.read_file('', test_file)
        assert content == test_content, "Помилка читання файлу: контент не співпадає"

        non_existent_content = file_controller.read_file('', 'nonexistent.txt')
        assert non_existent_content == f"File not found: {os.path.join(test_directory, 'nonexistent.txt')}", "Помилка: файл мав бути не знайдений"

        print("Усі тести пройшли успішно!")

    except AssertionError as e:
        print(f"Тест не пройдено: {e}")

    finally:
        os.remove(os.path.join(test_directory, test_file))
        os.rmdir(test_directory)