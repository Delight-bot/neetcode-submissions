class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Case 1: Target found at mid
            if nums[mid] == target:
                return mid

            # Case 2: Determine which half is sorted
            # Check if the left half (from nums[left] to nums[mid]) is sorted
            if nums[left] <= nums[mid]:
                # If the left half is sorted, check if target is within this sorted range
                if nums[left] <= target < nums[mid]:
                    # Target is in the sorted left half, so search there
                    right = mid - 1
                else:
                    # Target is not in the sorted left half, so it must be in the right (unsorted or rotated) half
                    left = mid + 1
            # Case 3: The right half (from nums[mid] to nums[right]) must be sorted
            else:
                # If the right half is sorted, check if target is within this sorted range
                if nums[mid] < target <= nums[right]:
                    # Target is in the sorted right half, so search there
                    left = mid + 1
                else:
                    # Target is not in the sorted right half, so it must be in the left (unsorted or rotated) half
                    right = mid - 1

        # If the loop finishes, the target was not found
        return -1
            