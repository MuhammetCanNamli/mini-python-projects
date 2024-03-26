def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):

        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


# Kullanıcıdan giriş sayısını al
num_entries = int(input("How many entries will you provide? "))

# Giriş sayısı kadar giriş al
arr = []
for i in range(num_entries):
    arr.append(int(input("Enter element {}: ".format(i+1))))

# Diziyi sırala
quickSort(arr, 0, len(arr) - 1)

# Sıralanmış diziyi yazdır
print("Sorted array:", arr)