def second_largest(numbers):
    m1 = m2 = 0
    for x in numbers:
        if x >= m1:
            m1, m2 = x, m1
        elif x > m2:
            m2 = x
    return m2

def second_smallest(numbers):
    m1 = m2 = float('inf')
    for x in numbers:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
    return m2

print(second_largest([45, 56, 32, 12]))