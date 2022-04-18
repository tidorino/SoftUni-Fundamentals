all_people = int(input())
people_for_course = int(input())

# sum_courses = int(all_people / people_for_course)
#
# print(sum_courses)
sum_people = 0
sum_curses = 0
rest_people = 0
course1 = 0
for i in range(1, all_people + 1):
    sum_people = i
    if sum_people % people_for_course == 0:
        sum_curses += 1

total_p_c = sum_curses * people_for_course
rest_for_course = sum_people - total_p_c
if 0 < rest_for_course:
    course1 = 1

total_numb_courses = course1 + sum_curses
print(total_numb_courses)
