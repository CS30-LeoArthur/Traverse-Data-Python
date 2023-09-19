# survey_file = open("survey-results.txt")

# survey_list = []
# for line in survey_file:
#     line = line.strip()
#     survey_list.append(line)

# survey_file.close()

# yes_count = 0
# no_count = 0
# maybe_count = 0
# for i in range(len(survey_list)):
#     if survey_list[i] == "Yes":
#         yes_count += 1
#     elif survey_list[i] == "No":
#         no_count += 1
#     elif survey_list[i] == "Maybe":
#         maybe_count += 1

# print(str(yes_count) + " " + str(no_count) + " " + str(maybe_count))

age_file = open("age-data.txt")

age_list = []
for line in age_file:
    line = line.strip()
    age_list.append(int(line))

age_file.close()

under_18_count = 0
between_18_and_35_count = 0
between_36_and_65_count = 0
above_65_count = 0
for i in range(len(age_list)):
    if age_list[i] < 18:
        under_18_count += 1
    elif age_list[i] <= 35:
        between_18_and_35_count += 1
    elif age_list[i] <= 65:
        between_36_and_65_count += 1
    else:
        above_65_count += 1

print("Under 18 (" + str(under_18_count) + "), 18 to 35 (" + str(between_18_and_35_count) + "), 36 to 65 (" + str(between_36_and_65_count) + "), Above 65 (" + str(above_65_count) + ")")

# number_file = open("number-data.txt")

# number_list = []
# for line in number_file:
#     line = line.strip()
#     number_list.append(int(line))

# number_file.close()

# even_count = 0
# odd_count = 0
# for i in range(len(number_list)):
#     if number_list[i]  % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1

# print("Even (" + str(even_count) + "), Odd (" + str(odd_count) + ")")
