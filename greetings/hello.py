""" I say hello """
import sys


def get_greeting(*names: list[str]) -> str:
    """Return a greeting message."""
    return f"Hello {' and '.join(names) if names else ''}!"


if __name__ == "__main__":
    _names = sys.argv[1:] if len(sys.argv) > 1 else ["World"]
    print(get_greeting(*_names))
