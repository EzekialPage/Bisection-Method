#Ezekial Page
#Bisection Method

def bisect(func, tolerance):
    low = 0
    high = .11
    count = 1
    i = 1
    mid = (low + high)/2
    while(i < tolerance):
        oldMid = mid
        
        #first iteration output
        if count == 1:
            print(str(count) + "\t\t" + str(low) + "\t" + str(high) +
              "\t" + str(mid) + "\t------" + "\t" + str(f(func, mid)))

        #bisect conditions
        if (f(func,low) * f(func, mid)) < 0:
            high = mid
        elif (f(func, low)*f(func, mid)) > 0:
            low = mid
        else:
            i = tolerance
        mid = round( ((low + high)/2), 5)
        error = round(abs((mid - oldMid)/mid) * 100, 4)
        count+=1
        i+=1

        #output results of iteration
        print(str(count) + "\t\t" + str(low) + "\t" + str(high) +
              "\t" + str(mid) + "\t" + str(error) + "\t" + str(f(func, mid)))

def f(function, x):
    return eval(function)

print("Iteration\txl\txu\txm\terror\tf(xm)")
function = "pow(x,3) - 0.165*pow(x,2) + .0003993"
tolerance = 10
bisect(function, tolerance)
