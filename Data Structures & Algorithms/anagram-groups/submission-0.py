class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        for i in range(len(strs)):
            dict_i = {}
            for j in range(len(strs[i])):
                if strs[i][j] not in dict_i:
                    dict_i[strs[i][j]] = 1
                else:
                    dict_i[strs[i][j]] = dict_i[strs[i][j]] + 1
            freq[strs[i]] = dict_i

        bool_index = [0] * (len(strs))
        output = []

        for i in range(len(strs)):
            tmp = []
            if bool_index[i] == 0:
                bool_index[i] = 1
                tmp.append(strs[i])
            for j in range(i + 1, len(strs)):
                if (freq[strs[i]] == freq[strs[j]]) and (bool_index[j] != 1):
                    tmp.append(strs[j])
                    bool_index[j] = 1

            if tmp:
               output.append(tmp)

        return output