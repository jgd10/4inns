import numpy as np

checkpoints = ['Start','Skye','HeyMs','Crow',
               'Tors','Gate','Snake','Edale',
               'Chap','White','Cat','Fin']
class Team:
    def __init__(self,name,position):
        self.name = name
        self.members = []
        self.times = []
        self.checkpoints = ['Start','Skye','HeyMs','Crow',
                            'Tors','Gate','Snake','Edale',
                            'Chap','White','Cat','Fin']
        self.rank = position

    def add_members(self,names):
        if type(names)==list:
            self.members.extend(names)
        else:
            self.members.append(names)

    def add_times(self,times):
        for i in range(12):
            t = times[i]
            dmy = t[:3]
            if dmy=='Ret' or dmy=='ret':
                act_time = -1.
            elif times[i] == 'Missed':
                act_time = self.times[-1]
            elif times[i] == 'DNS':
                act_time = -1.
            else:
                hrs  = float(t[:2])
                mins = float(t[3:])
                act_time = hrs+(mins/60.)
                if act_time < 6.0: act_time += 24.
            self.times.append(act_time)
        self._intervals()

    def _intervals(self):
        N = len(self.times)
        self.intvls = []
        for i in range(1,N):
            self.intvls.append(self.times[i]-self.times[i-1])
        self.cmsm = np.cumsum(self.intvls)
        self.total = self.cmsm[-1]

class Year:
    def __init__(self,year,teams):
        self.year = year
        self.teams = []
        self.teams.extend(teams)
        self._combineTeams()
        self.checkpoints = ['Start','Skye','HeyMs','Crow',
                            'Tors','Gate','Snake','Edale',
                            'Chap','White','Cat','Fin']
    def _combineTeams(self):
        self.names = []
        self.times = []
        self.intvls = []
        self.ranks = []
        self.totals = []
        for t in self.teams:
            self.names.append(t.name)
            self.times.append(t.times)
            self.intvls.append(t.intvls)
            self.ranks.append(t.rank)
            self.totals.append(t.total)
        self.names  = np.array(self.names) 
        self.times  = np.array(self.times)
        self.intvls = np.array(self.intvls)
        self.ranks  = np.array(self.ranks)
        self.totals  = np.array(self.totals)


