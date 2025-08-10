filenames = ['1.Raw Data.txt', '2.Report.txt','3.Presentation.txt']

for items in filenames:
    items = items.replace('.','-',1)
    print(items)