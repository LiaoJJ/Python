# for computer a output size after a conv filter to a image
# by Ljj 

print('Please input a number: Image Size')
image_size = input()   
print('Please input a number: Filter Size')
filter_size = input()
print('Please input a number: Stride')
stride = input()
print('The output Image Size is: %.2f'%((int(image_size)-int(filter_size))/int(stride)+1))