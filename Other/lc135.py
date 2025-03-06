class Solution:
    def candy(self, ratings):
        n = len(ratings)
        return sum(self.dp(ratings, 0, n - 1, 1))

    def dp(self, ratings, start_index, end_index, max_val):
        if start_index > end_index:
            return []
        if start_index == end_index:
            return [max_val]
        elif end_index - start_index == 1: # độ dài là 2
            arr = ratings[start_index:end_index+1]
            if arr[0] < arr[1]:
                return [max_val, max_val + 1]
            elif arr[0] == arr[1]:
                return [max_val, max_val]
            else:
                return [max_val + 1, max_val]
        else:
            stack = []
            for i in range(start_index, end_index + 1):
                if i > start_index and i < end_index:
                    if (ratings[i] <= ratings[i+1] and
                        ratings[i] <= ratings[i-1]):
                        stack.append(i)
                else:
                    if (
                        (i == start_index and ratings[i] <= ratings[i+1]) or
                        (i == end_index and ratings[i] <= ratings[i-1])
                    ):
                        stack.append(i)

            tmp_start = start_index
            res = []
            for i in stack:
                if i == start_index:
                    res.append(max_val)
                    tmp_start = start_index + 1
                else:
                    new_arr = self.dp(ratings, tmp_start, i - 1, max_val + 1)
                    res.extend(new_arr) # Thay vì loop append, dùng extend
                    res.append(max_val)
                    tmp_start = i + 1

            if tmp_start <= end_index:
                new_arr = self.dp(ratings, tmp_start, end_index, max_val + 1)
                res.extend(new_arr) # Thay vì loop append, dùng extend

            return res