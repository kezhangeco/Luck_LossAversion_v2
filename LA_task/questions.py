#five levels of fixed values: -1,-2,-3,-4,-5.Each one's range will be [abs(X),6abs(x)].
import numpy
import random


v_50_1_initList = [0,0, 0, 0, 15,21]
v_50_2_initList = [5,10,15,30,30,30]


class question(object):
    v_100 = None
    v_50_1 = None
    v_50_2 = None
    CE_median = None      #median of certainty equivalence from the last trail of pure gains
    algorithmIndex = None  # 1 is pure gain, 2 is pure loss, 3 is mixed
    to_display = True
    count = 1
    initX = None
    limit = 6             ####the number of time point for each question. e.g., =5, every question repeats 5 times(iteration)
    mid_gain_list = []
    mid_loss_list = []
    mid_loss = None

    #initial trails#
    def __init__(self, algorithmIndex, initX, mid_loss_list=None, mid_gain_list=None):
        print('Init algorithmIndex is', algorithmIndex, 'initX is', initX)
        self.algorithmIndex = algorithmIndex
        self.initX = initX
        self.v_50_1 = v_50_1_initList[self.initX]
        self.v_50_2 = v_50_2_initList[self.initX]
        self.v_100_history_gain =[]     #history of gain in pure questions
        self.v_100_history_loss =[]
        self.v_50_2_history = []
        self.mid_gain_list = mid_gain_list
        self.mid_loss_list = question.mid_loss_list

        if self.algorithmIndex == 1:                  #gains pure gambles#
            self.v_100 = (self.v_50_1 + self.v_50_2) * 0.5
            self.v_100_history_gain.append(self.v_100)

        elif self.algorithmIndex == 2:            #losses pure gambles#
            self.v_50_1 = -self.v_50_1
            self.v_50_2 = -self.v_50_2
            self.v_100 = (self.v_50_1 + self.v_50_2) * 0.5
            self.v_100_history_loss.append(self.v_100)
        print('initializing question ', self.algorithmIndex, 'values are ', self.v_50_1, self.v_50_2, self.v_100)

    def initMixQuestion(self, lastTwoMedium):  #mixed gamblers
        print('last two medium in staircase mixed is ', lastTwoMedium)
        self.v_50_1 = lastTwoMedium
        self.v_50_2 = -lastTwoMedium
        self.v_100 = 0
        self.v_50_2_history.append(self.v_50_2)
        print('init mixed v_50_2 ', self.v_50_2)
        question.mid_gain_list.append(lastTwoMedium)
        print('mid gain list in question.mid ', question.mid_gain_list)
        return

     #following trails#
    def get_question(self, accepted):
        self.count += 1
        print("saving history to algorithm index ", self.algorithmIndex, " with value ", self.v_100)

        if self.count == self.limit + 1 and self.algorithmIndex < 4:
            self.to_display = False

        else:
            if self.algorithmIndex == 1:
                self.get_question_gain(accepted)
            elif self.algorithmIndex == 2:
                self.get_question_loss(accepted)
            elif self.algorithmIndex == 3:
                self.get_question_mixed(accepted)

            print('question ', self.algorithmIndex, ' proceeded to value', self.v_50_1, self.v_50_2, self.v_100)


    #pure gains, at the iteration 2, the algorithm change of v_100 is different from its following iteration
    def get_question_gain(self, accepted):
        print('v_100_history_gain is ', self.v_100_history_gain)
        if accepted: #accept the certainty
            if self.count == self.limit - 4: #the change at the iteration 2
                print('new v 100 = ', self.v_100, '+', self.v_50_1)
                self.v_100 = (self.v_100 + self.v_50_1) / 2 #v_50_1 is lower bound


            elif self.count >= self.limit - 3: #the change at iteration 3,4,5,6
                print('new v 100 = ', self.v_100, ' - ', self.v_100_history_gain[-2],'-', self.v_100)
                self.v_100 = self.v_100 - abs(self.v_100_history_gain[-2] - self.v_100)/2

        else:
            if self.count == self.limit - 4: #the change at the iteration 2
                print('new v 100 = ', 'self.v_100', self.v_100, '+', 'self.v_50_1', self.v_50_1)
                self.v_100 = (self.v_100 + self.v_50_2) / 2
            elif self.count >= self.limit - 3:
                print('new v 100 = ', self.v_100, '+', abs(self.v_100_history_gain[-2]), '-', self.v_100)
                self.v_100 = self.v_100 + abs(self.v_100_history_gain[-2] - self.v_100) / 2
        self.v_100_history_gain.append(self.v_100)
        print('... gain ...')

    def get_question_loss(self, accepted):
        print('v_100_history_loss is ', self.v_100_history_loss)
        if accepted: #accept certainty
            if self.count == self.limit - 4: #the change at the iteration 2
                print('new v 100 = ', self.v_100, '+', self.v_50_2)
                self.v_100 = (self.v_100 + self.v_50_2) / 2 #v_50_2 is lower bound

            elif self.count >= self.limit - 3:
                print('new v 100 = ', '-', abs(self.v_100), '+', abs(self.v_100),'-',abs(self.v_100_history_loss[-2]))
                self.v_100 = - (abs(self.v_100) + abs(abs(self.v_100) - abs(self.v_100_history_loss[-2])) / 2)

        else: #accept 50/50
            if self.count == self.limit - 4: #the change at the iteration 2
                print('new v 100 = ', self.v_100, '+', self.v_50_1)
                self.v_100 = (self.v_100 + self.v_50_1) / 2  #v_50_1 is upper bound
            elif self.count >= self.limit - 3:
                print('new v 100 = ', abs(self.v_100), '-', abs(self.v_100), '-', abs(self.v_100_history_loss[-2]))
                self.v_100 = - (abs(self.v_100) - abs(abs(self.v_100) - abs(self.v_100_history_loss[-2])) / 2)
        self.v_100_history_loss.append(self.v_100)
        print('... loss ...')

        self.get_mid_loss()

    def get_mid_loss(self):
        if self.count == self.limit:
            print('v_100_ history at iter is 6', self.v_100_history_loss)
            print('v_100_history last question ', self.v_100_history_loss[-1], 'v_100_history second lst ', self.v_100_history_loss[-2])
            question.mid_loss = (self.v_100_history_loss[-1] + self.v_100_history_loss[-2])/2
            question.mid_loss_list.append(question.mid_loss)
            print('mid loss list now in question.mid is ', question.mid_loss_list)
            return

        else:
            pass


    def get_question_mixed(self, accepted):
        print('start mixed---------------------------------------------')

        if self.count == self.limit - 4:  # the change at the iteration 2
            ###############correct#################
            if accepted: #accept certainty:
                self.v_50_2 = -abs(self.v_50_2)/2
                print('count is 1 and accept certainty =', self.v_50_2, 'self.getlasttwomediam for acccept 50/50 = ', self.v_50_1)

            else:
                #self.v_50_2 = - (abs(self.v_50_2) + 6 * self.v_50_1)/2
                self.v_50_2 = -abs(self.v_50_2) * 2
                print('count is 1 and reject certainty = ', self.v_50_2, 'self.getlasttwomediam for acccept 50/50 = ', self.v_50_1)

        elif self.count >= self.limit - 3:
            if accepted: #accept certainty
                self.v_50_2 = -(abs(self.v_50_2)) + abs(abs(self.v_50_2_history[-2]) - abs(self.v_50_2)) / 2
                print('count is NOT 1 and accept certainty = ', self.v_50_2, 'self.getlasttwomediam for acccept 50/50 = ', self.v_50_1)

            else:
                self.v_50_2 = -(abs(self.v_50_2)) - abs(abs(self.v_50_2_history[-2]) - abs(self.v_50_2)) / 2
                print('count is NOT 1 and reject certainty = ', self.v_50_2, 'self.getlasttwomediam for acccept 50/50 = ', self.v_50_1)

        self.v_50_2_history.append(self.v_50_2)
        print('mixed gambles v_50_2 history is  ', self.v_50_2_history)












