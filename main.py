from ddns import *


def main():
    ddns = DDNS("61083", "30da406fb516e52be45ed7ec92b58323")
    ddns.update()


if __name__ == '__main__':
    main()
