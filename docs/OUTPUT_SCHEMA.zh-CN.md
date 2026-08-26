# 输出字段规范

每次识别并确认学校后，默认返回以下字段。聊天中每个字段应单独放在一个可复制代码块中。

1. `First name` —— 姓氏拼音，例如 `Li`
2. `Last name` —— 名字拼音，例如 `Feiyu`
3. `Address`
4. `City`
5. `State/Province`
6. `Postal/Zip code`
7. `Latitude`
8. `Longitude`
9. `Student ID` —— 生成 PPT 时额外返回

默认不再输出：

- `Country/Region`
- `Address line 2`
- `VAT/GST ID`

## 一致性要求

用于表单地址和经纬度的校区必须是同一个校区，不能出现地址来自 A 校区、坐标来自 B 校区的情况。

## 姓名规则

姓名可以随机生成，不从数字学号邮箱推断真实身份。默认使用二字或三字中文姓名对应的拼音形式。

例如：

```text
First name: Li
Last name: Feiyu
```

PPT 中的 `{{name}}` 使用合并后的形式：

```text
Li Feiyu
```
