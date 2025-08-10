contents = ["All carrots are be sliced","All eyes on me", "where are you" ]

filenames = ['doc.txt','report.txt','presentation.txt']

for content,filename,in zip(contents,filenames):
    file = open(f"files/{filename}", 'w')
    file.write(content)
    file.close()