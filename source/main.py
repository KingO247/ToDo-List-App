import menu
from Memory import populate
from gooey import Gooey
from argparse import ArgumentParser
@Gooey
def main():
    populate()
    menu.menu()
    parser = ArgumentParser(description="My Cool GUI Program!")
    parser.add_argument('Filename', widget="FileChooser")
    parser.parse_args()



if __name__ == "__main__":
    main()
