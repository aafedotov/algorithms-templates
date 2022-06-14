# ID: 68871993
class Student:
    """Определяем структуру данных для стажеров."""

    def __init__(self, username, points, penalty):

        self.username = username
        self.points = points
        self.penalty = penalty

    def __gt__(self, other):
        """Определяем компаратор (>) для сравнения студентов."""
        if isinstance(other, Student):
            return (
                    (0 - self.points, self.penalty, self.username) <
                    (0 - other.points, other.penalty, other.username)
                    )
        else:
            raise ValueError('Недопустимый формат для сравнения.')

    def __str__(self):
        """Переопределяем представление для печати."""
        return self.username


def partition(array, start, end):
    pivot = start
    for i in range(start + 1, end + 1):
        if array[i] > array[start]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[start] = array[start], array[pivot]
    return pivot


def qsort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1
    if start >= end:
        return
    pivot = partition(array, start, end)
    qsort(array, start, pivot - 1)
    qsort(array, pivot + 1, end)


def main():

    n = int(input())
    students = []
    for i in range(0, n):
        current = input().split()
        students.append(Student(current[0], int(current[1]), int(current[2])))
    qsort(students)
    for student in students:
        print(student)


if __name__ == '__main__':

    main()
