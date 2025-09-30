class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        writeIndex = 1
        duplicateCount = 0
        prevElement = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != prevElement:
                duplicateCount = 0
            else:
                duplicateCount += 1

            if duplicateCount <= 1:
                nums[writeIndex] = nums[i]
                writeIndex += 1
                prevElement = nums[i]

        return writeIndex