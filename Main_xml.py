import xlrd
txt = open("xm.txt", "a", encoding="utf-8")

#Open the workbook
wb = xlrd.open_workbook('tm1.xlsx')

#Open the sheet by index
sh = wb.sheet_by_index(0)
count = 0
#Read data with for loop
for sen in range(sh.nrows):
    if len(sh.row_values(sen)[0])>1:
        txt.write('{ \n "promptItems": \n [ \n{ ')
        txt.write(f'"itemcode": "I{count}", "mediaitems": [')
        txt.write('{ \n "annotationTemplate": false,')
        txt.write(f'"text": "{sh.row_values(sen)[0]}"')
        txt.write('}\n]\n}\n]\n},')
        count += 1
txt.write(']\n}\n]\n}')
txt.close()
