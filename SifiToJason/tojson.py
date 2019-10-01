from string import Template

try:
    res = []
    index = 0
    t = Template('{"id" : $id, "x" : $x, "y" : $y, "tag" : $tag, "name" : "$name", "idimage" : $idimage, "idanalysis" : $idanalysis}')
    filepath = 'input'
    f = open("out.json", "w+")
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            #print("Line {}: {}".format(cnt, line.strip()))
            split = line.split("	")
            result = t.safe_substitute(id=split[0], x = split[1], y = split[2], tag= split[3], name=split[4], idimage=split[5], idanalysis=split[6])
            #print(result)
            res.append(result+",")
            index += 1
            line = fp.readline()
            cnt += 1

    resultarr = "["+ "".join(res)[:-1]+"]"
    print(resultarr)
    f.write(resultarr)
finally:
    fp.close()
    f.close()