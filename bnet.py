import sys
Parents={"B":[],"E":[],"A":["B","E"],"J":["A"],"M":["A"]}
Probability_table={"B":0.001,"E":0.002,"ABE":0.95,"AB":0.94,"AE":0.29,"A":0.001,"JA":0.90,"MA":0.70,"J":0.05,"M":0.01}
class Bayesian_network:
	def __init__(self):
		self.symbol=['B','E','J','M','A']
		upper=[]
		lower=[]
		self.string=[]
		self.index=len(sys.argv)-1
		for i in range(1,len(sys.argv)): 
			if(sys.argv[i]=="given"): 
				self.index=i-1
			else:
				self.string.append(sys.argv[i])
	def computeProbability(self):
		upper=self.string[0:]
		upperextra=[]
		lower=self.string[self.index:]
		lowerextra=[]
		self.addextra_upper(upper,upperextra,self.symbol)
		self.addextra_upper(lower,lowerextra,self.symbol) 
		upper_combination=[]
		lower_combination=[] 
		self.createcombination(upper,upperextra,upper_combination) 
		self.createcombination(lower,lowerextra,lower_combination)
		upperprobability=[]
		lowerprobability=[]  
		array=self.combination(upper_combination,upperprobability)
		numerator=0 
		for i in array:
			numerator=numerator+i 
		array=self.combination(lower_combination,lowerprobability)
		denomenator=0
		for i in array:
			denomenator=denomenator+i
		probability=numerator/denomenator
		return probability
	def addextra_upper(self,var,varextra,symbol):
		var=list(map(lambda x:x[0],var)) 
		for i in range(0,len(symbol)): 
			if(symbol[i] not in var):
				varextra.append(symbol[i]) 
	def createcombination(self,var,varextra,varcombination):
		if(len(var)==0):
			return []
		if(len(varextra)==0):
			varcombination.append(var)
		else:
			first=varextra[0]
			var1=var+[first+"t"]
			var2=var+[first+"f"]
			rest=varextra[1:]
			self.createcombination(var1,rest,varcombination)
			self.createcombination(var2,rest,varcombination)
		return varcombination
	def combination(self,combination,probability_array): 
		if(len(combination)==0):
			return [1]
		else:
			
			for i in range(0,len(combination)): 
				probability=1
				combi=combination[i]
				#print(combi)
				for j in combi: 
					if(len(Parents[j[0]])==0):
						if(j[1]=="t"):
							#print(Probability_table[j[0]])
							probability=probability*Probability_table[j[0]]
						else:
							#print(1-Probability_table[j[0]])
							probability=probability*(1-Probability_table[j[0]])
					else:
						##print(Parents[j[0]])
						str1=j[0]  
						for k in Parents[j[0]]: 
							##print(k+"t")  
							if(k+"t" in combi): 
								str1=str1+k  
						##print(str1)
						if(j[1]=="t"):
							#print(Probability_table[str1])
							probability=probability*Probability_table[str1]
						else:
							#print(Probability_table[str1])
							probability=probability*(1-Probability_table[str1])
				probability_array.append(probability)
		return probability_array
bnet=Bayesian_network()
print(bnet.computeProbability())