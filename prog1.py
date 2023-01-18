# adj = input("Enter a word: ")
# print(f"This is a string with a place holder {adj}")

num = 2345.123456789
precision = input("Enter number decimal places: ")
print (int(precision))

# option 1 is to specify precision inline: {0:.5f.format(float)} - this does not work if the precision is variable.
# option 2 is to use round function: round(float,decimal_places) - this works by casting the input which is str by default

print(f"The number with precision to {precision} decimal places is: {round(num,int(precision))}")
