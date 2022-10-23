import study

def main():
    with open('data/input1.txt', 'r') as file:
        jewels = file.readline().rstrip()
        stones = file.readline().rstrip()
    print(f'{stones=} {jewels=} {study.counts_s_in_j(jewels, stones)}')



if __name__ == '__main__':
    main()
