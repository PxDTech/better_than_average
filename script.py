# codewars 8 kyu kata
# How good are you really?
# There was a test in your class and you passed it. Congratulations!
# But you're an ambitious person. You want to know if you're better than the average student in your class.
# You receive an array with your peers' test scores. Now calculate the average and compare your score!
# Return True if you're better, else False!
# Note:
# Your points are not included in the array of your class's points. For calculating the average point you may # add your point to the given array!

def better_than_average(class_points, your_points):
    if your_points > ((sum(class_points) + your_points) / (len(class_points) + 1)):
        return True
    else:
        return False



print(better_than_average([29, 55, 74, 60, 11, 90, 67, 28], 21))
