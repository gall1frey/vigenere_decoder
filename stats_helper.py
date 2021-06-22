class stats_helper:
    def __init__(self,data):
        self.data = data
        self.sorted_data = sorted(data)

    def mode(self):
        mode_dict = dict(list((self.sorted_data.count(x),x) for x in set(self.sorted_data)))
        return mode_dict[max(mode_dict.keys())]

    def median(self):
        if len(self.sorted_data) % 2 == 1:
            return self.sorted_data[len(self.sorted_data)//2]
        else:
            return (self.sorted_data[((len(self.sorted_data)-1)//2)]+self.sorted_data[((len(self.sorted_data)+1)//2)])/2

    def quartiles(self):
        l = len(self.sorted_data)
        return (self.sorted_data[int(0.25*(l))],self.sorted_data[int(0.5*(l))],self.sorted_data[int(0.75*(l))])

    def iqr(self):
        quartiles = self.quartiles()
        return(quartiles[2]-quartiles[0])

if __name__ == '__main__':
    stats = stats_helper([1,2,1,1,3,5,3,2,1,5,7,3,1,1,4])
    print(stats.sorted_data)
    #stats = stats_helper([1,2,3,4,5,6,7])
    print("MODE:",stats.mode())
    print("MEDIAN:",stats.median())
    print("QUARTILES:",stats.quartiles())
    print("IQR:",stats.iqr())
