# 大学信息填写 + PPT 替换 Skill

[English](README.md) | [简体中文](README.zh-CN.md)

这是一个面向 Codex / ChatGPT 的专用 Skill，用于以下固定工作流：

- 根据大学名称、学校邮箱或邮箱域名识别学校；
- 核验学校官方英文名、主要校区地址和邮编；
- 按指定格式输出表单字段和校区经纬度；
- 随机生成符合中文姓名习惯的拼音姓名和数字学号；
- 在内置 PPT 模板中只替换 `{{name}}`、`{{student_id}}`、`{{school_name}}` 三类占位符；
- 尽可能保持 PPT 原始版式、字体、字号、位置、行距、颜色和演示/无效标记不变。

## 仓库结构

- `SKILL.md`：Agent 的正式执行规则和硬性约束，是唯一操作规则源。
- `assets/certificate_template.pptx`：当前确认使用的 PPT 模板。
- `scripts/fill_certificate.py`：尽量保守地替换 PPTX 占位符。
- `scripts/inspect_template.py`：检查模板占位符和结构。
- `scripts/random_identity.py`：随机生成中文拼音姓名和学号。
- `data/names.json`：随机姓名数据源。
- `docs/OUTPUT_SCHEMA.md`：英文输出字段规范。
- `docs/OUTPUT_SCHEMA.zh-CN.md`：中文输出字段规范。
- `docs/PPT_RULES.md`：英文 PPT 格式规则。
- `docs/PPT_RULES.zh-CN.md`：中文 PPT 格式规则。
- `docs/RESEARCH_POLICY.md`：英文学校信息核验规则。
- `docs/RESEARCH_POLICY.zh-CN.md`：中文学校信息核验规则。
- `docs/MAINTAINER_GUIDE.zh-CN.md`：中文维护说明。
- `tests/test_template.py`：模板基础测试。

## 作为 Codex Skill 安装

把整个仓库克隆或复制到 Codex 的 skills 目录。例如 Windows：

```text
C:\Users\<USER>\.codex\skills\university-form-ppt-skill
```

包含 `SKILL.md` 的目录就是 Skill 根目录。

## 本地生成 PPT

Python 3.10+ 即可，核心替换脚本只依赖标准库。

```bash
python scripts/fill_certificate.py \
  --school-name "Xi'an Polytechnic University" \
  --output output.pptx
```

也可以手动指定姓名和学号：

```bash
python scripts/fill_certificate.py \
  --school-name "Soochow University" \
  --name "Li Feiyu" \
  --student-id 2023123456 \
  --output output.pptx
```

如果模板中的占位符数量与预期不一致，脚本会拒绝继续生成，避免误改模板。

## 当前固定输出字段

默认输出：

- First name
- Last name
- Address
- City
- State/Province
- Postal/Zip code
- Latitude
- Longitude
- 生成 PPT 时额外输出 Student ID

默认不再输出：

- Country/Region
- Address line 2
- VAT/GST ID

## PPT 硬性规则

默认只允许替换：

- `{{name}}`
- `{{student_id}}`
- `{{school_name}}`

右下角学校英文名必须保持单行。正文中较长的替换内容应自然向后顺排，不允许人为增加突兀的硬换行。

除为保证上述两点所需的最小局部调整外，不得修改模板其他内容。

## 重要说明

仓库内 PPT 是明确的演示模板。必须永久保留以下可见标识：

- `SAMPLE / NOT VALID`
- `仅供演示，不具效力`

不得删除、隐藏、裁切或遮挡这些标识。
