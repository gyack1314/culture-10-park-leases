# 文化园区租赁组合风险与专款流动性安排

本项目保存本地合成业务资料、输入约定和资料完整性检查。记录不对应真实个人、企业、场馆或合同；原始数据不带分析结论。

## 环境与现有入口

使用 Python 3.11。安装固定依赖：

```sh
python -m pip install -r requirements.txt
python tools/inspect_inputs.py
python -m pytest -q
```

现有入口仅检查本地资料的校验和、字段和主键，不计算业务结果。业务含义见 [业务约定](docs/业务约定.md)，文件与字段见 [资料目录](docs/资料目录.md)。data 中各表使用 UTF-8 JSON Lines，catalog.json 记载行数、主键和校验和。已有检查不需要网络和账号。
