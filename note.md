<center>概念学习</center>  

概念学习：从样例中逼近布尔值函数，推断出目标布尔函数

归纳学习假设：训练样本集中很好逼近目标函数->也能在未见实例中很好的逼近目标函数



假设的一般到特殊序：

​	$h_{j} \geq h_{k} $($h_j$ 比$h_k$更一般)：$(\forall x \in X)[(h_k(x) = 1) \dashrightarrow (h_j(x) = 1)]$

 - FIND-S:

   1、初始化假设$h$为$H$中最特殊的假设

   2、对每个正例$x$：

   ​	将$h$中每个约束属性$a_i$改成能够满足该正例的更一般的约束（满足的不变，不满足的添加）

   3、输出假设

   - 噪声、是否收敛？多个极大假设（输出的其中一个）？

- 变型空间和候选消除算法

  候选消除算法：输出的是与训练样例一致的所有假设的集合

  def:		一个假设$h$与训练样例一致，即对每个训练样例，该假设都能正确分类。

  def:		变型空间（$VS_{H,D} == {h \in H | Consistent(h, D)}$）

  候选消除：

  ​	初始化一个极大一般假设集合G、一个极大特殊假设集合S

  ​	对每个样例：

  ​		正样例：

  ​			从G中移除不满足的假设

  ​			对S中不满足的假设，移除，并添加其所有的极小泛化假设到S（与训练样例一致，比G中某个假			设更一般）

  ​			移除S中比另一个S中假设更一般的假设			

  ​		负样例：

  ​			从S中移除不满足的假设

  ​			对G中不满足的假设，移除，并添加其所有极小特殊假设到S（与训练样例一致，比S中某个假设更特殊）

  ​			移除G中比另一个G中假设更特殊的假设









<center>决策树</center>

熵：$Entropy(S) =  - \sum_{i} p_ilog_2p_i$,   其中$p_i$是该样例集中类别$i$的频率

信息增益：某个属性$A$相对于集合$S$的信息增益：

​	$Gain(S, A) = Entorpy(S)  - \sum_v \frac{\vert S_v \vert}{\vert S \vert} Entropy(S_v)$, 其中$S_v$是属性$A$为$v$的集合。

每次分裂的时候选择信息增益最大的属性

奥坎姆剃刀：优先选择拟合数据的最简单的假设

避免过度拟合：

​	0、及早停止树增长

​	1、错误率降低修剪：选择可以提高（验证集）的最大结点（成为叶结点）

​	2、规则后剪枝

合并连续值属性：取中间（lable变的两个值）







<center>人工神经网络</center>

感知器：一个实数值向量输入，输出1/-1:

$o(x_1,...x_n) = 1.  if (w_0 + w_1x_1 + ... + w_nx_n > 0).  Else: -1 $

​	感知器训练法则（数据需线性可分）：

​		$w_i = w_i + \vartriangle w_i = w_i + \eta(t-o)x_i,   (\eta>0,t(目标)，o(实际输出))$

​	梯度下降和delta法则：

​		训练误差：$E = \frac{1}{2} \sum_{d \in D} (t_d - o_d)^2$

​		梯度最大的负方向：$\vartriangle w_i = - \eta \frac{\partial E}{\partial w_i} = -\eta \sum_{d \in D}(t_d - o_d)(- x_{id})$

​		随机梯度下降：每个样例就更新：$\vartriangle w_i = \eta(t - o)x_i$

​	$o$的定义不一样，感知器是感知器输出，1/-1；梯度下降时线性单元输出。		

线性单元：对应感知器，不加阈值，即$o(\vec x) = \vec w . \vec x$,

sigmoid单元：

​	可微阈值函数：

​	sigmoid:$\sigma(y) = \frac{1}{1 + e^{-y}}, 	(y = \sum_{i=0}^{n} w_ix_i)$

​	反向传播算法：

​		输出单元：$\delta_k = o_k(1-o_k)(t_k-o_k)$

​		隐藏单元：$\delta_h = o_h(1-o_h)\sum_{s \in Downstream(h)}w_{sh}\delta_s$

​		更新：$w_{ji} = w_{ji} + \vartriangle_{ji} = w_{ji} + \eta \delta_jx_{ji}$ 







<center>贝叶斯学习</center>

贝叶斯公式：$P(h\vert D) = \frac{P(D \vert h)P(h)}{P(D)}$

极大后验假设：$h_{MAP} = arg_{h\in H}maxP(h \vert D) = arg_{h \in H}maxP(D \vert h)P(h)$

极大似然假设（假设每个假设有相同的先验概率）：$h_{ML} = arg_{h \in H}maxP(D \vert h)$

最小描述长度：$h_{MDL} = arg_{h \in H}minL_{C_{1}}(h) + L_{C_2}(D \vert h)$



贝叶斯最优分类器：多个假设，每个假设的后验概率。加权

GIBBS算法：按照后验概率的分布，随机选取一个假设，预测新的样例

朴素贝叶斯：独立性假设。











