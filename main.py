from manager import Manager

def main():
    manager = Manager()
    manager.push(b"2")
    print(manager.pop(1))

if __name__ == "__main__":
    main()