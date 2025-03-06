from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        while words:
            new_line = [words.pop(0)]
            l = len(new_line[0])
            while (words and
                   (l + len(words[0]) + 1 <= maxWidth)):
                l += len(words[0]) + 1
                new_line.append(words.pop(0))
            res.append(new_line)
        arr = []
        for i_th,line in enumerate(res):
            n_word = len(line)
            if n_word == 1:
                # 1 word
                str_line = line[0] + " "*(maxWidth - len(line[0]))
                arr.append(str_line)
                continue
            if i_th == len(res)-1:
                # last sentence
                str_line = " ".join(line)
                str_line += " "* (maxWidth - len(str_line))
                arr.append(str_line)
                continue
            
            total_l_word = len("".join(line))
            n_space = (maxWidth-total_l_word)//(n_word-1)
            n_sub_space = (maxWidth-total_l_word)%(n_word-1)
            str_line = ""
            for i in range(len(line)):
                if i == len(line) -1:
                    str_line+= line[i]
                    break
                str_line+= line[i] + n_space*" "
                if i < n_sub_space: str_line+=" "
            arr.append(str_line)
                
        return arr
solu = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification."]
words2 = ["What","must","be","acknowledgment","shall","be"]
words3 = words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 16

arr = solu.fullJustify(words2,16)
for x in arr:
    print(x)
                
                