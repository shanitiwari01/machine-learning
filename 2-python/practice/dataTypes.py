integersData = 1290
floatData = 12.32
booleanData = True
stringData = "Hello"
listData = [1,2,3,4,5,5]
tupleData = (1,2,3,4,5)
dictionaryData = { "name": "shani", "age": 23, "listData": listData, "tupleData": tupleData }
setData = set(listData)


print(f"""
      integersData: {integersData}, type: {type(integersData)}
      floatData: {floatData}, type: {type(floatData)}
      booleanData: {booleanData}, type: {type(booleanData)}
      stringData: {stringData}, type: {type(stringData)}
      listData: {listData}, type: {type(listData)}
      tupleData: {tupleData}, type: {type(tupleData)}
      dictionaryData: {dictionaryData}, type: {type(dictionaryData)}
      setData: {setData}, type: {type(setData)}
""")