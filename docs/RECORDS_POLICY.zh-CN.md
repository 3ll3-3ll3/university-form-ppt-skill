# 生成记录归档规则

## 目录

所有成功生成记录统一保存到：

```text
records/<中文学校名>/
```

学校分类目录必须使用学校官方中文名称。

## 每次生成的三件套

同一次生成必须使用相同 record stem，优先直接使用生成学号：

```text
<student_id>.md
<student_id>.pptx
<student_id>.png
```

PNG 必须由该 PPTX 直接渲染得到，不允许用 AI 生图替代。

## Markdown 内容

MD 至少记录：

- 中文学校名
- 官方英文学校名
- 采用校区
- First name / Last name
- Student ID
- Address
- City
- State/Province
- Postal/Zip code
- Latitude / Longitude
- 原始学校邮箱或学校线索（如有）
- PPT 视觉验收结果

MD 文件尾部必须包含对应 PPT 下载链接以及 PNG 内嵌预览，例如：

```md
[下载 PPT](./20253842.pptx)

![PPT 预览](./20253842.png)
```

## 完整性

只有 MD、PPTX、PNG 三件套都成功保存后，该记录才算完成归档。

如果当前执行环境不能把二进制 PPTX/PNG 写入 GitHub，必须明确报告“归档未完成”，不能只保存 MD 后声称完成。优先在本地仓库工作区保存三件套，待具备 Git push / GitHub 二进制写入能力时再同步。

## 聊天交付顺序

用户侧每次都必须先看到真实 PPT 渲染 PNG，再获得 PPTX 文件。不能只交付 PPT，也不能使用 AI 生成的预览图。
