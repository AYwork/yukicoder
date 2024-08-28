def main():
    random_string = input()
    if can_make_copy(random_string):
        print("YES")
    else:
        print("No")

def can_make_copy(random_strings):
        words = ["dream", "dreamer", "erase", "eraser"]

        while random_strings:
            # 末尾が一致するか
            matched = False
            for word in words:
                if random_strings.endswith(word):
                    random_strings = random_strings[:-len(word)]
                    matched = True
                    break
            if not matched:
                return False
        return True

if __name__ == "__main__":
    main()