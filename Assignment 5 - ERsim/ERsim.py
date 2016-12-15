import sys

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def printQueues(critical, serious, fair):
    print('   {0}'.format('Queues are:'))
    print('   {0} {1}'.format('Critical', critical.items))
    print('   {0} {1}'.format('Serious', serious.items))
    print('   {0} {1}'.format('Fair', fair.items))

def addPatient(queueName, queue, patient):
    queue.enqueue(patient)
    print('>>> Add patient {0} to {1} queue'.format(patient, queueName))
    print()
    
def treatCondition(queueName, critical, serious, fair):
    print('>>> Treat next patient on ', queueName, ' queue')
    print()
    if queueName == 'Critical':
        queue = critical
    if queueName == 'Serious':
        queue = serious
    if queueName == 'Fair':
        queue = fair
    if queue.size() != 0:
        patient = queue.dequeue()
        print('   Treating {0} from {1} queue'.format(patient, queueName))
        printQueues(critical, serious, fair)
        print()
    else:
        print('No patients available in that condition.')
        print()
        
def treatAll(critical, serious, fair):
    print('>>> Treat all patients')
    print()
    while (critical.size() > 0):
        patient = critical.dequeue()
        print('   Treating {0} from {1} queue'.format(patient, 'Critical'))
        printQueues(critical, serious, fair)
        print()
    while (serious.size() > 0):
        patient = serious.dequeue()
        print('   Treating {0} from {1} queue'.format(patient, 'Serious'))
        printQueues(critical, serious, fair)
        print()
    while (fair.size() > 0):
        patient = fair.dequeue()
        print('   Treating {0} from {1} queue'.format(patient, 'Fair'))
        printQueues(critical, serious, fair)
        print()
    if critical.size() == 0 and serious.size() == 0 and fair.size() == 0:
        print('   {0}'.format('No patients are available to treat'))

def treatNext(critical, serious, fair):
    print('>>> Treat next patient')
    print()
    if critical.size() != 0:
        patient = critical.dequeue()
        print('   Treating {0} from {1} queue'.format(patient, 'Critical'))
        printQueues(critical, serious, fair)
        print()
    elif serious.size() != 0:
        patient = serious.dequeue()
        print('   Treating {0} from {1} queue'.format(patient, 'Serious'))
        printQueues(critical, serious, fair)
        print()
    elif fair.size() != 0:
        patient = fair.dequeue()
        print('   Treating {0} from {1} queue'.format(patient, 'Fair'))
        printQueues(critical, serious, fair)
        print()
    else:
        print('   {0}'.format('No patients are available to treat'))
    
def main():
    critical = Queue()
    serious = Queue()
    fair = Queue()
    
    in_file = open ("ERsim.txt", "r")
    for line in in_file:
        line = line.strip()
        items = line.split()
        if len(items) == 3:
            command = items[0]
            patient = items[1]
            condition = items[2]
        if len(items) == 2:
            command = items[0]
            conditionOrPatients = items[1]
        if len(items) == 1:
            command = items[0]
        else:
            sys.exit
           
        if command == 'add':
            if condition == 'Critical':
                addPatient('Critical', critical, patient)
            if condition == 'Serious':
                addPatient('Serious', serious, patient)
            if condition == 'Fair':
                addPatient('Fair', fair, patient)
            printQueues(critical, serious, fair)
            print()
            
        if command == 'treat':
            if conditionOrPatients == 'Critical':
                treatCondition('Critical', critical, serious, fair)                   
            if conditionOrPatients == 'Serious':
                treatCondition('Serious', critical, serious, fair) 
            if conditionOrPatients == 'Fair':
                treatCondition('Fair', critical, serious, fair) 
            if conditionOrPatients == 'all':
                treatAll(critical, serious, fair)
            if conditionOrPatients == 'next':
                treatNext(critical, serious, fair)
            print()
                
        if command == 'exit':
            print('>>> Exit')
            print()
            sys.exit
    
main()
