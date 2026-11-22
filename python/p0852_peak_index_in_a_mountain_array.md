# 852. Peak Index in a Mountain Array · Python

[原题](https://leetcode.com/problems/peak-index-in-a-mountain-array/)。

原题arr为严格山峰数组：长度3..100000，值0..10^6，有唯一内部峰，两侧分别严格递增与严格递减。实现只支持保证的严格山峰，不把平台或单调数组当合法样本；返回峰下标int，输入保持。

[left,right]包含峰。left<right时mid<right，所以读取mid+1不会越界。若arr[mid]<arr[mid+1]，mid处仍在上升侧，峰严格在右，令left=mid+1；否则mid在峰或下降侧，峰不在mid右侧，令right=mid。每次区间长度至少约减半，收敛下标就是唯一峰。时间O(log n)，额外空间O(1)。

独立参考扫描max再找下标。峰值取1..5，左右坡分别由0..peak-1的非空子集按升序和降序构造，共1245个严格山峰，不要求两坡数值互异。另测长度100000、峰在1/50000/99998三处及值域上限，测试显式检查输入满足山峰合同、返回int及输入保持。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
