# 大学学生/教师认证信息填写 + PPT Skill

[English](README.md) | [简体中文](README.zh-CN.md)

当前 Skill 同时支持两种完全平行的工作流：**学生认证**与**教师认证**。

用户可能提供学生邮箱、教师邮箱、邮箱域名、学校名、学院名或其他明显学校线索。Agent 自动识别学校，并根据明确的角色/域名证据选择学生或教师模式；确实无法判断时，只询问认证类型，不猜测。

## 模板

- 学生：`assets/certificate_template.pptx`
- 教师：`assets/teacher_certificate_template.pptx`

学生模板占位符：`{{name}}`、`{{student_id}}`、`{{school_name}}`。
教师模板占位符：`{{name}}`、`{{faculty_id}}`、`{{school_name}}`。

教师认证与学生认证的学校查询、随机姓名/数字 ID、PPT 格式保护、渲染验收、聊天字段、REDO 和自动归档要求完全一致。教师模式只是在模板内部把同一随机数字 ID 写入 `{{faculty_id}}`。

## Google Drive 目录

学生和教师记录必须分开：

```text
大学PPT生成记录/学生认证/<中文学校名>/
大学PPT生成记录/教师认证/<中文学校名>/
```

每次生成保存同名三件套，并以本地生成时间精确到 1 分钟命名：

```text
YYYY-MM-DD_HH-mm.md
YYYY-MM-DD_HH-mm.pptx
YYYY-MM-DD_HH-mm.png
```

Google Drive 归档是必须且自动完成的硬性步骤。只有 PPTX、实际渲染 PNG、含真实 Drive 链接的 MD 均上传成功，并回读目标学校文件夹确认三件套存在后，任务才算完整完成。

## 输出字段

学生和教师认证继续使用同一套聊天输出字段和顺序。为兼容现有流程，教师模式默认仍显示 `Student ID` 字段名；该数值实际填入教师模板的 `{{faculty_id}}`。如果用户明确要求，可改用 `Faculty ID` 文案。

## 共同 PPT 规则

两种模式都只替换当前模板允许的占位符，保护非占位符格式和内容；第一行姓名 + 数字 ID 必须单行；后续正文自然顺排；右下角学校官方英文全名必须单行；源模板中存在的演示/无效标识必须保留；交付前必须实际渲染 PNG 检查。

## 仓库职责

GitHub 只维护工作流、脚本、文档、测试和两套最新模板；具体学校生成记录只进入 Google Drive。
