import os
import sys
from datetime import datetime

VERSION_FILE = 'version'
LOG_FILE = 'version_log'

def read_version():
    """Читает текущую версию из файла."""
    if not os.path.exists(VERSION_FILE):
        return None
    with open(VERSION_FILE, 'r') as f:
        return f.read().strip()

def write_version(version):
    """Записывает новую версию в файл."""
    with open(VERSION_FILE, 'w') as f:
        f.write(version)
def log_version_change(old_version, new_version, update_type):
    """Записывает изменения версии в лог-файл."""
    timestamp = datetime.now().strftime('%d.%m.%Y %H:%M:%S.%f')[:-3]
    log_entry = f"\n[{new_version}] <- [{old_version}] [{timestamp}] {update_type} update"
    with open(LOG_FILE, 'a') as f:
        f.write(log_entry)

def increment_version(version, update_type):
    """Инкрементирует версию в зависимости от типа обновления."""
    major, minor, patch = map(int, version.split('.'))

    if update_type == 'major':
        major += 1
        minor = 0
        patch = 0
    elif update_type == 'minor':
        minor += 1
        patch = 0
    elif update_type == 'patch':
        patch += 1
    else:
        raise ValueError("Invalid update type. Use 'major', 'minor', or 'patch'.")

    return f"{major}.{minor}.{patch}"

def main(update_type):
    """Основная функция для обработки обновления версии."""
    version = read_version()

    if version is None:
        version = "1.0.0"
        write_version(version)

    old_version = version
    new_version = increment_version(version, update_type)
    write_version(new_version)
    log_version_change(old_version, new_version, update_type)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    update_type = sys.argv[1]
    main(update_type)