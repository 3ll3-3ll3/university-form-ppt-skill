# 生成记录归档规则

## 归档位置

所有成功生成记录统一保存到 Google Drive：

```text
大学PPT生成记录/<中文学校名>/
```

学校分类目录必须使用学校官方中文名称。

具体学校生成记录不再保存到 GitHub；GitHub 仓库只维护 Skill 工作流、文档、脚本、测试和最新模板。

## 每次生成的三件套

同一次生成必须使用相同 record stem，并且 record stem 必须使用精确到 1 分钟的生成日期时间：

```text
YYYY-MM-DD_HH-mm
```

因此三件套为：

```text
YYYY-MM-DD_HH-mm.md
YYYY-MM-DD_HH-mm.pptx
YYYY-MM-DD_HH-mm.png
```

示例：

```text
2026-08-27_01-11.md
2026-08-27_01-11.pptx
2026-08-27_01-11.png
```

时间戳使用用户当前本地/会话时区。Student ID 不再作为常规归档文件名。

如果同一学校在同一分钟内已经存在完全相同的 record stem，为避免覆盖已有记录，可以追加：

```text
_<student_id>
```

例如：

```text
2026-08-27_01-11_7314286.pptx
```

PNG 必须由对应 PPTX 直接渲染得到，不允许用 AI 生图替代。

## 自动归档

Google Drive 归档是默认完整工作流的一部分，不得等待用户在生成后再发送“请你完成”之类的二次指令。

完整生成流程必须自动包含：

生成 PPT → 渲染 PNG → 视觉检查 → 生成 MD → 上传 PPTX/PNG → 取得真实 Drive 链接 → 将真实链接写入 MD → 上传/更新 MD → 在可用时回读目标文件夹确认三件套存在。

只有以上步骤成功后才能声称“Google Drive 归档完成”。

## Markdown 内容

MD 至少记录：

- 中文学校名
- 官方英文学校全名
- 用户原始输入/学校线索
- First name
- Last name
- 完整随机拼音姓名
- Student ID
- Address
- City
- State/Province
- Postal/Zip code
- 采用校区
- Latitude / Longitude
- 生成日期时间
- 时区
- PPT 视觉验收结果

MD 文件尾部必须保存 Google Drive 返回的 PPT 和 PNG 真实链接，例如：

```md
[PPT 文件](真实 Drive PPT 链接)

![PPT 预览](真实 Drive PNG 链接)
```

禁止自行拼接、猜测或伪造 Google Drive 链接。

## 完整性与 REDO

只有 MD、PPTX、PNG 三件套都成功保存后，该记录才算完成归档。

若用户指出英文校名、Student ID 换行、正文格式、落款、模板格式或 Drive 文件有误，必须完整 REDO：重新生成 PPT → 重新渲染 PNG → 重新检查 → 替换 Drive PPT → 替换 Drive PNG → 更新 MD。禁止只修聊天中的文件而保留错误的 Drive 版本。

## 聊天交付顺序

用户侧每次必须先看到真实 PPT 渲染 PNG，再获得 PPTX，然后再输出学校字段，经纬度最后。Google Drive 归档应自动作为同一工作流的尾部动作执行，不需要用户再次提醒。
