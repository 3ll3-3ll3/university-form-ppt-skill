# 中文维护说明

正式执行规则以 `SKILL.md` 为准。

## 双模式

- 学生认证 -> `assets/certificate_template.pptx`
- 教师认证 -> `assets/teacher_certificate_template.pptx`

教师认证与学生认证使用同一学校查询、随机姓名和数字 ID、输出字段、版式保护、渲染验收、REDO、Drive 自动归档逻辑。区别仅在模板和 ID 占位符：学生为 `{{student_id}}`，教师为 `{{faculty_id}}`。

如果邮箱/域名明显属于学生或教师体系，自动选模式；角色无法可靠判断时只询问认证类型。

Drive 目录固定分开为：

```text
大学PPT生成记录/学生认证/<学校>/
大学PPT生成记录/教师认证/<学校>/
```

每次记录仍用 `YYYY-MM-DD_HH-mm` 命名三件套，Drive 上传并回读确认是强制完成门槛。

规则变更时同步 `SKILL.md`、中英文文档、相关脚本、测试和被替换的模板二进制。只有真实 GitHub 写入成功后才能声称同步完成。
