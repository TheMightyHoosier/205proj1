#this is a comment
from PIL import Image
# print(im1.getpixel((0,0))[0]) <- An example

#Making a list of images.
imagelist = [] 

#Opening and adding to the list of images.
for i in range(1,10): 
    imagelist.append(Image.open("./Project1Images/"+str(i)+".png"))

#Makes a new image to be used.
newim = Image.new("RGB",(imagelist[0].size[0], imagelist[0].size[1]))

#Lists for the red, green, and blue values.
pixellistR =[]
pixellistG = []
pixellistB = []

#Nested loops to get shtuff done, yeah!
for y in range(0, imagelist[0].size[1]): 
    for x in range(0, imagelist[0].size[0]):
        for myImage in imagelist:
            
            #Gets the color values.
            redpix, greenpix, bluepix = myImage.getpixel((x,y))
            
            #Adds the color values to an appropriate list.
            pixellistR.append(redpix) 
            pixellistG.append(greenpix)
            pixellistB.append(bluepix)
        
        #Sorts the lists of pixels
        pixellistR.sort() 
        pixellistG.sort()
        pixellistB.sort()
        
        #Setting median pixel colors to new image.
        newim.putpixel((x,y),(pixellistR[4], pixellistG[4], pixellistB[4]))
        
        #Clear the lists
        pixellistR = []
        pixellistG = []
        pixellistB = []
        
newim.save("NewImage.png")