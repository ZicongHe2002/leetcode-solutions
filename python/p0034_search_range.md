# 34. Find First and Last Position of Element in Sorted Array · Python

[原题](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)。

非递减数组长度0..100000，值与target在[-10^9,10^9]，返回target首尾下标或[-1,-1]。第一次半开区间二分找首个不小于target的位置first，允许哨兵n。first=n或该项不等于target就返回缺失，短路判断避免访问nums[n]。目标存在时，从first到n再找首个严格大于target的位置，减1得到末下标。

第一次搜索已排除前缀都小于target、已排除后缀都不小于target；边界答案始终在闭区间[left,right]。第二次把比较改为<=，使边界前缀允许等于目标。两个更新都严格缩小候选；第二个上边界必大于已知命中first，减1合法。没有计算target+1，也不从任意命中处线性扩展。时间O(log n)，空输入常数时间，额外空间O(1)，输入保持。

独立oracle逐项记录所有匹配下标。五值集合上长度0..8全部1287个非递减数组，各查七个target共9009次。另有固定重复段、空输入、值域端点；100000长度检查覆盖全相等、全缺失及重复10次的首段、中段和尾段。

A使用OpenAI Codex辅助编写；测试范围和实际结果见PR与日志，未向LeetCode提交。完整初稿可由B正式review后按最终head普通merge，共同补写为可选，仅按真实内容署名。
