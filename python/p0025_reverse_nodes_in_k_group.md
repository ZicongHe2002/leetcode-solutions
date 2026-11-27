# 25. Reverse Nodes in k-Group · Python

[原题](https://leetcode.com/problems/reverse-nodes-in-k-group/)。

原题链长n，1<=k<=n<=5000，节点值0..1000；每个完整k节点组反转，最后不足k个节点保持顺序，只改next不能改val。假设无环，返回新的头。本文件ListNode用于本地导入，与评测器val/next一致。

before始终是下一个候选组的前驱。先向后探测k次找到end；若提前遇到None，未修改该候选组，直接返回，保留不足一组的尾链。完整组的后继after先保存，再从after作为反转初始previous，把当前组的每个next逐个反向。循环在current到达after时结束，组内已反转且旧组头连向after。before.next接到旧组尾end，before移动到旧组头first，为下一组恢复不变量。

每个完整组探测和反转各k步，末组最多探测k步，合计O(n)时间；只使用固定指针与一个哨兵，额外空间O(1)，不递归、不保存节点数组。测试参考按原节点数组对完整切片逆序，逐个比较对象身份，最后断言None，同时核对所有val不变。值0/1、长度1..7的254条链，遍历全部合法k共1538次；另测5000节点、多种整除及非整除组长和值域上限。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
