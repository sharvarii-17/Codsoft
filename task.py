class Task:                                 #object for task
    def __init__(self, title, due_date):    #constructor to initiate class
        self.title = title                  #variables for title and due date.
        self.due_date = due_date            #task is initiated false since it is not completed
        self.completed = False