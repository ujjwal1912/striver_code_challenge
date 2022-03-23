# There is one meeting room in a firm. There are N meetings in the form of (start[i], end[i]) 
# where start[i] is start time of meeting i and end[i] is finish time of meeting i.
# What is the maximum number of meetings

def maximumMeetings(self,n,start,end):
  # code here
  meeting_no = list(range(1,n+1))
  meetings = sorted(list(zip(start, end, meeting_no)), key = lambda x: x[1])
  meeting_order = []
  end = 0
  for meet in meetings:
      if end<meet[0]:
          meeting_order.append(meet[2])
          end = meet[1]
  # print(meeting_order)
  return len(meeting_order)
