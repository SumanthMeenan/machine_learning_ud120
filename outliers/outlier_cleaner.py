#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)
    """
    '''
    predictions is a list of predicted targets that come from your regression, 
    ages is the list of ages in the training set, 
    net_worths is the actual value of the net worths in the training set
    '''
    cleaned_data = []
    errors = []
    print "predictions from the linear regression: ",predictions
    print "net_worths from the training set: ", net_worths
    errors = predictions - net_worths
    print "errors: ", errors

    import heapq
    import pprint
    #print "81 values with the smallest errors: ",heapq.nsmallest(81,errors)
    h = []
    for i in errors:
        heapq.heappush(h, i)
        
    s_heap = [heapq.heappop(h) for i in range(len(h))]
    print "s_heap: "
    pprint.pprint(s_heap)
    '''
    ### your code goes here
    original_cleaned_data_lenth = len(cleaned_data)
    for i in range(0, len(predictions)):
        age = ages[i][0]
        net_worth = net_worths[i][0]
        prediction = predictions[i][0]
        error = net_worth - prediction
        cleaned_data.append([age, net_worth, error])

    cleaned_data.sort(key=lambda element: element[2], reverse=True)
    cleaned_data = cleaned_data[0:int(len(cleaned_data)*0.9)]
    '''


    return cleaned_data

