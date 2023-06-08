#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import importlib

    hidden_4 = importlib.import_module("hidden_4")
    names = [name for name in dir(hidden_4) if not name.startswith("__")]
    print("\n".join(names))
