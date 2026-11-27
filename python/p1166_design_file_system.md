# 1166. Design File System · Python

[原题](https://leetcode.com/problems/design-file-system/)。

接口为FileSystem。题目路径格式合法、非空且非根路径，value为正数，不涉及删除或改名。用空字符串哨兵表示顶层父目录：/a的父键为空，/a/b的父键是/a。createPath只有在当前路径尚未存在且直接父路径已存在时成功，不自动创建缺失祖先。路径不存在时get返回-1，重复创建不得覆盖旧值。

单次操作按路径长L计期望O(L)，总空间为所存路径文本长度之和。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
