side = 10
spacing = 0.1
soil_depth = 1
gravel_depth = 1

total_area = side**2
radius = side/4
outer_green = radius**2+2*(radius**2-3.1415*radius**2/4)
inner_green = radius**2-3.1415*radius**2/4

outer_flowers = int(outer_green/spacing**2)

inner_flowers = int(inner_green/spacing**2)

print("The flowerbeds in the corners can fit "+str(outer_flowers)+" each and in total "+str(outer_flowers*4)+" flowers.")
print("The flowerbeds in the center can fit "+str(inner_flowers)+" each and in total "+str(inner_flowers*4)+" flowers.")
print("In total, the garden can fit " +str(4*(inner_flowers+outer_flowers))+" flowers.")
print("The flowerbeds in the corners requires "+str(soil_depth*(outer_green)/27)+" cubic yards of soil.")
print("The flowerbeds in the center requires "+str(soil_depth*(inner_green)/27)+" cubic yards of soil.")
print("The garden requires "+str(soil_depth*(outer_green+inner_green)/27)+" cubic yards of soil.")
print("THe garden requires "+str(gravel_depth*3*3.1415*radius**2/27)+" cubic yards of gravel.")

#I just want to note that there are cases when directly dividing by the spacing doesn't provide the right amount of flowers because even if the area of the center flowerbed is less than the spacing needed, you can still plant 1 flower.