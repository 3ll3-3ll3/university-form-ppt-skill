# 生成记录归档规则

## 唯一正式归档位置

所有成功生成记录统一保存到 Google Drive：

```text
大学PPT生成记录/<中文学校名>/
```

GitHub 不保存具体学校生成记录，只保存 Agent/Skill 工作流、模板、脚本、文档和测试。

## 每次生成的三件套

同一次生成必须使用同一个、精确到 1 分钟的时间戳 record stem：

```text
YYYY-MM-DD_HH-mm.md
YYYY-MM-DD_HH-mm.pptx
YYYY-MM-DD_HH-mm.png
```

如果同一学校在同一分钟生成第二条记录，仅为避免覆盖追加：

```text
YYYY-MM-DD_HH-mm_<student_id>.*
```

PNG 必须由该 PPTX 直接渲染得到，不允许用 AI 生图替代。

## Markdown 内容

MD 至少记录：

- 中文学校名
- 官方英文学校全名
- 用户原始输入
- First name / Last name
- 完整随机姓名
- Student ID
- Address
- City
- State/Province
- Postal/Zip code
- 校区
- 经纬度
- PPT 视觉验收结果
- 真实 Google Drive PPT 链接
- 真实 Google Drive PNG 链接

禁止写入预测、拼接或尚未真实返回的 Drive 链接。

## 强制自动归档

Google Drive 归档是每次生成的**强制完成条件**，而且必须在同一次工作流里自动执行。

不允许：

- 等用户再次说“归档”或“请完成”才上传；
- 在 Drive 尚未完成时把生成流程正常结束；
- 只上传 PPT/PNG 而漏掉 MD；
- 上传后不回读目标文件夹；
- 伪造上传成功或 Drive 链接。

一次生成只有在以下四项都成功后才算完整完成：

1. PPTX 上传成功；
2. PNG 上传成功；
3. MD 上传成功；
4. 目标学校 Drive 文件夹回读确认三件套存在。

若任一步失败，必须明确写：

```text
该步骤当前没有成功完成。
```

并禁止声称本次生成已完整完成。

## REDO

若英文校名、排版、落款、Student ID 换行、模板、Drive 文件等任一处有误，必须全链路 REDO：

```text
重新生成 PPT
→ 重新渲染 PNG
→ 重新视觉验收
→ 替换/更新 Drive PPT
→ 替换/更新 Drive PNG
→ 更新 Drive MD
→ 回读确认
```

禁止只修聊天中的文件而保留 Drive 中的错误版本。
