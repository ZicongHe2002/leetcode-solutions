# 1103. Distribute Candies to People · Python

[原题](https://leetcode.com/problems/distribute-candies-to-people/)。

num_people为正，每份期望数量从1递增。第gift份的接收人下标为(gift-1)%num_people，实际发放min(gift,剩余糖果)，保证最后不足一份时也准确分配，所有糖果恰好发完。每次循环按题意完成一份发放，累计发放前t份需约t(t+1)/2颗，因此份数只为平方根量级。

初始糖果数C、人数P，时间O(P+sqrt(C))，输出空间O(P)，除输出外额外空间O(1)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
