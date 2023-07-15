class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        
        events.sort()

        started = []
        count = 0
        day = 0
        
        today = events[0][0]
        
        while day<n:
            while day<n and events[day][0]==today:
                heappush(started, events[day][1])
                day += 1

            heappop(started)
            count += 1
            today += 1

            while started and started[0]<today: 
                heappop(started)
                
            if day<n and not started: 
                today = events[day][0]

        while started:
            if heappop(started)>=today:
                today += 1
                count += 1

        return count