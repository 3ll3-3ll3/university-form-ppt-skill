# 大学信息填写 + PPT 替换 Skill

[English](README.md) | [简体中文](README.zh-CN.md)

这是一个面向 Codex / ChatGPT 的专用 Skill，用于以下固定工作流：

- 根据大学名称、学校邮箱或邮箱域名识别学校；
- 核验学校官方中文名、官方英文全名、主要校区地址、邮编和经纬度；
- 随机生成较短的中文拼音姓名和适配第一行版面的数字学号；
- 在最新用户确认的 PPT 模板中只替换 `{{name}}`、`{{student_id}}`、`{{school_name}}`；
- 尽可能保持模板原始版式、字体、字号、位置、行距、颜色和演示/无效标记不变；
- 交付前必须渲染检查第一行、正文连续顺排和右下角官方英文校名单行效果；
- 每次成功生成后，自动把 MD、PPTX 和由该 PPT 直接渲染得到的 PNG 归档到 Google Drive，不再等待用户二次提醒。

## GitHub 仓库用途

本仓库只维护可复用工作流，不保存具体学校生成记录：

- `SKILL.md`：Agent 正式执行规则，是唯一操作规则源。
- `assets/certificate_template.pptx`：当前用户确认使用的最新 PPT 模板。
- `scripts/fill_certificate.py`：保守替换 PPTX 占位符。
- `scripts/inspect_template.py`：检查模板占位符和结构。
- `scripts/random_identity.py`：随机生成拼音姓名和版面友好学号。
- `scripts/archive_record.py`：生成按分钟时间戳命名的本地三件套，供 Google Drive 归档流程使用。
- `tests/`：工作流测试。
- `docs/`：中英文维护文档。

具体学校生成记录统一保存在 Google Drive，不再写入 GitHub `records/`。

## Google Drive 归档规则

每次成功生成后，必须自动归档到：

```text
大学PPT生成记录/<中文学校名>/
```

同一次生成的 MD、PPTX、PNG 使用完全相同的 record stem，并且文件名必须使用**精确到 1 分钟的生成日期时间**：

```text
YYYY-MM-DD_HH-mm.md
YYYY-MM-DD_HH-mm.pptx
YYYY-MM-DD_HH-mm.png
```

例如：

```text
2026-08-27_01-11.md
2026-08-27_01-11.pptx
2026-08-27_01-11.png
```

时间戳使用用户当前本地/会话时区。以后不再默认使用 Student ID 作为归档文件名。若同一学校在同一分钟内已经存在同名记录，只允许为避免覆盖而追加 `_<student_id>`。

PNG 必须由生成后的 PPT 直接渲染，不能使用 AI 生图替代。

MD 至少记录：中文校名、官方英文全名、用户原始输入、First name、Last name、完整随机拼音姓名、Student ID、Address、City、State/Province、Postal/Zip code、校区、经纬度、生成时间及时区、PPT 视觉验收结果。MD 尾部必须保存 Google Drive 返回的 PPT 和 PNG **真实链接**，禁止拼接或伪造链接。

只有 MD、PPTX、PNG 三件套均成功上传，并在可用时完成目标文件夹回读确认，才算归档完成。

## 回复交付顺序

每次生成后的聊天回复必须：

1. 先给由 PPT 直接渲染得到的 PNG；
2. 再给 PPTX；
3. 再按规定顺序给学校字段；
4. 经纬度最后输出。

Google Drive 归档是默认自动流程尾步骤，不需要用户再说“请你完成”。

## 当前固定输出字段

默认顺序：

- 学校中文名
- Official English Name
- First name
- Last name
- Student ID
- Address
- City
- State/Province
- Postal/Zip code
- 经纬度（最后）

默认不输出：Country/Region、Address line 2、VAT/GST ID。

## PPT 硬性规则

默认只允许替换 `{{name}}`、`{{student_id}}`、`{{school_name}}`。

必须同时满足：

1. 第一行姓名和 Student ID 必须完整保持单行；优先换更短姓名，再换更短学号，不允许修改正文排版来硬塞。
2. 第二行及之后正文允许自然换行，但禁止人为插入换行或硬拆词。
3. 正文和右下角学校名必须使用同一个官方英文全名，禁止简称或自行翻译。
4. 右下角学校英文全名必须保持单行；必要时只允许对该处做最小局部适配。
5. 每次生成后必须渲染并肉眼检查；失败则重做。
6. `SAMPLE / NOT VALID` 与 `仅供演示，不具效力` 必须永久保留且清晰可见。

## REDO

若用户指出英文校名、学号换行、正文格式、落款、模板格式或 Google Drive 文件有误，必须完整 REDO：重新生成 PPT → 重新渲染 PNG → 重新检查 → 替换 Drive PPT → 替换 Drive PNG → 更新 MD。禁止只修聊天文件。

## 对话规则与 GitHub 同步

只要用户在当前对话里修改了这个 Agent / Skill 的规则，就要把 GitHub 仓库对应内容立即一起更新，不能只在聊天中记住。具体学校生成记录仍只进入 Google Drive。

## 重要说明

仓库内 PPT 是明确的演示模板。必须永久保留 `SAMPLE / NOT VALID` 与 `仅供演示，不具效力`，不得删除、隐藏、裁切、弱化或遮挡。
