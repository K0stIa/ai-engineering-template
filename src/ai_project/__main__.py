import json

from . import __version__


def main():
    print(json.dumps({"status": "ok", "version": __version__}))


if __name__ == "__main__":
    main()
