#import statements
import statistics as sts
import csv

#opening the csc file and reading it
with open("StudentsPerformance.csv", newline ="") as f:
    reader = csv.reader(f)
    file_data = list(reader)
    file_data.pop(0)
    scores = []

    #adding every student's score to the scores array
    for i in range(len(file_data)):
        math_score = file_data[i][5]
        scores.append(float(math_score))

    for i in range(len(file_data)):
        read_score = file_data[i][6]
        scores.append(float(read_score))
        
    for i in range(len(file_data)):
        write_score = file_data[i][7]
        scores.append(float(write_score))
    
    #Finding the mean median mode and standard deviation
    mean = sum(scores)/len(scores)
    median =  sts.median(scores)
    mode = sts.mode(scores)
    std_dev = sts.stdev(scores, mean)

    #finding standard deviation start and end values
    first_sd_start, first_sd_end = mean - std_dev, mean + std_dev
    second_sd_start, second_sd_end = mean - (2 * std_dev), mean + (2 * std_dev)
    third_sd_start, third_sd_end = mean - (3 * std_dev), mean + (3 * std_dev)

    #creating variables for scores between standard deviations
    scores_in_sd = 0
    scores_in_sd2 = 0
    scores_in_sd3 = 0

    #checking if the score lies between sd and adding to the variables above accordingly
    for i in scores:
        if(first_sd_start < i < first_sd_end):
            scores_in_sd += 1
        if(second_sd_start < i < second_sd_end):
            scores_in_sd2 +=1
        if(third_sd_start < i < third_sd_end):
            scores_in_sd3 += 1

    #calculating the percentage of scores in sd
    percentage_in_sd = (scores_in_sd/len(scores)) *100 
    percentage_in_sd2 = (scores_in_sd2/len(scores)) *100  
    percentage_in_sd3 = (scores_in_sd3/len(scores)) *100  

    print("Mean of this data --> " + str(mean) + "\nMedian of this data --> " + str(median) + "\nMode of data --> " + str(mode) + "\nStandard Deviation of this data --> " + str(std_dev) + "\n" + str(percentage_in_sd) + " of data the lies in 1 standard deviation\n" + str(percentage_in_sd2) + " of the data lies within 2 standard deviations\n" + str(percentage_in_sd3) + " of the data lies in 3 standard deviations")
          