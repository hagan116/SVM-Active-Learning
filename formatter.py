#!usr/bin/python

class Formatter:
    # a function to format the magic04.data file for scikit-learn usage
    # once formatting is complete, the function returns both a 2-dimensional array of
    # attributes and entries, and a one-dimensional array of equal length containing labels
    @staticmethod
    def separate_magic(content):
        attributeList = []
        labelList = []
        for line in content: #iterate through each line in the file
            entries = line.split(",") # create an array containing each attribute/label from the line as an entry
            last = len(entries)-1 #get a reference to the last slot in the array. entries[-1] would also work
            if entries[last] == 'g': #assign an integer value for each label
                entries[last] = 1
            elif entries[last] == 'h':
                entries[last] = 2
            attributes = entries[:last]
            attributes = map(float, attributes) #convert attribute entries from string to float
            attributeList.append(attributes)
            labelList.append(entries[last])
        return attributeList, labelList #return an array containing attrbiutes for each entry, and an arr

    @staticmethod
    def separate_newsgroup(content):
        attributeList = []
        labelList = []
        for i in range(0,len(content)):
            attributeList.append(content[i][0])
            labelList.append(content[i][1])
        
        return attributeList, labelList #return an array containing attrbiutes for each entry, and an array containing labels

    @staticmethod
    def separate_mushroom(content):
        attributeList = []
        labelList = []
        alphabet = {'a': 1.0, 'b': 2.0, 'c': 3.0, 'd': 4.0, 'e': 5.0, 'f': 6.0, 'g': 7.0, 'h': 8.0, 'i': 9.0, 'j': 10.0,
                    'k': 11.0, 'l': 12.0, 'm': 13.0, 'n': 14.0, 'o': 15.0, 'p': 16.0, 'q': 17.0, 'r': 18.0, 's': 19.0, 't':20.0,
                    'u':21.0, 'v':22.0, 'w':23.0, 'x':24.0, 'y':25.0, 'z': 26.0}
        for line in content:
            entries = line.split(",")
            entries.pop(11) #get rid of entry with missing attribute
            if entries[0] == 'e':
                entries[0] = 1.0
            elif entries[0] == 'p':
                entries[0] = 2.0
            for i in range(1,len(entries)):
                entries[i] = alphabet[entries[i]]
            labelList.append(entries[0])
            attributeList.append(entries[1:])
        return attributeList, labelList
            
    @staticmethod
    def format_mushroom_sample(sample):
        attributeList = []
        labelList = []
        alphabet = {'a': 1.0, 'b': 2.0, 'c': 3.0, 'd': 4.0, 'e': 5.0, 'f': 6.0, 'g': 7.0, 'h': 8.0, 'i': 9.0, 'j': 10.0,
                    'k': 11.0, 'l': 12.0, 'm': 13.0, 'n': 14.0, 'o': 15.0, 'p': 16.0, 'q': 17.0, 'r': 18.0, 's': 19.0, 't':20.0,
                    'u':21.0, 'v':22.0, 'w':23.0, 'x':24.0, 'y':25.0, 'z': 26.0}
        
        entries = sample.split(",")
        entries.pop(11) #get rid of entry with missing attribute
        if entries[0] == 'e':
            entries[0] = 1.0
        elif entries[0] == 'p':
            entries[0] = 2.0
        for i in range(1,len(entries)):
            entries[i] = alphabet[entries[i]]
        return entries[1:], entries[0]
   
    @staticmethod
    def separate_bankAuth(content):
        attributeList = []
        labelList = []
        for line in content: #iterate through each line in the file
            entries = line.split(",") # create an array containing each attribute/label from the line as an entry
            last = len(entries)-1 #get a reference to the last slot in the array. entries[-1] would also work
            if entries[last] == '0': #assign an integer value for each label
                entries[last] = 1
            elif entries[last] == '1':
                entries[last] = 2
            attributes = entries[:last]
            attributes = map(float, attributes) #convert attribute entries from string to float
            attributeList.append(attributes)
            labelList.append(entries[last])
        return attributeList, labelList #return an array containing attrbiutes for each entry, and an array containing labels
        
    # a function to format the magic04.data file for scikit-learn usage
    # once formatting is complete, the function returns both a 2-dimensional array of
    # attributes and entries, and a one-dimensional array of equal length containing labels
    @staticmethod
    def separate_ionosphere(content):
        attributeList = []
        labelList = []
        for line in content: #iterate through each line in the file
            entries = line.split(",") # create an array containing each attribute/label from the line as an entry
            last = len(entries)-1 #get a reference to the last slot in the array. entries[-1] would also work
            if entries[last] == 'b': #assign an integer value for each label
                entries[last] = 1
            elif entries[last] == 'g':
                entries[last] = 2
            attributes = entries[:last]
            attributes = map(float, attributes) #convert attribute entries from string to float
            attributeList.append(attributes)
            labelList.append(entries[last])
        return attributeList, labelList #return an array containing attrbiutes for each entry, and an array containing labels

    @staticmethod
    def separate_sensor(content):
        attributeList = []
        labelList = []
        for line in content: #iterate through each line in the file
            entries = line.split(",") # create an array containing each attribute/label from the line as an entry
            last = len(entries)-1 #get a reference to the last slot in the array. entries[-1] would also work
            if entries[last] == 'Sharp-Right-Turn': #assign an integer value for each label
                entries[last] = 1
            elif entries[last] == 'Move-Forward':
                entries[last] = 2
            attributes = entries[:last]
            attributes = map(float, attributes) #convert attribute entries from string to float
            attributeList.append(attributes)
            labelList.append(entries[last])
        return attributeList, labelList #return an array containing attrbiutes for each entry, and an array containing labels

    @staticmethod
    def separate_madelon(content):
        attributeList = []
        labelList = []
        for line in content: #iterate through each line in the file
            entries = line.split(" ") # create an array containing each attribute/label from the line as an entry
            last = len(entries)-1 #get a reference to the last slot in the array. entries[-1] would also work
            if entries[last] == '-1': #assign an integer value for each label
                entries[last] = 1
            elif entries[last] == '1':
                entries[last] = 2
            attributes = entries[:last]
            attributes = map(float, attributes) #convert attribute entries from string to float
            attributeList.append(attributes)
            labelList.append(entries[last])
        return attributeList, labelList #return an array containing attrbiutes for each entry, and an array containing labels
        
    
    @staticmethod
    def separate_sonar(content):
        attributeList = []
        labelList = []
        for line in content: #iterate through each line in the file
            entries = line.split(",") # create an array containing each attribute/label from the line as an entry
            last = len(entries)-1 #get a reference to the last slot in the array. entries[-1] would also work
            if entries[last] == 'R': #assign an integer value for each label
                entries[last] = 1
            elif entries[last] == 'M':
                entries[last] = 2
            attributes = entries[:last]
            attributes = map(float, attributes) #convert attribute entries from string to float
            attributeList.append(attributes)
            labelList.append(entries[last])
        return attributeList, labelList #return an array containing attrbiutes for each entry, and an array containing labels
        
    
    @staticmethod
    def separate_spam(content):
        attributeList = []
        labelList = []
        for line in content: #iterate through each line in the file
            entries = line.split(",") # create an array containing each attribute/label from the line as an entry
            last = len(entries)-1 #get a reference to the last slot in the array. entries[-1] would also work
            if entries[last] == '0': #assign an integer value for each label
                entries[last] = 1
            elif entries[last] == '1':
                entries[last] = 2
            attributes = entries[:last]
            attributes = map(float, attributes) #convert attribute entries from string to float
            attributeList.append(attributes)
            labelList.append(entries[last])
        return attributeList, labelList #return an array containing attrbiutes for each entry, and an array containing labels
    
    @staticmethod
    def writeBoxplotOutput(accuracy, writer):
        length  = len(accuracy)
        numTrials = len(accuracy[1])
        for i in range(0,numTrials):
            for j in range(0,length):
                if j == length-1:
                    writer.write(str(accuracy[j][i]) + "\n")
                    break
                writer.write(str(accuracy[j][i]) + " ")
        return

    @staticmethod
    def writeHistogramOutput(accuracy,writer):
        for entry in accuracy:
            writer.write(str(entry) + "\n")
        return

    @staticmethod
    def confusion_matrix(prediction,set,output,j):
        last = len(prediction)-1
        tp = 0
        fp = 0
        fn = 0
        tn = 0
        for i in range(0,last):
            if prediction[i] == set[i]:
                if prediction[i] == 1:
                    tn += 1
                else:
                    tp +=1
            elif prediction[i] != set[i]:
                if prediction[i] == 1:
                    fn += 1
                else:
                    fp += 1

        print ("True Positives: " + str(tp) + "\tFalse Positives: " + str(fp))
        print ("True Negatives: " + str(tn) + "\tFalse Negatives: "+ str(fn))
        
        if j == 0:
            output.write("5%")
            output.write("\n")
        elif j == 1:
            output.write("7.5%")
            output.write("\n")
        else:
            output.write(str((j-1) * 10) + "%")
            output.write("\n")
        output.write("True Positives: " + str(tp) + "\tFalse Positives: " + str(fp))
        output.write("\n")
        output.write("True Negatives: " + str(tn) + "\tFalse Negatives: "+ str(fn))
        output.write("\n")

        accuracy = (float(tp) + float(tn))/(float(tn) + float(fp) + float(fn) + float(tp))
        precision = float(tp)/(float(tp) + float(fp))
        recall = float(tp)/(float(tp) + float(fn))
        return accuracy, precision, recall

    @staticmethod
    def f_measure(precision,recall):
        fMeasure = (2*precision*recall)/(precision+recall)
        return fMeasure

    #return a list of the averages of each element in a list of lists
    @staticmethod
    def takeAverage(l):
        result = []
        for i in range(0,len(l[0])):
            sum_vars = 0
            for j in range(0,len(l)):
                sum_vars += l[j][i]
            average = sum_vars/len(l)
            result.append(average)
        return result
