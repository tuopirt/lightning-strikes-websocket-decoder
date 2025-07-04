# filter for the data we got

t = {"time":1751431675354640600,"lat":36.879283,"lon":-109.63561,"alt":0,"pol":0,"mds":11814,"mcg":221,"status":0,"region":3,
 "sig":
    [{"sta":3173,"time":4491380,"lat":47.649044,"lon":-117.149841,"alt":640,"status":24},
     {"sta":2655,"time":4533785,"lat":47.940067,"lon":-116.742805,"alt":757,"status":10},
     {"sta":1503,"time":5024793,"lat":45.010864,"lon":-124.006073,"alt":30,"status":12},
     {"sta":2487,"time":5217865,"lat":50.50182,"lon":-104.660706,"alt":592,"status":12},
     {"sta":1670,"time":5218420,"lat":50.501842,"lon":-104.660805,"alt":581,"status":12},
     {"sta":2433,"time":5340491,"lat":44.108608,"lon":-93.210289,"alt":376,"status":12},
     {"sta":1046,"time":5436210,"lat":51.107212,"lon":-114.210037,"alt":1134,"status":2},
     {"sta":2430,"time":5545708,"lat":36.748119,"lon":-108.27182,"alt":1688,"status":4},
     {"sta":2530,"time":5591317,"lat":32.544704,"lon":-92.004089,"alt":41,"status":4},
     {"sta":1891,"time":6018790,"lat":51.260845,"lon":-120.203423,"alt":722,"status":12},
     {"sta":2772,"time":6567800,"lat":47.814789,"lon":-90.684029,"alt":540,"status":12},
     {"sta":1177,"time":6759663,"lat":45.396603,"lon":-88.124367,"alt":283,"status":10},
     {"sta":799,"time":6793020,"lat":35.727013,"lon":-86.886681,"alt":235,"status":10},
     {"sta":2176,"time":6986090,"lat":34.599266,"lon":-86.527885,"alt":458,"status":12},
     {"sta":3020,"time":7296174,"lat":38.221172,"lon":-84.817368,"alt":228,"status":12},
     {"sta":2543,"time":7620849,"lat":41.491768,"lon":-83.720009,"alt":186,"status":12},
     {"sta":2231,"time":9325755,"lat":51.688416,"lon":-76.133362,"alt":295,"status":4}],"delay":9.9,"lonc":0,"latc":0}

def customfilter(arr):
    #print("start filters")
    return {k:v for k, v in arr.items() if k != "sig"}

#print(customfilter(t))