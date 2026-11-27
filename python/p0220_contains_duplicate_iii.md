# 220. Contains Duplicate III · Python

[原题](https://leetcode.com/problems/contains-duplicate-iii/)。

给定整数列表、正整数indexDiff及非负整数valueDiff，判断是否存在i!=j，同时满足abs(i-j)<=indexDiff和abs(nums[i]-nums[j])<=valueDiff。输入不变；额外将非正indexDiff或负valueDiff定义为False，也支持空列表。

桶宽取valueDiff+1，整数x属于x//width号桶。Python的//向负无穷取整，因此负值也被划入相邻且不重叠的等宽区间。相同桶内两个整数最多相差width-1=valueDiff；相差至少两个桶的值至少相差width+1，所以只需检查同桶和左右邻桶。邻桶不能仅看是否存在，还必须检查实际差值。

扫描right之前，字典保存前indexDiff个下标以内的值。成功加入当前值之前若同桶已有值就返回True，因此继续扫描时每个桶至多一个值。先比较再删除right-indexDiff，保证恰好达到距离上界的配对不会被提前排除。删除时该桶确实属于过期值：若它与当前值同桶，比较阶段就已经返回，不会到达插入和删除阶段。

哈希字典按期望O(1)操作计，时间O(n)，额外空间O(min(n,indexDiff+1))，加一包含插入后尚未删除的瞬间。valueDiff=0时桶宽为1，算法自然退化为精确数值重复判断。Python整数计算不受32位减法溢出影响；不将负数除法改成截断到零。

独立oracle枚举全部i<j的下标对，直接计算两个绝对差，不使用分桶。穷举五值域长度0..5的3906个数组、0..n+1下标距离与0..3数值距离。另测负桶边界、valueDiff=0、过期后同值再次出现、极端正负值、100000项单调序列及输入保持；非正距离扩展另有明确检查。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
