'''

You have to transform the json as per the requirement.
1) if id property is not available "data" json, you have to get the id from the "imageUrl" link which is "0F391ED1-0861-421A-B51F-0913C3091FF6"
2) If the type is not "DailyLookImage" you can add it in the value of the "children" property list
3) If the type is "DailyLookImage" then the "label" with "hero" value can come once otherwise the "label" property with "hero" value can not come more than once.


data={
    "type": "StoryContent",
    "children": [
        {
            "id": "78DFF8B8-5613-44DC-BD11-E463D494FD35",
            "label": "hero",
            "type": "TextContent",
            "text": "What does the fox say?"
        },
        {
            "id": "8c7661ee-9825-459a-9eba-1fda7eac2905",
            "imageUrl": "https://temp.s3.amazonaws.com/0F391ED1-0861-421A-B51F-0913C3091FF6/image/8c7661ee-9825-459a-9eba-1fda7eac2905.jpeg",
            "label": "hero",
            "type": "DailyLookImage",
            "altText": "Pow Pow Pow"
        },
        {
            "id": "5d4883BB-9725-459a-9eba-1fda7eac2906",
            "imageUrl": "https://temp.s3.amazonaws.com/0F391ED1-0861-421A-B51F-0913C3091FF6/image/5d4883BB-9725-459a-9eba-1fda7eac2906.jpeg",
            "label": "hero",
            "type": "DailyLookImage",
            "altText": "Yich Yich Yich"
        }
    ]
}


output = 
{
   "id":"0F391ED1-0861-421A-B51F-0913C3091FF6",
   "type":"StoryContent",
   "children":[
      {
         "id":"78DFF8B8-5613-44DC-BD11-E463D494FD35",
         "label":"hero",
         "type":"TextContent",
         "text":"What does the fox say?"
      },
      {
         "id":"8c7661ee-9825-459a-9eba-1fda7eac2905",
         "imageUrl":"https://temp.s3.amazonaws.com/0F391ED1-0861-421A-B51F-0913C3091FF6/image/8c7661ee-9825-459a-9eba-1fda7eac2905.jpeg",
         "label":"hero",
         "type":"DailyLookImage",
         "altText":"Pow Pow Pow"
      },
      {
         "id":"5d4883BB-9725-459a-9eba-1fda7eac2906",
         "imageUrl":"https://temp.s3.amazonaws.com/0F391ED1-0861-421A-B51F-0913C3091FF6/image/5d4883BB-9725-459a-9eba-1fda7eac2906.jpeg",
         "type":"DailyLookImage",
         "altText":"Yich Yich Yich"
      }
   ]
}

'''

def getChildrenList(listJsonData):
    d={}
    newL=[]
    count=0
    for i in listJsonData:
        if i["type"]!= "DailyLookImage":
            newL.append(i)

        elif i["type"] == "DailyLookImage" and i["label"] == "hero" and count==0:
            newL.append(i)
            count += 1
        elif count > 0 and i["type"] == "DailyLookImage" and i["label"] != "hero":
            newL.append(i)
        else:
            for k, v in i.items():
                if k != "label":
                    d[k] = v
            newL.append(d)
    return newL


def getId(data):
    for key,value in data.items():
        if key=="children":
            for inner in value:
                for k1,v1 in inner.items():
                    if k1 == "imageUrl":
                        listOfDict = v1.split('/')
                        return listOfDict[3]


newJson={}
if "id" not in newJson:
    newJson["id"] = getId(data)
    for key, value in data.items():
        if key != "children":
            newJson[key] = value
        else:
            newJson[key] = getChildrenList(value)
else:
    for key, value in data.items():
        if key != children:
            newJson[key] = value
        else:
            newJson[key] = getChildrenList(value)
    
print(newJson)



