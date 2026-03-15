#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# Forzar a que los errores de decodificación no rompan el programa
# Esto hará que los caracteres extraños se ignoren o se reemplacen
if sys.platform == 'win32':
    import _locale
    _locale._getdefaultlocale = (lambda *args: ['es_ES', 'cp1252'])


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pythonV.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
