''' total 15'''
# Max Consecutive Ones
class Solution:
    def findMaxConsecutiveOnes(self, nums=[]):
        self.nums=nums
        max_count=0
        curr_count=0
        for i in range(0, len(self.nums)):
            if self.nums[i] == 1:
                curr_count += 1
                if curr_count > max_count:
                    max_count=curr_count
            else:
                if curr_count > max_count:
                    max_count=curr_count
                curr_count=0
        return max_count

# Find Numbers with Even Number of digits
class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        cnt=0
        for n in nums:
            if len(str(n))%2 == 0:
                cnt +=1
        return cnt

# Squares of a Sorted Array
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        result= []
        for n in nums:
            result.append(n**2)
        result.sort()
        return result
'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([x*x for x in nums])
'''

# Duplicate Zeros
class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i=0
        while i < len(arr)-1:
            if arr[i] == 0:
                j = len(arr)-1
                #한칸씩옮기기
                while(j>i):
                    arr[j]=arr[j-1]
                    j -= 1
                i += 1
            #복사한 0 뛰어넘기
            i += 1

# Merge Sorted Array
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:n]
        nums1.sort()

# Remove Element
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        k=len(nums)
        return k

# Remove Duplicates from Sorted array
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i=0
        while i < len(nums) and len(nums) > 1:
            if nums[i-1] == nums[i]:
                nums.remove(nums[i-1])
            else:
                i += 1
        k= len(nums)
        return k
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i] 
                k += 1
        return k
'''

# Check If N and its Double Exist
class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        seen = set()
        for n in arr:
            if n / 2 in seen or n * 2 in seen:
                return True
            seen.add(n)
        return False

# Valid Mountain Array
class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        top=max(arr) 
        i=0
        if len(arr) < 3 or arr[0] == top:
            return False
        while arr[i] < top: 
            if arr[i] == arr[i+1]: 
                return False
            elif arr[i] > arr[i+1]: 
                return False
            elif arr[i] < arr[i+1]: 
                i=i+1
        if arr[i] == top: 
            if i == len(arr)-1:
                return False
            if arr[i] == arr[i+1]:
                return False
            i=i+1
        while i > arr.index(top): 
            if i == len(arr):
                return True
            if arr[i-1] == arr[i]: 
                return False
            elif arr[i-1] < arr[i]: 
                return False
            elif arr[i-1] > arr[i]:
                i=i+1
# Valid Mountain Array (Better Answer)
class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        left = 0
        if len(arr) <= 2:
            return False
        for i in range(1, len(arr)):
            if arr[i-1] < arr[i]:
                left = i
            elif arr[i-1] == arr[i]:
                return False
            else:
                break
        print(left)
        right = len(arr) - 1
        for i in range(len(arr) - 1, 0, -1):
            if arr[i-1] > arr[i]:
                right = i - 1
            elif arr[i-1] == arr[i]:
                return False
            else:
                break
        print(right)
        if right == len(arr)-1 or left == 0:
            return False
        return left == right
    
# Replace Elements with Greatest Element on Right side
class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        for i in range(0, len(arr)-1):
            maximum=max(arr[i+1:])          
            arr[i]=maximum
        arr[-1] = -1
        return arr

'''
two-pointer technique is one of the main techniques used for in-place array algorithms.
'''

# Move Zeroes
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        insert_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_index]=nums[i]
                insert_index+=1
        for i in range(insert_index,len(nums)):
            nums[i]=0

# Move Zeroes (better)
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j=0
        for i in nums:
            if i!=0:
                nums[j]=i
                j+=1
        for k in range(j,len(nums)):
            nums[k]=0

# Sort Array by Parity (need to figure out)
class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        write = 0
        read = 0
        while read < len(nums):
            if nums[read]%2 == 0:
                nums[write], nums[read] = nums[read], nums[write]
                write += 1
            read += 1
        return nums

# Height Checker
class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        n = 0
        expected = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                n += 1
        return n

# Third Maximum Number
class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        i=0
        nums.sort()
        while i < len(nums) and len(nums) > 1:
            if nums[i-1] == nums[i]:
                nums.remove(nums[i-1])
            else:
                i += 1
        nums.sort(reverse=True)
        first = nums[0]
        try:
            second = nums[1]
        except:
            second = None
        try:
            third = nums[2]
        except:
            third = None
        if third == None or second == None:
            return first
        return third

# Third Maximum Number (Faster)
class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        hash = sorted(set(nums)) #set -> erase duplicates
        if len(hash) >= 3:
            return hash[-3]
        else:
            return max(hash)

# Find All Numbers Disappeared in an Array
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result=[]
        hash = set(nums)
        for i in range(1,n+1):
            if i not in hash:
                result.append(i)
        return result