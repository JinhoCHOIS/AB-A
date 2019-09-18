import util
import wordsegUtil

_X_ = None

class JointSegmentationInsertionProblem(util.SearchProblem):
    def __init__(self, query, bigramCost, possibleFills):
        self.query = query
        self.bigramCost = bigramCost
        self.possibleFills = possibleFills

    def start_state(self):
        # position before which text is reconstructed & previous word
        return 0, wordsegUtil.SENTENCE_BEGIN #현재까지 처리한 캐릭터 수, 이전에 리컨스트럭트 한 단어

    def is_end(self, state):
        return state[0] == len(self.query)

    def succ_and_cost(self, state):
        # raise NotImplementedError #remove this line
        pro, current_word = state
        for now_pro in range(pro + 1, len(self.query) + 1):
            vowel_removed_word = self.query[pro:now_pro]
            cont = self.possibleFills(vowel_removed_word)
            for now_cont in cont:
                next_state = now_pro, now_cont
                cost =self.bigramCost(current_word, now_cont)
                yield now_cont, next_state, cost

        #possilblefils만 써야함, 파이프연산 사용하면 안됨
        #use 'self.possiblefills(vowel_removed_word)' instead of
        # 'self.possiblefills(vowel_removed_word) | (vowel_removed_word)'
        #use two overlapped 'for' loops


unigramCost, bigramCost = wordsegUtil.makeLanguageModels('leo-will.txt')
smoothCost = wordsegUtil.smoothUnigramAndBigram(unigramCost, bigramCost, 0.2)
possibleFills = wordsegUtil.makeInverseRemovalDictionary('leo-will.txt', 'aeiou')
problem = JointSegmentationInsertionProblem('mgnllthppl', smoothCost, possibleFills)

import dynamic_programming_search
dps = dynamic_programming_search.DynamicProgrammingSearch(verbose=1)
# dps = dynamic_programming_search.DynamicProgrammingSearch(memory_use=False, verbose=1)
print(dps.solve(problem))

# import uniform_cost_search
# ucs = uniform_cost_search.UniformCostSearch(verbose=0)
# print(ucs.solve(problem))
