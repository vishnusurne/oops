class player:
    def __init__(self,jn,n,r,w,tn):
        self.jersey_no=jn
        self.name=n
        self.runs=r
        self.wickets=w
        self.team_name=tn

    def setJersey_no(self,njn):
        self.jersey_no=njn

    def setName(self,nn):
        self.name=nn

    def setRuns(self,nr):
        self.runs=nr
    
    def setWickets(self,nw):
        self.wickets=nw
    
    def setTeam_name(self,ntn):
        self.team_name=ntn
    
    def getJersey_n(self):
        return self.jersey_n
    
    def getName(self):
        return self.name
    
    def getRuns(self):
        return self.runs
    
    def getWickets(self):
        return self.wickets
    
    def getTeam_name(self):
        return self.team_name
    


    
p1=player(7,"msd",17226,1,"india")
print(p1.runs)

p1.setRuns(18000)
print("new runs:",p1.runs)

print(p1.getName())