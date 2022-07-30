class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
                                                                                            #       2.2------2.4
        if len(intervals) == 1 :
                return 0
        intervals = sorted(intervals)
        print(intervals)
        count = 0
        start_prev = intervals[0][0]
        end_prev = intervals[0][1]
        i = 1
        # print(start_prev)
        while i < len(intervals) :

            end_current = intervals[i][1]
            start_current = intervals[i][0]
            #no overlap    
            if start_current >= end_prev :
                start_prev = start_current
                end_prev = end_current
                # print("no overlap")
                i +=1
            #else there is overlap
            else :
                if end_prev >=  end_current :
                    count+=1
                    end_prev = end_current
                    start_prev = start_current
                    i+=1
                    # print("ends before")
                else :
                    # len_current = end_current - start_current + 1
                    # len_prev = end_prev - start_prev + 1
                    # print("ends after")
                    if end_current >=end_prev :
                        count +=1
                        i = i + 1
                    else :
                        start_prev = start_current
                        end_prev = end_current
                        count += 1
                        i = i + 1
        return count
