if __name__  == '__main__':
    arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append(name,score)
    second_lowest = sorted(set([score for name, score in arr]))[1]
    print('\n'.join(sorted([name for name, score in arr if score == second_lowest])))