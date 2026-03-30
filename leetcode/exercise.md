
# 补充
1. 列表推导式：       
   ```python
    [表达式 for 变量 in 可迭代对象]
    [表达式 for 变量 in 可迭代对象 if 条件]
    [表达式1 if 条件 else 表达式2 for 变量 in 可迭代对象]
    [表达式 for 变量1 in ... for 变量2 in ...]
   ```

# 1 
## 自己尝试的，错误百出。
- list.index()只会返回第一个出现的索引
- 注意是找到break还是没找到break，否则可能找到了还在循环
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for num in nums:
            obj = []
            # index只会返回第一个出现的索引
            i = nums.index(num)
            val = target - num
            if (val in nums):
                j = nums.index(val)
                if i != j :
                    obj = sorted([i, j])
                #如果列表设置为空在循环内部，不能continue
                #且else后break并不能退出for循环，需要放在内层if即找到结果的后一句
                    break 
        #obj不一定被赋值
        return obj 
```
## 列表循环，ai改
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```
## 评论区解决遍历时间
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            obj = []
            # index只会返回第一个出现的索引
            val = target - nums[i]
            if val in nums[i+1:]:
                return [i, nums[i+1:].index(val)+i+1]
```