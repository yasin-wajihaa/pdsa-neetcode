class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # output=[]
        # used=[]
        # for i in range(len(strs)):
        #     if i in used:
        #         continue
        #     sub_str=[]
        #     sub_str.append(strs[i])
        #     used.append(strs[i])
        #     for j in range(i+1,len(strs)):
        #         if j not in used and sorted(strs[i])==sorted(strs[j]):
        #             sub_str.append(strs[j])
        #             used.append(j)
        #     output.append(sub_str)
        # return output

        # for i in strs:
        #     sub_str=[]
        #     sub_str.append(i)
        #     for j in strs:
        #         if i!=j and sorted(i)==sorted(j) :
        #             sub_str.append(j)
        #             strs.remove(j)
        #     strs.remove(i)
        #     output.append(sub_str)
        # return output     

        groups={}

        groups = {}                      # label -> list of words with that label
        for s in strs:
            key = ''.join(sorted(s))                    # the group's "name" for word s
            if key not in groups:
                groups[key] = []        # start a new bucket
            groups[key].append(s)           # put s in its bucket
        return list(groups.values()) 

