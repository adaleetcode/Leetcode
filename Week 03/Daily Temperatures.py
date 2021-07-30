class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0]*len(temperatures)
        stack = [] 
        for curr_index, curr_temp in enumerate(temperatures):
        
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_index = stack.pop()
                out[prev_index] = curr_index - prev_index
            
            stack.append(curr_index)
        
        return out