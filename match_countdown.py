def countdown_to_start():
    for i in range(10, 0, -1):
        if i == 1:
            print("1...Fight!")
        else:
            print(f"{i}...")

# Example usage
def test():
    print("Counting down to match start:")
    countdown_to_start()
    print("=====================================")


def main():
    test()


main()