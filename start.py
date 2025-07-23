import subprocess
import time
from watchfiles import watch
import sys
import os


def run_bot():
    # Запускаем bot/main.py как отдельный процесс
    return subprocess.Popen([sys.executable, os.path.join("bot", "main.py")])


if __name__ == "__main__":
    process = run_bot()
    print("Бот запущен. Ожидание изменений в коде...")
    for changes in watch("bot"):
        print("Обнаружены изменения в коде. Перезапуск бота через 20 секунд...")
        process.terminate()
        process.wait()
        time.sleep(20)  # задержка перед рестартом
        process = run_bot()
