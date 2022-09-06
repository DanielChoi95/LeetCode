'''
Introduction to Array 
total 17
'''

# Find Pivot Index
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left=0
        if sum(nums[1:]) == 0:
            return 0     
        for i in range(len(nums)):
            try:
                left += nums[i]
                right = sum(nums[i+2:])
                if left == right and i+1 < len(nums):
                    return i+1
            except:
                return -1
        return -1

# Find Pivot Index (Better)
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        leftSum = 0
        rightSum = sum(nums)
        for i in range(0, len(nums)):
            rightSum -= nums[i]
            if (rightSum == leftSum):
                return i
            else:
                leftSum += nums[i]
        return -1

# Largest Number At Least Twice of Others
class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        max_num=max(nums)
        for i in range(len(nums)):
            if nums[i] == max_num:
                pass
            elif nums[i]*2 > max_num:
                return -1
        return nums.index(max_num)

# Plus One
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num1= ''.join(map(str,digits))
        num2= int(num1)+1
        return [int(i) for i in str(num2)]

''' @@@@@@ Introduction to 2D Array @@@@@@ '''

# Diagonal Traverse
class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        if mat == []: return []
        m,n = len(mat), len(mat[0])
        result = []
        number = m * n #전체 elem 수
        i = j = 0
        up = True
        while number:
            number -= 1 #break point
            result.append(mat[i][j])
            #up일때, i감소 j 증가
            if up:
                if j == n - 1: #최대 col 도달
                    i += 1
                    up = False
                elif i == 0: #up 마지막 단계[증가 시퀀스에서만]
                    j += 1
                    up = False
                else: #일반적일때
                    i -= 1
                    j += 1
            #down일때, i증가 j감소
            else:
                if i == m - 1: #최대 row 도달
                    up = True
                    j += 1
                elif j == 0: #down 마지막 단계[증가 시퀀스에서만]
                    i += 1
                    up = True
                else: #일반적일때
                    i += 1
                    j -= 1
        return result

# Spiral Matrix
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        max_row, max_col = len(matrix), len(matrix[0])
        min_row, min_col = 1,0
        m,n = 0,0
        direction = 1 # right(1) -> down(2) -> left(3) -> up(4)
        number=max_row*max_col
        if max_col == 1:
            for i in range(max_row):
                result.append(matrix[i][0])
            return result
        while number:
            number -= 1
            result.append(matrix[m][n])
            if direction == 1: #right
                n += 1
                if n == max_col-1:
                    direction = 2
                    max_col -= 1
            
            elif direction == 2: #down
                m += 1
                if m == max_row-1:
                    direction = 3
                    max_row -= 1
            
            elif direction == 3: #left
                n -= 1
                if n == min_col:
                    direction = 4
                    min_col += 1

            elif direction == 4: #up
                m -= 1
                if m == min_row:
                    direction = 1
                    min_row += 1
        return result

# Pascal's Triangle
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result=[[1],[1,1]] #어차피 고정
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return result
        for i in range(numRows-2):
            lst=[]
            lst.append(1) #왼쪽 끝
            for j in range(i+1): #중간
                lst.append(result[i+1][j]+result[i+1][j+1])
            lst.append(1) #오른쪽 끝
            result.append(lst)
        return result

# Pascal's Triangle (little bit Better)
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = [[1] * x for x in range(1, numRows +1)]
        for i in range(2, numRows):
            for j in range(1, i):
                triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

        return triangle

''' @@@@@@ Introduction to String @@@@@@'''

# Add Binary
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

# Implement strStr()
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1

# Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort(key=len)
        
        for i in range(len(strs[0])):
            letter = strs[0][i]
            for str in strs:
                if str[i] == letter:
                    pass
                else:
                    try:
                        return strs[0][:i]
                    except:
                        return ''
        return strs[0]

'''
@@@@@@ Two-Pointer Technique @@@@@@@
1. from start to middle
2. from end to middle
or
1. used for the iteration
2. always points at the position for next addition
The key to solving this kind of problems is to Determine the movement strategy for both pointers.
'''

# Reverse String ( s.reverse() )
class Solution:
    def reverseString(self, s: list[str]) -> None:
        cnt = 0
        while cnt < len(s)/2:
            s[cnt], s[-(cnt+1)] = s[-(cnt+1)], s[cnt]
            cnt += 1

# Array Partition I ( sum(sorted(nums)[::2]) )
class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        sum=0
        for i in range(len(nums)):
            if i%2 == 0:
                sum += nums[i]
        return sum

# Two Sum II - Input array is sorted
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        hash = list(set(numbers))
        hash.sort()
        for i in range(len(hash)):
            num2 = target - hash[i]
            if num2 in hash:
                index1 = numbers.index(hash[i]) + 1
                index2 = numbers.index(num2, index1) + 1
                return [index1, index2]

# Two Sum II - Input array is sorted (Better)
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        ans=[]
        i=0
        j=len(numbers)-1
        while i<j:
            check=numbers[i]+numbers[j]
            if check>target:
                j=j-1
            elif check<target:
                i=i+1
            else:
                ans.append(i+1)
                ans.append(j+1)
                break
        return ans

# Minimum Size Subarray Sum (Failed : Time Limit Exceeded)
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if sum(nums) < target:
            return 0
        
        min_len = len(nums)
        idx_start = 0
        while idx_start < len(nums):
            for i in range(idx_start, len(nums)+1):
                #제한 길이 초과 시 파괴
                if len(nums[idx_start:i]) > min_len:
                    break
                #최소값 갱신 시
                if sum(nums[idx_start:i]) >= target and min_len > len(nums[idx_start:i]):
                    min_len = len(nums[idx_start:i])
                    break
            idx_start += 1 #스타트포인트 갱신
        return min_len

# Minimum Size Subaray Sum (Need to Study)
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        start = 0
        end = 0
        sum = nums[0]
        min = len(nums)
        found = False

        if len(nums) == 0: return 0


    # left를 기준으로 판단한다. 

        while start <= end and end < len(nums):
            if sum < target:
                end += 1
                if end < len(nums):
                    sum += nums[end]
            elif sum >= target:
                if min >= (end - start + 1):
                    min = end - start + 1
                    found = True
                if sum > target:
                    
                    sum -= nums[(start)]
                    start += 1
                    
                else:
                    end += 1
                    if end < len(nums):
                        sum += nums[end]
        if found==True:
            return min
        return 0

'''
@@@@@@ Conclusion : Array-related Techniques @@@@@@
'''

# Rotate Array (Not Efficient)
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        #맨 뒤를 맨앞으로 가져오는걸 k번 반복 한다
        if k > len(nums):
            k = k % len(nums)
        for _ in range(k):
            elem = nums.pop()
            nums.reverse()
            nums.append(elem)
            nums.reverse()

# Rotate Array (Failed: Time Limit Exceeded)
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        #맨 뒤를 맨앞으로 가져오는걸 k번 반복 한다
        if k > len(nums):
            k = k % len(nums)
        while k:
            num = nums[-1]
            for i in range(len(nums)-1, 0, -1):
                nums[i] = nums[i-1]
            nums[0] = num
            k -= 1
        return nums

# Rotate Array (Best)
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k %= len(nums)
        nums[k:], nums[:k] = nums[:-k], nums[-k:]

# Pascal's Triangle II
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        result=[[1],[1,1]] #어차피 고정
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return result[1]
        for i in range(rowIndex-1):
            lst=[]
            lst.append(1) #왼쪽 끝
            for j in range(i+1): #중간
                lst.append(result[i+1][j]+result[i+1][j+1])
            lst.append(1) #오른쪽 끝
            result.append(lst)
        return result[rowIndex]

# Reverse Words in a String
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))

# Reverse Words in a String III
class Solution:
    def reverseWords(self, s: str) -> str:
        list_word = s.split()
        
        for idx_word in range(len(list_word)):
            list_letter=[]
            for idx_letter in range(len(list_word[idx_word])):              
                list_letter.append(list_word[idx_word][idx_letter])
            list_letter.reverse()
            word = ''.join(list_letter)
            list_word[idx_word] = word
        return ' '.join(list_word)

# Reverse Words in a String III (Better)
class Solution:
    def reverseWords(self, s: str) -> str:
        ans = s.split()
        for i in range(len(ans)):
            ans[i] = ans[i][::-1]
        ans = ' '.join(ans)
        return ans