# 大学信息填写 + PPT 替换 Skill

[English](README.md) | [简体中文](README.zh-CN.md)

这是一个面向 Codex / ChatGPT 的专用 Skill，用于以下固定工作流：

- 根据大学名称、学校邮箱或邮箱域名识别学校；
- 核验学校官方英文名、主要校区地址和邮编；
- 按指定格式输出表单字段和校区经纬度；
- 随机生成符合中文姓名习惯的拼音姓名和适配版面的数字学号；
- 在内置 PPT 模板中只替换 `{{name}}`、`{{student_id}}`、`{{school_name}}` 三类占位符；
- 尽可能保持 PPT 原始版式、字体、字号、位置、行距、颜色和演示/无效标记不变；
- 交付前必须渲染检查第一行、正文连续顺排和右下角校名单行效果；
- 每次成功生成后，把 MD 记录、PPT 和由该 PPT 直接渲染得到的 PNG 一起归档到仓库。

## 仓库结构

- `SKILL.md`：Agent 的正式执行规则和硬性约束，是唯一操作规则源。
- `assets/certificate_template.pptx`：当前确认使用的 PPT 模板。
- `records/`：所有历史生成记录。
- `records/<中文学校名>/`：按中文学校名分类，每次生成保存同名 stem 的 `.md`、`.pptx`、`.png`。
- `scripts/fill_certificate.py`：尽量保守地替换 PPTX 占位符。
- `scripts/inspect_template.py`：检查模板占位符和结构。
- `scripts/random_identity.py`：随机生成中文拼音姓名和适配版面的学号。
- `data/names.json`：随机姓名数据源。
- `docs/OUTPUT_SCHEMA.md` / `docs/OUTPUT_SCHEMA.zh-CN.md`：输出字段规范。
- `docs/PPT_RULES.md` / `docs/PPT_RULES.zh-CN.md`：PPT 格式规则。
- `docs/RESEARCH_POLICY.md` / `docs/RESEARCH_POLICY.zh-CN.md`：学校信息核验规则。
- `docs/MAINTAINER_GUIDE.zh-CN.md`：中文维护说明。

## 记录归档规则

每次成功生成 PPT 后，必须在：

```text
records/<中文学校名>/
```

保存三件套。推荐直接使用本次随机学号作为文件名 stem，例如：

```text
records/湖南工学院/20253842.md
records/湖南工学院/20253842.pptx
records/湖南工学院/20253842.png
```

其中 PNG 必须是**由生成后的 PPT 直接渲染得到的图片**，不能用 AI 生图替代。

MD 文件记录学校、校区、表单字段、经纬度、随机姓名、学号等信息，并且在文件尾部用相对路径同时嵌入 PPT 链接和图片预览，例如：

```md
[下载 PPT](./20253842.pptx)

![PPT 预览](./20253842.png)
```

同一所学校生成多次时，继续存放在同一个中文学校文件夹中，以不同学号/record stem 区分。

## 回复交付顺序

每次生成后的聊天回复必须：

1. **先给由 PPT 直接渲染得到的图片**；
2. **再给 PPT 下载文件**。

不能只给 PPT，也不能用 AI 生成的近似图片代替真实 PPT 渲染图。

## 本地生成 PPT

Python 3.10+ 即可，核心替换脚本只依赖标准库。

```bash
python scripts/fill_certificate.py \
  --school-name "Xi'an Polytechnic University" \
  --output output.pptx
```

自动随机身份默认使用 8 位学号，以优先保证证书第一行不换行。只有在渲染检查确认第一行仍然完整单行时，才建议使用 9 位学号。

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

默认不再输出：Country/Region、Address line 2、VAT/GST ID。

## PPT 硬性规则

默认只允许替换 `{{name}}`、`{{student_id}}`、`{{school_name}}`。

必须同时满足：

1. 第一行包含姓名和 student ID 的整行必须保持单行；优先通过 8 位学号和较短随机拼音姓名适配。
2. 第二行及之后的正文必须像正常英文段落一样自然连续顺排，不能出现替换造成的突兀孤立单行。
3. 右下角学校英文名必须保持单行。
4. 每次生成后必须渲染并肉眼检查；失败则重做。

## 对话规则与 GitHub 同步

只要用户在当前对话里修改了这个 Agent / Skill 的规则，就要把 GitHub 仓库对应内容立即一起更新，不能只在聊天中记住。

## 重要说明

仓库内 PPT 是明确的演示模板。必须永久保留 `SAMPLE / NOT VALID` 与 `仅供演示，不具效力`，不得删除、隐藏、裁切或遮挡。
