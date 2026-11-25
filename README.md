# expense-tracker

軟體工程導論 Assignment 1：簡易記帳工具。
可以輸入多筆支出，並依類別產生圓餅圖。

## 輸入支出（Member A）

需求：Python 3（不需要額外安裝套件）

執行：

    python expense_input.py

依照提示輸入：
- 日期（格式 YYYY-MM-DD，直接按 Enter 會使用今天日期）
- 金額（必須是正數）
- 類別（例如 Food、Transport、Entertainment）
- 備註（可省略）

每筆資料會存到 `expenses.csv`，欄位為 `date,amount,category,note`。

## 產生圓餅圖（Member B）

需求：

    pip install matplotlib

執行（請先用 expense_input.py 輸入資料）：

    python expense_piechart.py

程式會讀取 `expenses.csv`，依類別加總金額並畫出圓餅圖，同時存成 `pie_chart.png`。

![Pie chart](pie_chart.png)