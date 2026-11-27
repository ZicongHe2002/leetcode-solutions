# 154. Find Minimum in Rotated Sorted Array II · Python

[原题](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)。

原题长度1..5000，值在-5000..5000，非递减数组旋转1..n次，可有重复值。旋转n次等同未旋转，仍属合法输入；空数组不在合同内。返回最小值int，输入保持。

闭区间[left,right]保留至少一个全局最小值。若nums[mid]>nums[right]，从mid到right之间跨过了下降断点，最小值在mid右侧；若nums[mid]<nums[right]，mid到right有序，最小值可以在mid，保留[left,mid]。相等时无法判断断点方向，但被删的right值在mid仍有一份，所以只把right减一不会删掉所有最小值。区间严格缩小，收敛到的元素就是最小值。重复值可能让每次只缩一个元素，例如全相等数组，最坏时间O(n)，不能宣称保证O(log n)；额外空间O(1)。

独立参考直接用min扫描。枚举值-1/0/1、长度1..8的164个有序多重集合，再枚举每个旋转位置，共990次查询。长度5000分别覆盖全相等、一处极小值、两端值域与未旋转；核对返回类型与输入保持。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
