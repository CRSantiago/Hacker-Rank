# Task
# Given  sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

# Input Format

# The first line of input contains an integer, M.
# The second line contains M space-separated integers.
# The third line contains an integer, N.
# The fourth line contains N space-separated integers.

# Output Format

# Output the symmetric difference integers in ascending order, one per line.

# Sample Input

# 4
# 2 4 5 9
# 4
# 2 4 11 12
# Sample Output

# 5
# 9
# 11
# 12

if __name__ == '__main__':
    n1 = int(input())
    set1 = set(map(int, input().split()))
    n2 = int(input())
    set2 = set(map(int, input().split()))

    sym_dif = set1.difference(set2)
    sym_dif2 = set2.difference(set1)
    difference_set = sym_dif|sym_dif2
    
    for value in sorted(difference_set):
        print(value)
    