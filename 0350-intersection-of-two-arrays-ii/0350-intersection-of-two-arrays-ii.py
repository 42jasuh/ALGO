class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        nums1.sort()
        nums2.sort()

        length1 = len(nums1)
        length2 = len(nums2)

        i1 = 0
        i2 = 0

        while i1 < length1 and i2 < length2:
            print(f'i1: {i1}, i2: {i2}')
            if nums1[i1] == nums2[i2]:
                answer.append(nums1[i1])
                i1 += 1
                i2 += 1
            elif nums1[i1] > nums2[i2]:
                i2 += 1
            elif nums1[i1] < nums2[i2]:
                i1 += 1
        
        return answer