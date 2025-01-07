import queue
import threading
import time
from queue import Queue
from datetime import datetime, timedelta

# sistema izvada cikos tiks sakta un beigta katra ediena pagatavosana

mealsAndPreparationTimes = queue.Queue()
class MealsWillBeReady(threading.Thread):
    def __init__(self, mealAndItsPreperationTime):
        super().__init__()
        self.mealAndItsPreperationTime = mealAndItsPreperationTime

    def run(self):
        startTime = datetime.now()
        # izvada cikos sak gatavot
        print(self.mealAndItsPreperationTime[0], "is STARTED to been prepared at", startTime.strftime("%H:%M:%S"))
        time.sleep((self.mealAndItsPreperationTime[1] * 60 / 1000))
        readyTime = (startTime + timedelta(minutes=round(self.mealAndItsPreperationTime[1],2))).strftime("%H:%M:%S")
        # izvada cikos beidz gatavot
        print(self.mealAndItsPreperationTime[0], "is READY at", readyTime)

def getResults():
    x = 1
    while  not mealsAndPreparationTimes.empty():
        myThread = MealsWillBeReady(mealAndItsPreperationTime=mealsAndPreparationTimes.get())
        if x == 1:
            x = x+1
            myThread.start()
        else:
            x = x+1
            # lai oficiants pienemtu pasutijumus un nodotu tos pavariem paiet 3 minutes
            time.sleep(3 * 60 / 1000)
            myThread.start()
    myThread.join() # lai tiktu pabeigti visi pavedieni un tad noteikts beigu laiks

mealsDictionary = {
    "mealsAndTheirPrepTime": [
        {
            "name": "Pancakes",
            "timeInMin": 15
        },
        {
            "name": "Salads",
            "timeInMin": 10
        },
        {
            "name": "Chicken fillet",
            "timeInMin": 25
        },
        {
            "name": "Soup",
            "timeInMin": 20
        },
        {
            "name": "Ice cream",
            "timeInMin": 15
        },
        {
            "name": "Salmon fillet",
            "timeInMin": 25
        }
    ]
}

for item in mealsDictionary["mealsAndTheirPrepTime"]:
    mealsAndPreparationTimes.put([item.get("name"), item.get("timeInMin")])

start_time = time.time()
getResults()
end_time = time.time()

# aprekina un izvada cik ilgs laiks paies kamer tiks pagatavoti visi edieni
print("Meals preperation took", round(((end_time-start_time) * 1000 / 60),2) , "minutes.")

