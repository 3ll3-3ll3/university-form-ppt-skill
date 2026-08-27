# Google Drive 生成记录归档规则

## 唯一正式归档位置

所有具体学校生成记录统一保存到 Google Drive：

```text
大学PPT生成记录/<中文学校名>/
```

GitHub 只维护 Agent/Skill 工作流、模板、脚本、文档和测试，不保存具体学校的生成记录。

## 自动归档是强制完成条件

Google Drive 归档必须在每次 PPT 生成的同一次工作流中自动执行，不允许等待用户第二次说“请完成”“归档”或类似指令。

正确流程：

```text
生成 PPT
→ 实际渲染 PNG
→ 视觉验收
→ 准备聊天交付内容
→ 自动上传最终 PPTX
→ 自动上传最终 PNG
→ 用真实返回的 PPT/PNG Drive URL 写入 MD
→ 上传 MD
→ 回读目标学校文件夹
→ 确认三件套存在
→ 才允许声称本次任务完整完成
```

如果任一外部步骤失败，必须明确写：

```text
该步骤当前没有成功完成。
```

禁止伪造上传、链接、文件替换、删除、渲染或回读成功。

## 每次生成的三件套

同一次生成必须使用相同 record stem：

```text
<record_stem>.md
<record_stem>.pptx
<record_stem>.png
```

PNG 必须由最终 PPTX 实际渲染得到，禁止使用 AI 生图替代。

## 文件名：精确到 1 分钟

record stem 使用本地生成日期时间，精确到 1 分钟：

```text
YYYY-MM-DD_HH-mm
```

例如：

```text
2026-08-27_09-37.md
2026-08-27_09-37.pptx
2026-08-27_09-37.png
```

如果同一学校在同一分钟再次生成一条记录，仅为避免覆盖追加：

```text
YYYY-MM-DD_HH-mm_<student_id>.*
```

常规情况下不再使用 Student ID 作为文件名 stem。

## Markdown 内容

MD 至少记录：

- 中文学校名；
- 官方英文全名；
- 用户原始输入；
- First name；
- Last name；
- 完整随机拼音姓名；
- Student ID；
- Address；
- City；
- State/Province；
- Postal/Zip code；
- 采用校区/校区列表；
- 对应经纬度；
- PPT 视觉验收结果；
- 对应 PPT 的真实 Google Drive URL；
- 对应 PNG 的真实 Google Drive URL。

只有实际上传返回的 URL 才能写入 MD，禁止预测、拼接或伪造 URL。

## 完成验证

一次归档只有同时满足以下条件才算成功：

1. 最终 PPTX 上传成功；
2. 最终 PNG 上传成功；
3. 写入真实链接的最终 MD 上传成功；
4. 再次读取 `大学PPT生成记录/<中文学校名>/`，确认预期的 `.md/.pptx/.png` 三个文件都存在。

仅“准备了本地三件套”不等于归档完成。

## REDO

只要发现英文校名、使用简称、第一行换行、正文异常、落款两行、模板错误、Drive 保存旧版本或其他生成错误，必须全链路 REDO：

```text
重新生成 PPT
→ 重新渲染 PNG
→ 重新视觉验收
→ 替换/更新 Drive PPTX
→ 替换/更新 Drive PNG
→ 更新 Drive MD
→ 回读确认
```

禁止只修聊天文件而保留 Google Drive 中的错误版本。
