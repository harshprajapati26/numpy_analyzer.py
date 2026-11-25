import numpy as np


class DataAnalytics:

    def __init__(self, array=None):
        self.array = array

    # Create Array
    def create_array(self):
        print("\n1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        choice = input("Choose array type: ")

        if choice == "1":
            values = list(map(int, input("Enter elements: ").split()))
            self.array = np.array(values)

        elif choice == "2":
            rows = int(input("Enter rows: "))
            cols = int(input("Enter columns: "))
            values = list(map(int, input("Enter elements: ").split()))
            self.array = np.array(values).reshape(rows, cols)

        elif choice == "3":
            layers = int(input("Enter layers: "))
            rows = int(input("Enter rows: "))
            cols = int(input("Enter columns: "))
            values = list(map(int, input("Enter elements: ").split()))
            self.array = np.array(values).reshape(layers, rows, cols)

        else:
            print("Invalid choice!")
            return

        print("Array created successfully:")
        print(self.array)

    # Mathematical Operations
    def math_operations(self):
        if self.array is None:
            print("Create an array first!")
            return

        values = list(map(int, input("Enter second array: ").split()))
        second = np.array(values).reshape(self.array.shape)

        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Choose operation: ")

        if choice == "1":
            print("Result:", self.array + second)
        elif choice == "2":
            print("Result:", self.array - second)
        elif choice == "3":
            print("Result:", self.array * second)
        elif choice == "4":
            print("Result:", self.array / second)
        else:
            print("Invalid choice!")

    # Combine and Split
    def combine_split(self):
        if self.array is None:
            print("Create an array first!")
            return

        print("1. Combine Arrays")
        print("2. Split Array")

        choice = input("Choose option: ")

        if choice == "1":
            values = list(map(int, input("Enter another array: ").split()))
            second = np.array(values).reshape(self.array.shape)

            result = np.concatenate((self.array, second), axis=0)
            print("Combined Array:")
            print(result)

        elif choice == "2":
            parts = int(input("Enter number of parts: "))
            result = np.array_split(self.array, parts)
            print("Split Arrays:")
            print(result)

    # Search, Sort and Filter
    def search_sort_filter(self):
        if self.array is None:
            print("Create an array first!")
            return

        print("1. Search")
        print("2. Sort")
        print("3. Filter")

        choice = input("Choose option: ")

        if choice == "1":
            value = int(input("Enter value to search: "))
            print("Positions:", np.where(self.array == value))

        elif choice == "2":
            print("Sorted Array:")
            print(np.sort(self.array, axis=-1))

        elif choice == "3":
            value = int(input("Filter values greater than: "))
            print(self.array[self.array > value])

    # Statistics
    def statistics(self):
        if self.array is None:
            print("Create an array first!")
            return

        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        print("6. Minimum and Maximum")
        print("7. Percentile")

        choice = input("Choose option: ")

        if choice == "1":
            print("Sum:", np.sum(self.array))

        elif choice == "2":
            print("Mean:", np.mean(self.array))

        elif choice == "3":
            print("Median:", np.median(self.array))

        elif choice == "4":
            print("Standard Deviation:", np.std(self.array))

        elif choice == "5":
            print("Variance:", np.var(self.array))

        elif choice == "6":
            print("Minimum:", np.min(self.array))
            print("Maximum:", np.max(self.array))

        elif choice == "7":
            p = float(input("Enter percentile: "))
            print("Percentile:", np.percentile(self.array, p))

    # Indexing and Slicing
    def indexing_slicing(self):
        if self.array is None:
            print("Create an array first!")
            return

        print("1. Indexing")
        print("2. Slicing")

        choice = input("Choose option: ")

        if choice == "1":
            index = int(input("Enter index: "))
            print("Element:", self.array.flat[index])

        elif choice == "2":
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Sliced Array:", self.array.flat[start:end])

    @classmethod
    def about(cls):
        print("Welcome to NumPy Analyzer")

    @staticmethod
    def correlation(a, b):
        print("Correlation:", np.corrcoef(a, b))


# Main Program
def main():

    analyzer = DataAnalytics()
    DataAnalytics.about()

    while True:

        print("\n===== NUMPY ANALYZER =====")
        print("1. Create Array")
        print("2. Mathematical Operations")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort or Filter")
        print("5. Statistics")
        print("6. Indexing and Slicing")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            analyzer.create_array()

        elif choice == "2":
            analyzer.math_operations()

        elif choice == "3":
            analyzer.combine_split()

        elif choice == "4":
            analyzer.search_sort_filter()

        elif choice == "5":
            analyzer.statistics()

        elif choice == "6":
            analyzer.indexing_slicing()

        elif choice == "7":
            print("Thank you for using NumPy Analyzer!")
            break

        else:
            print("Invalid choice!")


main()
