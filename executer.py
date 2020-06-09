from tracer import is_debug

class Executer:
    def __init__(self, plan):
        # if is_debug():
        #     print (plan)
        self.EXECUTION_PLAN = plan

    def __run__(self):
        if is_debug():
            print('Starting run program')

        index = 1
        while True:
            if self.EXECUTION_PLAN.get(index) == None:
                break

            index = self.EXECUTION_PLAN[index].__next__()