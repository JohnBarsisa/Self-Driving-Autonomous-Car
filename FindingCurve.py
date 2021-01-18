def getHistogram(img,display=False,minVal = 0.1,region= 4):
 
    histValues = np.sum(img, axis=0)

maxValue = np.max(histValues)  # FIND THE MAX VALUE
minValue = minPer*maxValue

indexArray =np.where(histValues >= minValue) # ALL INDICES WITH MIN VALUE OR ABOVE
basePoint =  int(np.average(indexArray)) # AVERAGE ALL MAX INDICES VALUES

if display:
    imgHist = np.zeros((img.shape[0],img.shape[1],3),np.uint8)
    for x,intensity in enumerate(histValues):
       # print(intensity)
        if intensity > minValue:color=(255,0,255)
        else: color=(0,0,255)
        cv2.line(imgHist,(x,img.shape[0]),(x,img.shape[0]-(intensity//255//region)),color,1)
    cv2.circle(imgHist,(basePoint,img.shape[0]),20,(0,255,255),cv2.FILLED)