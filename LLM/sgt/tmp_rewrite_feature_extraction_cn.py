import json
from pathlib import Path


path = Path(r"F:\csnotes\LLM\sgt\otto\3. Feature Extraction.ipynb")
nb = json.loads(path.read_text(encoding="utf-8"))


def comment_for(line: str) -> str:
    s = line.strip()
    if not s:
        return line
    if s.startswith("#"):
        return "# \u6ce8\u91ca\n"
    if s.startswith("VER ="):
        return "# \u811a\u672c\u7248\u672c\n"
    if s.startswith("import pandas as pd, numpy as np"):
        return "# \u5bfc\u5165 pandas \u548c numpy\n"
    if s.startswith("from tqdm.notebook import tqdm"):
        return "# \u5bfc\u5165 Jupyter \u8fdb\u5ea6\u6761\n"
    if s == "tqdm.pandas()":
        return "# \u4e3a pandas \u542f\u7528\u8fdb\u5ea6\u6761\n"
    if s.startswith("import os, sys, pickle, glob, gc"):
        return "# \u5bfc\u5165\u5e38\u7528\u6807\u51c6\u5e93\n"
    if s.startswith("from collections import Counter"):
        return "# \u5bfc\u5165 Counter \u5de5\u5177\n"
    if s.startswith("import cudf, itertools"):
        return "# \u5bfc\u5165 RAPIDS \u548c\u8fed\u4ee3\u5de5\u5177\n"
    if s.startswith("print("):
        return "# \u6253\u5370\u4fe1\u606f\n"
    if s.startswith("pd.set_option("):
        return "# \u8bbe\u7f6e pandas \u663e\u793a\u9009\u9879\n"
    if s.startswith("from pandarallel import pandarallel"):
        return "# \u5bfc\u5165\u5e76\u884c\u5904\u7406\u5de5\u5177\n"
    if s.startswith("pandarallel.initialize("):
        return "# \u521d\u59cb\u5316\u5e76\u884c\u73af\u5883\n"
    if s.startswith("import polars as pl"):
        return "# \u5bfc\u5165 polars\n"
    if s.startswith("from pyarrow.parquet import ParquetFile"):
        return "# \u5bfc\u5165 ParquetFile\n"
    if s.startswith("import pyarrow as pa"):
        return "# \u5bfc\u5165 pyarrow\n"
    if s.startswith("def "):
        return "# \u5b9a\u4e49\u51fd\u6570\n"
    if s.startswith("GENERATE_FOR ="):
        return "# \u6307\u5b9a\u751f\u6210\u6a21\u5f0f\n"
    if s.startswith("CANDIDATE_COUNT ="):
        return "# \u8bbe\u7f6e\u5019\u9009\u6570\u91cf\n"
    if s.startswith("type_labels ="):
        return "# \u5b9a\u4e49\u884c\u4e3a\u7c7b\u578b\u6620\u5c04\n"
    if s.startswith("if GENERATE_FOR == \"local\":"):
        return "# \u672c\u5730\u6a21\u5f0f\u7684\u6570\u636e\u8def\u5f84\n"
    if s.startswith("elif GENERATE_FOR == \"kaggle\":"):
        return "# Kaggle \u6a21\u5f0f\u7684\u6570\u636e\u8def\u5f84\n"
    if "read_parquet" in s:
        return "# \u8bfb\u53d6\u6570\u636e\u6587\u4ef6\n"
    if s.startswith("for "):
        return "# \u904d\u5386\u6570\u636e\n"
    if s.startswith("return "):
        return "# \u8fd4\u56de\u7ed3\u679c\n"
    if s.startswith("del "):
        return "# \u6e05\u7406\u4e34\u65f6\u53d8\u91cf\n"
    if s.startswith("item_features = pd.concat(") or s.startswith("user_features = pd.concat(") or s.startswith("user_item_int_features = pd.concat("):
        return "# \u62fc\u63a5\u7279\u5f81\u8868\n"
    if s.startswith("aid_count_df = item_df[item_df.type==0]"):
        return "# \u7edf\u8ba1\u5546\u54c1\u51fa\u73b0\u6b21\u6570\n"
    if s.startswith("co_"):
        return "# \u8bfb\u53d6\u5171\u73b0\u77e9\u9635\n"
    if s.startswith("ppmi_target_combs ="):
        return "# \u51c6\u5907 PPMI \u7ec4\u5408\n"
    if s.startswith("score_df_tuples_w_names ="):
        return "# \u7ec4\u88c5\u7279\u5f81\u8f93\u5165\n"
    if s.startswith("generate_candidate_history_pair_score_features("):
        return "# \u751f\u6210\u5019\u9009\u5386\u53f2\u7279\u5f81\n"
    if s.startswith("def generate_datetime_features"):
        return "# \u751f\u6210\u65f6\u95f4\u7279\u5f81\n"
    if s.startswith("input_df[\"datetime\"] ="):
        return "# \u751f\u6210 datetime \u5217\n"
    if s.startswith("input_df[\"hour\"] ="):
        return "# \u63d0\u53d6\u5c0f\u65f6\n"
    if s.startswith("input_df[\"dayofweek\"] ="):
        return "# \u63d0\u53d6\u661f\u671f\n"
    if s.startswith("input_df[\"is_weekend\"] ="):
        return "# \u6807\u8bb0\u5468\u672b\n"
    if s.startswith("aid_count_df.fillna"):
        return "# \u7f3a\u5931\u503c\u586b\u5145\n"
    if ".to_parquet" in s:
        return "# \u4fdd\u5b58 parquet \u7ed3\u679c\n"
    if s.startswith("item_df = pd.concat([train_df,val_df"):
        return "# \u5408\u5e76\u8bad\u7ec3\u96c6\u548c\u9a8c\u8bc1\u96c6\n"
    if s.startswith("user_df = val_df"):
        return "# \u7528\u9a8c\u8bc1\u96c6\u4f5c\u4e3a\u7528\u6237\u7279\u5f81\u8f93\u5165\n"
    if s.startswith("user_item_int_df = val_df"):
        return "# \u7528\u9a8c\u8bc1\u96c6\u4f5c\u4e3a\u4ea4\u4e92\u7279\u5f81\u8f93\u5165\n"
    return "# \u5904\u7406\u8be5\u884c\u4ee3\u7801\n"


for cell in nb.get("cells", []):
    if cell.get("cell_type") != "code":
        continue
    new_source = []
    for line in cell.get("source", []):
        if line.strip() and not line.lstrip().startswith("#"):
            new_source.append(comment_for(line))
        new_source.append(line)
    cell["source"] = new_source

path.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
