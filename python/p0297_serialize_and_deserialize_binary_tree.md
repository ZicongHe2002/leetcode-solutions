# 297. Serialize and Deserialize Binary Tree · Python

[原题](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)。

实现Codec.serialize与Codec.deserialize，在字符串和二叉树之间往返。每个节点有val/left/right字段，值可重复且包含0和负数；原题至多10000节点。返回的新树必须保留数值、左右方向和空子树位置，不依赖原树对象或同一个Codec实例。TreeNode定义与仓库相邻树题保持一致。

协议为逗号分隔的先序token：整数表示节点，#表示空孩子，空树的完整编码就是#。每个非空节点后都编码左右两个孩子，因此n个节点共有2n+1个token。若只保存节点值而省略空标记，单个左孩子与单个右孩子的树会产生同样值序列，无法唯一恢复。

serialize用显式栈，先压右孩子再压左孩子，使弹出顺序为根、左、右。deserialize维护尚待填写孩子的(parent,side)栈：side=0时填写左孩子并将父节点标为待右；side=1时填写右孩子并移除已填满的父节点。非空新孩子再成为下一待填节点。每个token恰好填一个先序空位，所以还原结构唯一。

两端都不递归，深链不依赖Python递归上限。按原题有界节点值计，时间O(n)；序列化片段、反序列化split得到的token列表均为O(n)，另有O(d)显式栈，d为树高，返回节点本身也占O(n)。不能因为控制栈只有O(d)就把整个解码辅助空间写成O(d)。deserialize的合同输入是本协议生成的合法数据，这里没有增加通用损坏数据校验器。

测试用独立层序遍历的带空位签名核对结构，不复用生产先序空位栈；同时检查序列化不改原树、解码节点与原树身份不重用、不同Codec实例可解码。0..5节点全部二叉树形与三值域全部标号共11497棵，另测10000节点左右深链、重复/负/零值及固定协议文本。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
