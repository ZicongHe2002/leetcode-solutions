# 968. Binary Tree Cameras · Python

[原题](https://leetcode.com/problems/binary-tree-cameras/)。

后序三态为0未覆盖、1有摄像头、2已覆盖无摄像头，空孩子视为已覆盖。任一孩子未覆盖时，当前节点放摄像头，能同时覆盖自己、孩子与父方向，比把摄像头放在那个孩子更能向上覆盖；否则有孩子摄像头则当前被覆盖；两孩子都已覆盖但没摄像头时当前留待父亲处理。根没有父亲，若最终未覆盖再补一个。显式后序栈先求孩子状态，原树不修改。

时间O(n)，状态表与显式栈额外空间O(n)，不依赖长链递归深度。TreeNode由LeetCode提供。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
