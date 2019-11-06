'''
给定一个只包含整数的有序数组，每个元素都会出现两次，唯有一个数只会出现一次，找出这个数。

示例 1:

输入: [1,1,2,3,3,4,4,8,8]
输出: 2
示例 2:

输入: [3,3,7,7,10,11,11]
输出: 10
注意: 您的方案应该在 O(log n)时间复杂度和 O(1)空间复杂度中运行。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-element-in-a-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def singleNonDuplicate(self, nums) -> int:
            out = None
            # 数组只会有1,>=3的长度的情况
            # 小于3的, 若长度唯一肯定就是那个, 长度为2则不存在单一数
            if len(nums) < 3:
                    return nums[0]
            # 长度 >= 3 的, 先看首尾, 第一个不等于第二个,则取第一个, 倒一不等于倒二, 则取倒一
            if nums[0] != nums[1]:
                    return nums[0]
            elif nums[-1] != nums[-2]:
                    return nums[-1]
            else:
                    # 当单一数在位置 [1,2,3,...,n-1]中时, 重复地3个3个看, 若i!=i+1!=i+2, 则单一数为i+1
                    for i in range(1, len(nums)-1):
                            if nums[i] != nums[i+1] and nums[i+1] != nums[i+2]:
                                    out = nums[i+1]

                    return out

if __name__ == '__main__':
    nums = [3,3,7,7,10,11,11]
    sol = Solution()
    print(sol.singleNonDuplicate(nums))












