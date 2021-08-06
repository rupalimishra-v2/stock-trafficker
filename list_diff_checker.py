import pandas as pd



if __name__ == '__main__':
 df = pd.read_excel('/Users/rupali/Desktop/test_diff.xlsx', sheet_name='0', engine='openpyxl')  # can also index sheet by name or fetch all sheets
 excel_list = df['excel_sheet'].tolist()
 notebook_list = df['notebook_sheet'].tolist()

 diff_list = []
 for i in excel_list :
    if i in notebook_list:
        continue
    else:
        diff_list.append(i)

 print(diff_list)

