import socket
import win32print
import win32api
import os
import configparser

def load_settings():
    config = configparser.ConfigParser()
    settings_file = "settings.ini"

    # Проверка наличия файла settings.ini
    if not os.path.exists(settings_file):
        print("Файл settings.ini не найден. Создаем файл с настройками по умолчанию.")
        config["Printer"] = {"name": "Xprinter XP-365B"}
        with open(settings_file, "w") as configfile:
            config.write(configfile)

    config.read(settings_file)
    
    if "Printer" not in config or "name" not in config["Printer"]:
        raise ValueError("Настройки принтера не найдены в файле settings.ini")
    
    return config["Printer"]["name"]

def print_file(data, printer_name):
    file_path = "print_job.pdf"
    
    try:
        # Запись данных в файл
        with open(file_path, "wb") as f:
            f.write(data)
        
        # Настройка принтера
        hprinter = win32print.OpenPrinter(printer_name)
        try:
            # Создание задания на печать
            hjob = win32print.StartDocPrinter(hprinter, 1, ("Print Job", None, "RAW"))
            win32print.StartPagePrinter(hprinter)
            win32print.WritePrinter(hprinter, data)
            win32print.EndPagePrinter(hprinter)
            win32print.EndDocPrinter(hprinter)
            print(f"Файл {file_path} успешно отправлен на печать.")
        finally:
            win32print.ClosePrinter(hprinter)
    except Exception as e:
        print(f"Ошибка при печати: {e}")
    finally:
        # Удаление временного файла
        if os.path.exists(file_path):
            os.remove(file_path)

def start_server(host='0.0.0.0', port=9100):
    printer_name = load_settings()
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Сервер печати запущен на {host}:{port}")
    
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Получено подключение от {addr}")
        try:
            data = bytearray()
            while True:
                packet = client_socket.recv(4096)  # Получение данных файла
                if not packet:
                    break
                data.extend(packet)
            
            if data:
                print_file(data, printer_name)
            else:
                print("Получены пустые данные.")
        except Exception as e:
            print(f"Ошибка при получении данных: {e}")
        finally:
            client_socket.close()

if __name__ == "__main__":
    start_server()
