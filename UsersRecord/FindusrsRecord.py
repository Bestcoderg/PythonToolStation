# version:python3
# Instructions:找到TMailFlow.txt中所有在openids中有记录的openid
#               每个用户一个文件，输出对应的记录
# Time:2020-09-25
# Author:@Bestcoderg


openids = set()
with open("openids.txt", "r+") as f:

    lines = f.readline()
    lines = lines.strip()
    lines = lines.replace(r'\n', '')
    # lines = re.sub(r'\n','',lines)
    while(lines != ""):
        lines = f.readline()
        lines = lines.strip()
        lines = lines.replace(r'\n','')
        openids.add(lines)

    #print(lines)
# print(openids)
with open("TMailFlow.txt", "r+",encoding="utf-8") as f:
    lines = f.readline()

    while True:
        #print(lines)
        linelist = lines.split('|')
        #print(linelist)
        if linelist[8] in openids:
            with open(str(linelist[8])+'.txt' ,'a+') as fout:
                fout.write(lines+'\n')

        lines = f.readline()
        if lines:
            continue
        else:
            break






