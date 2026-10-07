1. 读取原始行为日志
2. 按 user/session 和时间排序
3. 清洗数据、转换字段
4. 按时间划分 train / valid / test
5. 用 train 构造统计特征和共现矩阵
6. 对 valid/test 的每个用户或 session 生成候选集
7. 用未来行为构造 label
8. 合并 item 特征、user/session 特征、交叉特征
9. 训练排序模型
10. 对候选集 predict 打分
11. 每个用户/session 按分数排序取 TopK
12. 用 Recall@K / NDCG@K / MAP@K 评估
13. 生成最终推荐结果

- 第一，数据层面：                    

原始数据是 session 级电商行为日志，每条记录包含 session、商品 aid、时间戳 ts 和行为类型 type。我先统一时间戳和行为编码，并在资源限制下抽取部分 parquet 文件复现完整流程。

- 第二，召回层面：                     

我构建了三类 item-to-item co-visitation matrix：clicks 用于点击兴趣召回，carts_orders 用于加购/购买召回，buy2buy 用于强化购买关联。构造时通过 session 内 self-merge 生成商品对，并结合时间窗口、行为权重和商品 ID 分片控制规模。

- 第三，候选生成：                       

对每个 session，我结合最近历史商品、共现矩阵召回商品和全局热门商品兜底，为 clicks、carts、orders 分别生成候选列表，先生成 Top100，再截断为 Top50 控制后续训练规模。

- 第四，特征工程：        

我构造了 item、session、session-aid 三类特征。item 特征描述商品热度和转化能力，session 特征描述用户当前行为强度，session-aid 特征描述某个商品和当前 session 的交互关系。

- 第五，排序模型：       

我把推荐问题转化为 session-aid 粒度的排序学习任务，使用 XGBoost rank:pairwise 训练三类目标模型。训练时按 session 设置 group，并用 GroupKFold 保证同一个 session 不会同时出现在训练和验证折中。

- 第六，评估：              

最终对每个 session 输出 Top20 商品，分别计算 clicks、carts、orders 的 Recall@20，并按 OTTO 权重计算加权总分。

这份代码最核心的 5 个面试点

你一定要背熟这 5 个：

- self-merge 生成共现商品对                     
同一个 session 内商品两两配对，统计 item-to-item 关系。
- 三类共现矩阵服务不同目标                     
clicks 偏兴趣，carts_orders 偏转化，buy2buy 偏购买。
- 候选生成不是模型预测      
候选生成是召回阶段，目的是缩小商品空间。
- 排序样本是 session-aid 粒度              
每一行代表“某个 session 下的某个候选商品”。
- XGBoost rank:pairwise 要设置 group            
一个 session 是一个排序组，模型学习组内正样本排在负样本前面。