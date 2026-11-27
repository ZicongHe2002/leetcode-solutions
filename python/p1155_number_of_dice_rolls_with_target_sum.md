# 1155. Number of Dice Rolls With Target Sum · Python

[原题](https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/)。

骰子有序，每个骰子可取1..k。previous[s]为已处理骰子得到和s的方案数，加入一个骰子时current[s]为previous[s-1]至previous[s-k]之和。相邻s的求和区间仅移动一位，用滑动和加入新右端并减去过期左端，把每态枚举k面降为常数更新。初始0个骰子仅和0有一种方案，所有结果取模10^9+7。

时间O(n*target)，额外空间O(target)，不使用浮点运算。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
