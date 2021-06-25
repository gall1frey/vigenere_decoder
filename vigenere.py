from math import gcd

class vigenere:
    def __init__(self,key=None,ciphertext=None,plaintext=None,alphabet=None,freq=None):
        self.key = key
        self.key_length = 0
        self.ciphertext = ciphertext
        self.plaintext = plaintext
        self.alphabet = alphabet or 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.freq = freq or {
            'A': 0.08123837786542185,
            'B': 0.014892788379785303,
            'C': 0.027114199985738028,
            'D': 0.043191828988003486,
            'E': 0.12019549870270922,
            'F': 0.02303856765933638,
            'G': 0.020257483420459344,
            'H': 0.05921460425774672,
            'I': 0.07305420097310522,
            'J': 0.0010312501714179142,
            'K': 0.006895114178044245,
            'L': 0.03978541219837304,
            'M': 0.02611586205383345,
            'N': 0.06947773761265585,
            'O': 0.07681168165087793,
            'P': 0.018189497704371293,
            'Q': 0.0011245015167057042,
            'R': 0.06021294218965129,
            'S': 0.06280752373795274,
            'T': 0.09098588613462202,
            'U': 0.02877626808116158,
            'V': 0.011074968596238131,
            'W': 0.020948640450239437,
            'X': 0.0017278925744502285,
            'Y': 0.021135143140815018,
            'Z': 0.0007021277762845373
        }

    def sanitize(self,inp):
        inp = inp.upper()
        inp = ''.join(list(x for x in inp if x in self.alphabet))
        return inp

    def set_ct(self,ct):
        ct = self.sanitize(ct)
        self.ciphertext = ct

    def set_pt(self,pt):
        pt = self.sanitize(pt)
        self.plaintext = pt

    def set_key(self,key):
        key = self.sanitize(key)
        self.key = key
        self.key_length = len(self.key)

    def set_alpha(self,alpha):
        self.alphabet = alpha.upper()

    def set_freq(self,freq):
        if self.freq == None:
            self.freq = {}
        for i in freq.keys():
            if i not in self.freq.keys():
                self.freq[i.upper()] = freq[i]

    def check_errors(self,func):
        if self.alphabet == None:
            raise ValueError('Alphabet Not Provided!')
        if func == 'encode':
            if self.plaintext == None:
                raise ValueError('Plaintext Not Provided!')
            if self.key == None:
                raise ValueError('Key Not Provided!')
            for i in self.key:
                if i not in self.alphabet:
                    raise ValueError('Key not in alphabet!')
        elif func == 'decode':
            if self.ciphertext == None:
                raise ValueError('Ciphertext Not Provided!')
        elif func == 'decodeNoKey':
            if self.freq == None:
                raise ValueError('Frequency Not Provided!')
            if self.ciphertext == None:
                raise ValueError('Ciphertext Not Provided!')

    def scoring_func(self,in_str,shift):
        l = list(0 for i in range(len(self.alphabet)))
        for i in in_str:
            l[self.alphabet.index(i)] += 1
        for i in range(len(l)):
            l[i] = l[i] / len(in_str)
        text_freq = l
        lang_freq = list(self.freq.values())
        score = 0
        for i in range(len(self.alphabet)):
            score += text_freq[(i+shift)%26] * lang_freq[i]
        return score

    def Nmaxelements(self, in_list, N):
        final_list = []
        for i in range(N):
            final_list.append(max(in_list))
            in_list.remove(max(in_list))
        return final_list

    def gcd_multiple(self,in_list):
        if len(in_list) == 2:
            return gcd(in_list[0],in_list[1])
        else:
            return gcd(in_list[0],self.gcd_multiple(in_list[1:]))

    def get_key_length(self):
        ciphertext_shifted_list = []
        for i in range(len(self.ciphertext)):
            ciphertext_shifted_list.append('\u2005'*i+self.ciphertext)
        coincidences_list = []
        for i in range(1,len(ciphertext_shifted_list)):
            coincidence = 0
            for j in range(len(ciphertext_shifted_list[0])):
                if ciphertext_shifted_list[0][j] == ciphertext_shifted_list[i][j]:
                    coincidence += 1
            coincidences_list.append(coincidence)
        check = self.Nmaxelements(coincidences_list.copy(),10)
        spaces_list = [i for i in range(len(coincidences_list)) if coincidences_list[i] in check]
        diff = list((spaces_list[i] - spaces_list[i-1]) for i in range(1,len(spaces_list)))
        self.key_length = self.gcd_multiple(diff)
        return self.key_length

    def encode(self):
        self.check_errors('encode')
        shifts = [self.alphabet.index(i) for i in self.key]
        self.ciphertext = ''
        for i in range(0,len(self.plaintext),len(self.key)):
            for j in range(len(self.key)):
                if i+j >= len(self.plaintext):
                    break
                self.ciphertext += self.alphabet[(self.alphabet.index(self.plaintext[i+j])+shifts[j])%len(self.alphabet)]
        return self.ciphertext

    def decode(self):
        self.check_errors('decode')
        print("Decoding text using key '{0}'".format(self.key))
        shifts = [self.alphabet.index(i) for i in self.key]
        self.plaintext = ''
        for i in range(0,len(self.ciphertext),len(self.key)):
            for j in range(len(self.key)):
                if i+j >= len(self.ciphertext):
                    break
                self.plaintext += self.alphabet[(self.alphabet.index(self.ciphertext[i+j])-shifts[j])%len(self.alphabet)]
        return self.plaintext

    def decode_no_key(self):
        self.check_errors('decode')
        print("Determining key length...")
        key_length = self.get_key_length()
        print("Length of key:",self.key_length)
        print("Determining Key of length {0}...".format(self.key_length))
        ct = self.ciphertext
        ct_split = ['' for i in range(key_length)]
        key = ''
        for i in range(len(ct)):
            ct_split[i%key_length] += ct[i]
        for sub_ct in ct_split:
            scores = []
            for shift in range(len(self.alphabet)):
                score = self.scoring_func(sub_ct,shift)
                scores.append(score)
            key += self.alphabet[scores.index(max(scores))]
        self.key = key
        print("Key is:",key)
        return self.decode()


if __name__ == '__main__':
    pt = '''I PROPOSE to consider the question, 'Can machines think?' This should begin with definitions of the meaning of the terms 'machine' and 'think'. The definitions might be framed so as to reflect so far as possible the normal use of the words, but this attitude is dangerous. If the meaning of the words 'machine' and 'think' are to be found by examining how they are commonly used it is difficult to escape the conclusion that the meaning and the answer to the question, 'Can machines think?' is to be sought in a statistical survey such as a Gallup poll. But this is absurd. Instead of attempting such a definition I shall replace the question by another, which is closely related to it and is expressed in relatively unambiguous words.
    '''
    key = '''crypto'''
    ct = '''K GPDICUV rd vcpjgsxf vyc fnsukgdg, 'Qce kpvvkech mvkei?' Iawu jfdnzf scvbb yzrw wshzlxmwqeq dy hjv kttbkee dy hjv rtkau 'dyrawpv' ycw 'hjzlz'. Mvg ucubbkkgdgg ozewm pg wppfsf jm pl hq icuesek qd yot rq ehguzzax hjv ldkacc shx ch kft pctuq, qnh vygh thvzrjws kj bpgugimjl. Wh kft fscegcz ch kft pctuq 'btqjzlt' tbf 'kfxgy' cic ih pg wmjgr dp cmtakegcz vqn rwxm cic rhaoflar iuvb xm wu uguywelji mc gjapis vyc rhbecshbcp kfpm hjv kttbkee pgr vyc pggyvp ih hjv ojxgvzmc, 'Vop dyrawpvq iawpb?' gh mc dv qdnujk gc t gvrrxlhktya litmcn liey yh t Uccjji dqcj. Qnh vygh bg csqjkr. Keqixof fd pmhgdnibbi jsra o fvdxgwvzmc B gjrja ksrcyrx hjv ojxgvzmc um cemiast, nfxvv kj aahggcw gxzckcs mc kk ycw wu vveksujcs bb tvjpmwxvjn nbcdzxziqlq lhffj.
    '''
    cipher = vigenere()
    #cipher.set_pt(pt)
    cipher.set_key('KEY')
    cipher.set_ct('ZPYSRROBRDSCXGPITR')
    print(cipher.decode())
    #print(cipher.decode_no_key())
