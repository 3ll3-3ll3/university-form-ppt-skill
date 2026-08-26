# 大学信息填写 + PPT 替换 Skill

[English](README.md) | [简体中文](README.zh-CN.md)

这是一个面向 Codex / ChatGPT 的专用 Skill，用于以下固定工作流：

- 根据大学名称、学校邮箱或邮箱域名识别学校；
- 核验学校官方英文名、主要校区地址和邮编；
- 按指定格式输出表单字段和校区经纬度；
- 随机生成符合中文姓名习惯的拼音姓名和适配版面的数字学号；
- 在内置 PPT 模板中只替换 `{{name}}`、`{{student_id}}`、`{{school_name}}` 三类占位符；
- 尽可能保持 PPT 原始版式、字体、字号、位置、行距、颜色和演示/无效标记不变；
- 交付前必须渲染检查第一行、正文连续顺排和右下角校名单行效果。

## 仓库结构

- `SKILL.md`：Agent 的正式执行规则和硬性约束，是唯一操作规则源。
- `assets/certificate_template.pptx`：当前确认使用的 PPT 模板。
- `scripts/fill_certificate.py`：尽量保守地替换 PPTX 占位符。
- `scripts/inspect_template.py`：检查模板占位符和结构。
- `scripts/random_identity.py`：随机生成中文拼音姓名和适配版面的学号。
- `data/names.json`：随机姓名数据源。
- `docs/OUTPUT_SCHEMA.md`：英文输出字段规范。
- `docs/OUTPUT_SCHEMA.zh-CN.md`：中文输出字段规范。
- `docs/PPT_RULES.md`：英文 PPT 格式规则。
- `docs/PPT_RULES.zh-CN.md`：中文 PPT 格式规则。
- `docs/RESEARCH_POLICY.md`：英文学校信息核验规则。
- `docs/RESEARCH_POLICY.zh-CN.md`：中文学校信息核验规则。
- `docs/MAINTAINER_GUIDE.zh-CN.md`：中文维护说明。
- `tests/test_template.py`：模板和随机身份基础测试。

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

自动随机身份默认使用 8 位学号，以优先保证证书第一行不换行。只有在渲染检查确认第一行仍然完整单行时，才建议使用 9 位学号：

```bash
python scripts/fill_certificate.py \
  --school-name "Soochow University" \
  --student-id-length 9 \
  --output output.pptx
```

也可以手动指定姓名和学号：

```bash
python scripts/fill_certificate.py \
  --school-name "Soochow University" \
  --name "Li Feiyu" \
  --student-id 20231234 \
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

必须同时满足：

1. 第一行包含姓名和 student ID 的整行必须保持单行；优先通过 8 位学号和较短随机拼音姓名适配，不能让学号单独掉到下一行。
2. 第二行及之后的正文必须像正常英文段落一样自然连续顺排。字段变长时，后续文字依次向后流动，不能出现替换逻辑造成的突兀孤立单行。
3. 右下角学校英文名必须保持单行。

每次生成后必须渲染并肉眼检查。任意一项失败都要重新生成更短随机身份和/或做最小必要局部调整，再重新渲染。

除为保证上述规则所需的最小局部调整外，不得修改模板其他内容。

## 对话规则与 GitHub 同步

只要用户在当前对话里修改了这个 Agent / Skill 的规则，就要把 GitHub 仓库的对应内容立即一起更新，不能只在聊天中记住。至少检查并同步：

- `SKILL.md`
- 对应英文/中文文档
- 受影响的脚本
- 可以覆盖该规则的测试

## 重要说明

仓库内 PPT 是明确的演示模板。必须永久保留以下可见标识：

- `SAMPLE / NOT VALID`
- `仅供演示，不具效力`

不得删除、隐藏、裁切或遮挡这些标识。
