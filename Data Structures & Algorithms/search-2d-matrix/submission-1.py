class Solution:
    def searchMatrix(self, matrix, target) -> bool:
        t, b = 0, len(matrix) - 1
        while t <= b:
            mid = ((t + b) // 2)
            midArr = matrix[mid]
            if target >= midArr[0] and target <= midArr[len(midArr) - 1]:
                return self.binarySearch(midArr, target)
            elif target > midArr[len(midArr) - 1]:
                t = mid + 1
            else:
                b = mid - 1
        return False

    def binarySearch(self, arr, target):
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = ((l + r) // 2)
            if arr[mid] < target:
                l = mid + 1
            elif arr[mid] > target:
                r = mid - 1
            else:
                return True
        return False