class Piccolo:
  clause =0
	var=256
	eqtn =0
	word = []
	
  mat =  [
	["63","7c","77","7b","f2","6b","6f","c5","30","01","67","2b","fe","d7","ab","76"],
	["ca","82","c9","7d","fa","59","47","f0","ad","d4","a2","af","9c","a4","72","c0"],
	["b7","fd","93","26","36","3f","f7","cc","34","a5","e5","f1","71","d8","31","15"],
	["04","c7","23","c3","18","96","05","9a","07","12","80","e2","eb","27","b2","75"],
	["09","83","2c","1a","1b","6e","5a","a0","52","3b","d6","b3","29","e3","2f","84"],
	["53","d1","00","ed","20","fc","b1","5b","6a","cb","be","39","4a","4c","58","cf"],
	["d0","ef","aa","fb","43","4d","33","85","45","f9","02","7f","50","3c","9f","a8"],
	["51","a3","40","8f","92","9d","38","f5","bc","b6","da","21","10","ff","f3","d2"],
	["cd","0c","13","ec","5f","97","44","17","c4","a7","7e","3d","64","5d","19","73"],
	["60","81","4f","dc","22","2a","90","88","46","ee","b8","14","de","5e","0b","db"],
	["e0","32","3a","0a","49","06","24","5c","c2","d3","ac","62","91","95","e4","79"],
	["e7","c8","37","6d","8d","d5","4e","a9","6c","56","f4","ea","65","7a","ae","08"],
	["ba","78","25","2e","1c","a6","b4","c6","e8","dd","74","1f","4b","bd","8b","8a"],
	["70","3e","b5","66","48","03","f6","0e","61","35","57","b9","86","c1","1d","9e"],
	["e1","f8","98","11","69","d9","8e","94","9b","1e","87","e9","ce","55","28","df"],
	["8c","a1","89","0d","bf","e6","42","68","41","99","2d","0f","b0","54","bb","16"]
	]
	
  def newstate():
    state = []
    state.append([])
    state.append([])
    state.append([])
    state.append([])

    for i in range(4):
      for j in range(4):
        state[i].append([None] * 4)

    return state

  def shiftrowa(row,val)
    temp = row[0:val]
    shr = row[(val):(len(row))]
		for t in temp {
        shr.append(t)
    }
		return shr
	
  def shiftState(state)
		state[1] = shiftrowa(state[1],1)
		state[2] = shiftrowa(state[2],2)
		state[3] = shiftrowa(state[3],3)
		return state
	
  def printstate(state)
		i=0
		print "State:"
		for r in state {
        for c in r:
				  print "#" + str(c) + "      "
			print 

	def addroundKeyGfirst()
		i = 1
		temp  = 256
		word.append(" ".join(range(385,513)))

		# $details.write("round 0:\n\t ptext = 1 .. 128\n\t rk[0] = 257 .. 384\n\t output = 385 .. 512\n")
    while i<=128:
			# $eq.write "x#{temp+i+128} -#{i} #{temp+i} 0\n"
			clause = clause + 1
			eqtn +=1
			i = i + 1
		
    var = var + 256
		return range(385,513)
	
  def addroundKey(rnd,inp)
		#x = $var-127
		y = var+1
		z = var+129
    word.append (" ".join(range(y:(y+128))))
		# $details.write("round #{rnd}: Add Round Key \n\t input = #{inp[0]}..#{inp[127]}\n\t rkey = #{y}..#{y+127}\n\t output = #{z}..#{z+127}\n")
    for i in range(128):
			# $eq.write "x#{z+i} -#{inp[i]} #{y+i} 0\n"
			clause +=1
		
    var = z+127
    return var[-127:]
	
  def addroundKeyfaulty(rnd,inp)
		#x = $var-127
		#y = $var+1
		z = var+1
		y = word[rnd].split(' ')
		#$details.write("round #{rnd}: Add Round Key \n\t input = #{inp[0]}..#{inp[127]}\n\t rkey = #{y[0]}..#{y[127]}\n\t output = #{z}..#{z+127}\n")
    for i in range(128):
			#$eq.write "x#{z+i} -#{inp[i]} #{y[i]} 0\n"
			clause +=1
		
    var = z+127
    return var[-127:]
	
  def shiftrow(rnd,inp)
		#x = $var-128+1
		y = var+1

		#$details.write("round #{rnd}: Shift ROW \n\t input = #{inp[0]}..#{inp[127]}\n\t output = #{y}..#{y+127}\n")
		#$eq.write("\n\nRound :#{rnd} --- SHIFT ROW --------\n\n")
		#inp = (x..(x+127)).to_a
    out = range(y:(y+128))
		state1 = newstate()
		state2 = newstate()
		i=0
    while i<128:
			j=0
      while j<4:
				t = j*8+i
        state1[j][i/32] = " ".join(inp[t:(t+8)])
        state2[j][i/32] = " ".join(out[t:(t+8)])
				j = j + 1
			i =  i + 32

		state2 = shiftState(state2)
    for u in range(4):
      for h in range(4):
				temp1 = state1[u][h].split(' ')
				temp2 = state2[u][h].split(' ')
				i=0 
        for i in range(8):
					# $eq.write("x#{temp2[i]} -#{temp1[i]} 0\n")
					clause += 1
					eqtn += 1
		
    var += 128
		return out
	
  def multiply(str1,str2)
		#str =(lenbit8(str2.to_i(16).to_s(2))).split('')
		 str = str2.split(' ')
    y = var[1:8]
		#$details.write(" round #{}:---------- Multiply----------\n\t input: #{str.to_s}\n\t output: #{y.join(',')}\n")
		var = var+8
		if(str1=="01")
			$eq.write("x#{y[0]} -#{str[0]} 0\n")
			$eq.write("x#{y[1]} -#{str[1]} 0\n")
			$eq.write("x#{y[2]} -#{str[2]} 0\n")
			$eq.write("x#{y[3]} -#{str[3]} 0\n")
			$eq.write("x#{y[4]} -#{str[4]} 0\n")
			$eq.write("x#{y[5]} -#{str[5]} 0\n")
			$eq.write("x#{y[6]} -#{str[6]} 0\n")
			$eq.write("x#{y[7]} -#{str[7]} 0\n")
		end
		if(str1=="02")
			$eq.write("x#{y[0]} -#{str[1]} 0\n")
			$eq.write("x#{y[1]} -#{str[2]} 0\n")
			$eq.write("x#{y[2]} -#{str[3]} 0\n")
			$eq.write("x#{y[3]} -#{str[0]} #{str[4]} 0\n")
			$eq.write("x#{y[4]} -#{str[0]} #{str[5]} 0\n")
			$eq.write("x#{y[5]} -#{str[6]} 0\n")
			$eq.write("x#{y[6]} -#{str[0]} #{str[7]} 0\n")
			$eq.write("x#{y[7]} -#{str[0]} 0\n")
		end
		if(str1=="03")
			$eq.write("x#{y[0]} -#{str[0]} #{str[1]} 0\n")
			$eq.write("x#{y[1]} -#{str[2]} #{str[1]} 0\n")
			$eq.write("x#{y[2]} -#{str[3]} #{str[2]} 0\n")
			$eq.write("x#{y[3]} -#{str[0]} #{str[4]} #{str[3]} 0\n")
			$eq.write("x#{y[4]} -#{str[0]} #{str[5]} #{str[4]} 0\n")
			$eq.write("x#{y[5]} -#{str[6]} #{str[5]} 0\n")
			$eq.write("x#{y[6]} -#{str[0]} #{str[7]} #{str[6]} 0\n")
			$eq.write("x#{y[7]} -#{str[0]} #{str[7]} 0\n")
		end
		clause +=8
		eqtn +=8
		return y

  def varXor(out,v1,v2,v3,v4):
		#$eq.write("\n\n var xor \n\n")
		out = out.split(' ')
    for i in range(8):
			#$eq.write("x#{out[i]} -#{v1[i]} #{v2[i]} #{v3[i]} #{v4[i]} 0\n")
			clause +=1
			eqtn +=1
	
  def mixColmEq(state, state2 ,rnd):
		i=0
		while i<4
		 	varXor(state2[0][i],multiply("02",state[0][i]),multiply("03",state[1][i]),multiply("01",state[2][i]),multiply("01",state[3][i]))
			varXor(state2[1][i],multiply("02",state[1][i]),multiply("03",state[2][i]),multiply("01",state[3][i]),multiply("01",state[0][i]))
			varXor(state2[2][i],multiply("02",state[2][i]),multiply("03",state[3][i]),multiply("01",state[0][i]),multiply("01",state[1][i]))
			varXor(state2[3][i],multiply("02",state[3][i]),multiply("03",state[0][i]),multiply("01",state[1][i]),multiply("01",state[2][i]))
			i = i + 1
	
  def pad(l,x):
		temp = l-len(x)
		s = ""
		while temp>0
			s = s + "0"
			temp -=1

		return s + x
	
  def mixcolumn(rnd,inp):
		#x = $var-127
		y = var+1
		  #$details.write("round #{rnd}: MixColumn \n\t input = #{inp[0]}..#{inp[127]}\n\t output = #{y}..#{y+127}\n")
		  #$details.write("\t intermediate var:#{y+128} .. #{$var}\n")
		#$eq.write("\n\nRound :#{rnd} --- Mix Column--------\n\n")
		#inp = (x..(x+127)).to_a
		out = range(y, (y+128))
		state1 = newstate()
		state2 = newstate()
		i=0
    while i<128:
			j=0
      while j<4:
				t = j*8+i
        state1[j][i/32] = " ".join(inp[t:(t+7)])
        state2[j][i/32] = " ".join(out[t:(t+7)])
				j = j + 1
			i =  i + 32
		var += 128
		mixColmEq(state1,state2,rnd)
		return out

  def substate(rnd,inp):
		#x = $var-127
		y = var+1
		  #$details.write("round #{rnd}: subByte \n\t input = #{inp[0]}..#{inp[127]}\n\t output = #{y}..#{y+127}\n")
		#$eq.write("\n\nRound :#{rnd} --- substate--------\n\n")
		#inp = (x..(x+127)).to_a
    out = range(y:(y+128))
		state1 = newstate()
		state2 = newstate()
		i=0
    while i<128:
			j=0
      while j<4:
				t = j*8+i
        state1[j][i/32] = " ".join(inp[t:(t+7)])
        state2[j][i/32] = " ".join(out[t:(t+7)])
				j = j + 1
			i =  i + 32
		var = var+128
    for i in range(4):
      for j in range(4):
				subByte (state1[j][i],state2[j][i])
		#$details.write("\t intermediate var:#{y+128} .. #{$var}\n")
		return out
	
  def subByte(str1,str2):
		start = var+1
		#len = output.size
		#y = (start..start+len).to_a
		str1 = str1.split(' ')
			str2 = str2.split(' ')
		
    file = open("out1anf.txt", "r")
		sboxeq = []
		sboxeq[0] = []
		index=0
    for line in file:
      if line[0:3] == "bit"
				index +=1
				sboxeq[index] = []
			else
				line =  line.replace("\n",'')
				sboxeq[index].append(line)
		
    for bit in range(8):
			count=0
      if "1" in sboxeq[bit]:
        tempvar = range(start, len(start+sboxeq[bit]))
				start += len(sboxeq[bit])
				#$eq.write "x#{str2[bit]} #{tempvar.join(' ')} 0\n"

			else
				tempvar = range(start, (start+len(sboxeq[bit])+1))
				start +=len(sboxeq[bit])+1
				#$eq.write "x#{str2[bit]} -#{tempvar.join(' ')} 0\n"
			end
			clause +=1
      for cls in sboxeq[bit]:
				if cls != "1"
					c1 = cls.replace("x","-x")
          for ind in range(8):
						c1 = c1.replace("x#{ind}",str1[ind])
					end
					c1 = c1.replace("*"," ")
					c1 = ([str(tempvar[count]) + " "] + ci.split("")).join('')
					#$eq.write "#{c1} 0\n"
					clause +=1
					
					c2 = cls.split('*')
          for lit in c2:
						#$eq.write "-#{tempvar[count]} #{str1[lit.gsub("x",'').to_i]} 0\n"
						clause +=1
					count +=1
		var = start-1
	
  def keygenerationAlgo():
		#$details.write "\n---------------Key Genraton Algo-----------------\n"
		#$details.write "\tcipher key= 129..256\n"
		key = []
    key[0] = range(129, 161)
		key[1] = range(161, 193)
		key[2] = range(193, 225)
		key[3] = range(225, 257)
		
		rkey = []
    for i in range(0, 11):
			w = word[i].split(' ')
      rkey.append(w[0:32])
      rkey.append(w[32:64])
      rkey.append(w[64:96])
      rkey.append(w[96:128])
		
    for i in range(0, 128):
			# $eq.write "x#{$word[0].split(' ')[i]} -#{(129..256).to_a[i]} 0\n"
			clause +=1
		
    for i in range(4, 44):
			temp = range(var+1, var+129)
			var += 128
			#$details.write "\nIteration: #{i}\n"
			printeq32bit(temp,rkey[i-1])
      if i%4 == 0:
				temp = rotword(temp)
				temp = subword(temp)
				temp = rkoneq(temp,i)
			
      for j in range(32):
				#$eq.write "x#{rkey[i][j]} -#{rkey[i-4][j]} #{temp[j]} 0\n"
				clause +=1
	
  def rkoneq(temp,i)
		temp1 = range(var+1, var+33)
		#$details.write "\t rkoneq: input: #{temp[0]}..#{temp[31]}, output: #{temp1[0]}..#{temp1[31]}\n"
		var +=32 
		const  = rkon(i,4)
		const = pad 32,const.to_i(16).to_s(2)
    for i in range(0, 32):
			if const[i] == '0'
				#$eq.write "x#{temp1[i]} -#{temp[i]} 0\n"
			else
				#$eq.write "x#{temp1[i]} #{temp[i]} 0\n"
			
      clause +=1
		return temp1
	
  def rkon(i,nk):
		t = i/nk
		s = "00000000"
		s[8-t] = '1'
    if t == 9:
			return  "1b000000"
    if t ==10:
			return "36000000"
		return pad 8,str.to_i(2).to_s(16).concat("000000")

  def subword(temp):
		temp1 = ($var+1..$var+32).to_a
		$details.write "\t subword: input: #{temp[0]}..#{temp[31]}, output: #{temp1[0]}..#{temp1[31]}\n"
		$var +=32
		subByte(temp[0..7].join(' '),temp1[0..7].join(' '))
		subByte(temp[8..15].join(' '),temp1[8..15].join(' '))
		subByte(temp[16..23].join(' '),temp1[16..23].join(' '))
		subByte(temp[24..31].join(' '),temp1[24..31].join(' '))
		$details.write "\t        intermediate #{temp1[31]}..#{$var}\n"
		return temp1
	end
	def rotword(temp)
		
		temp1 = ($var+1..$var+32).to_a
		$details.write "\t rotword: input: #{temp[0]}..#{temp[31]}, output: #{temp1[0]}..#{temp1[31]}\n"
		t = temp[24..31]
		temp = temp[0..23]
		t.each do |tr|
			temp.push(tr)
		end
		for i in 0..31
			$eq.write "x#{temp1[i]} -#{temp[i]} 0\n"
			$clause +=1
		end
		$var += 32
		return temp1
	end
	def printeq32bit(v1,v2)
		$details.write "\t Prineq32bit: input: #{v1[0]}..#{v1[31]}, output: #{v2[0]}..#{v2[31]}\n"
		for j in 0..31
			$eq.write "x#{v1[j]} -#{v2[j]} 0\n"
			$clause +=1
		end
	end
	def generateFaulteq(r)
		x = $roundinput[r-1]
		w = ($var+1..$var+128).to_a
		$var +=128
		u = ($var+1..$var+16).to_a
		$var +=16
		z = ($var+1..$var+128).to_a
		$var +=128
		y = ($var+1..$var+128).to_a
		$var += 128
		for i in 0..127
			$eq.write "x#{z[i]} -#{x[i]} #{y[i]} 0\n"
			$clause +=1
		end
		
		for i in 0..127
			$eq.write "x#{w[i]} #{z[i]} 0\n"
			$clause +=1
		end
		
		for i in 0..15
			t = w[8*i..8*i+7]
			t.each do |temp|
				$eq.write "-#{u[i]} #{temp} 0\n"
				$clause +=1
			end
			$eq.write "#{u[i]} #{t.join(' -').insert(0,'-')} 0\n"
			$clause +=1
		end
		$eq.write "#{u.join(' -').insert(0,'-')} 0\n"
		$clause +=1
		out = y
		for rnd in r..9
			out = substate(rnd,out)
			puts "round #{rnd}: var: #{$var}, clause:#{$clause}, eq:#{$eqtn}"
			out = shiftrow(rnd,out)
			puts "round #{rnd}: var: #{$var}, clause:#{$clause}, eq:#{$eqtn}"
			out = mixcolumn(rnd,out)
			puts "round #{rnd}: var: #{$var}, clause:#{$clause}, eq:#{$eqtn}"
			out = addroundKeyfaulty(rnd,out)
			puts "round #{rnd}: var: #{$var}, clause:#{$clause}, eq:#{$eqtn}"
		end
			rnd += 1
			out = substate(rnd,out)
			puts "round #{rnd}: var: #{$var}, clause:#{$clause}, eq:#{$eqtn}"
			out = shiftrow(rnd,out)
			puts "round #{rnd}: var: #{$var}, clause:#{$clause}, eq:#{$eqtn}"
			out = addroundKeyfaulty(rnd,out)
			puts "round #{rnd}: var: #{$var}, clause:#{$clause}, eq:#{$eqtn}"
	end
	def getequation(fault_round,ctext,ptext)
		$eq = File.open("equation.cnf","w")
		$details = File.open("details.txt",'w')
		p= pad 128,ptext.join('').to_i(16).to_s(2)
		c= pad 128,ctext.to_i(16).to_s(2)
		for i in 1..128
			if p[i-1] =='1'
				$eq.write "#{i} 0\n"
			else
				$eq.write "-#{i} 0\n"
			end
		end
		$clause +=128
		$roundinput = Array.new(10)
		out = addroundKeyGfirst
		for rnd in 1..9
			$roundinput[rnd-1]=out
			out = substate(rnd,out)
			puts "round #{rnd}: var: #{$var}, clause:#{$clause}, eq:#{$eqtn}"
			out = shiftrow(rnd,out)
			puts "round #{rnd}: var: #{$var}, clause:#{$clause}, eq:#{$eqtn}"
			out = mixcolumn(rnd,out)
			puts "round #{rnd}: var: #{$var}, clause:#{$clause}, eq:#{$eqtn}"
			out = addroundKey(rnd,out)
			puts "round #{rnd}: var: #{$var}, clause:#{$clause}, eq:#{$eqtn}"
		end
			rnd += 1
			$roundinput[rnd-1]=out
			out = substate(rnd,out)
			puts "round #{rnd}: var: #{$var}, clause:#{$clause}, eq:#{$eqtn}"
			out = shiftrow(rnd,out)
			puts "round #{rnd}: var: #{$var}, clause:#{$clause}, eq:#{$eqtn}"
			out = addroundKey(rnd,out)
			puts "round #{rnd}: var: #{$var}, clause:#{$clause}, eq:#{$eqtn}"
			for i in 1..128
				if c[i-1] =='1'
					$eq.write "#{out[i-1]} 0\n"
				else
					$eq.write "-#{out[i-1]} 0\n"
				end
			end
			$clause +=128
			keygenerationAlgo
			puts "key geaneration: var: #{$var}, clause:#{$clause}, eq:#{$eqtn}"
			generateFaulteq(fault_round)
	end

end


puts "Rajul"
x = Aes.new
y = x.newstate

y.each{ |z| 
  print y
}
puts y.class

a = Aes.new
#a.subByte("1 2 3 4 5 6 7 8","9 10 11 12 13 14 15 16")
ctext = "2b7e151628aed2a6abf7158809cf4f3c"
ptext = ["32", "43", "f6", "a8", "88", "5a", "30", "8d", "31", "31", "98", "a2", "e0", "37", "07", "34"]
a.getequation(8,ctext,ptext)
