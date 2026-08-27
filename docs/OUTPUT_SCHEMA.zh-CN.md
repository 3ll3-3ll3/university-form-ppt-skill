# 输出字段规范

每次识别并确认学校后，聊天输出顺序固定如下。每个学校/表单字段必须单独放在一个可复制代码块中。

1. 学校中文名
2. Official English Name
3. First name —— 姓氏拼音，例如 `Li`
4. Last name —— 名字拼音，例如 `Feiyu`
5. Student ID
6. Address
7. City
8. State/Province
9. Postal/Zip code
10. 经纬度最后

默认不输出：

- Country/Region
- Address line 2
- VAT/GST ID

## 姓名字段约定

本项目特殊约定：

- `First name` = 姓的拼音
- `Last name` = 名的拼音

PPT `{{name}}` 使用合并后的形式，例如：

```text
Li Feiyu
```

不要从学校邮箱用户名推测用户真实姓名。

## 经纬度输出

- 如果只有一个相关主要校区，只输出一组明确对应校区的 Latitude/Longitude。
- 如果学校有多个校区，不要全部输出；最多选择两个最主要、最常见、最有代表性的校区，并分别标注校区名。
- 表单 Address 与主坐标必须对应同一个真实校区，不能地址来自 A 校区、坐标来自 B 校区。

## 生成 PPT 时的交付顺序

1. 由实际 PPT 直接渲染得到的 PNG；
2. PPTX；
3. 上述字段。

Google Drive 归档在同一次工作流中自动执行，并在声称完整完成前回读确认。
