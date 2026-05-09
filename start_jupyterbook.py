import subprocess
import sys


try:
    subprocess.run(["jupyter-book", "start", "--port", "3000"], check=True)
except subprocess.CalledProcessError as e:
    print(f"Ошибка запуска JupyterBook: {e}", file=sys.stderr)
    sys.exit(1)
except FileNotFoundError:
    print("Ошибка: команда 'jupyter-book' не найдена. Установите JupyterBook: pip install jupyter-book", file=sys.stderr)
    sys.exit(1)