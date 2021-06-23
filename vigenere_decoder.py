from math import gcd

#Test case:
pt = '''I PROPOSE to consider the question, 'Can machines think?' This should begin with definitions of the meaning of the terms 'machine' and 'think'. The definitions might be framed so as to reflect so far as possible the normal use of the words, but this attitude is dangerous. If the meaning of the words 'machine' and 'think' are to be found by examining how they are commonly used it is difficult to escape the conclusion that the meaning and the answer to the question, 'Can machines think?' is to be sought in a statistical survey such as a Gallup poll. But this is absurd. Instead of attempting such a definition I shall replace the question by another, which is closely related to it and is expressed in relatively unambiguous words.
'''
key = '''crypto'''
ct = '''k gpdicuv rd vcpjgsxf vyc fnsukgdg, ‘qce kpvvkech mvkei?’ Iawu jfdnzf scvbb yzrw wshzlxmwqeq dy hjv kttbkee dy hjv rtkau ‘dyrawpv’ ycw ‘hjzlz’. Mvg ucubbkkgdgg ozewm pg wppfsf jm pl hq icuesek qd yot rq ehguzzax hjv ldkacc shx ch kft pctuq, qnh vygh thvzrjws kj bpgugimjl. Wh kft fscegcz ch kft pctuq ‘btqjzlt’ tbf ‘kfxgy’ cic ih pg wmjgr dp cmtakegcz vqn rwxm cic rhaoflar iuvb xm wu uguywelji mc gjapis vyc rhbecshbcp kfpm hjv kttbkee pgr vyc pggyvp ih hjv ojxgvzmc, ‘Vop dyrawpvq iawpb?’ gh mc dv qdnujk gc t gvrrxlhktya litmcn liey yh t Uccjji dqcj. Qnh vygh bg csqjkr. Keqixof fd pmhgdnibbi jsra o fvdxgwvzmc B gjrja ksrcyrx hjv ojxgvzmc um cemiast, nfxvv kj aahggcw gxzckcs mc kk ycw wu vveksujcs bb tvjpmwxvjn nbcdzxziqlq lhffj.
'''

class vigenere:
    def __init__(self,key=None,ciphertext=None,plaintext=None,alphabet=None):
        self.key = key
        self.ciphertext = ciphertext
        self.plaintext = plaintext
        self.alphabet = alphabet

    def set_key(self,key):
        self.key = key

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

    def set_alpha(self,alphabet):
        self.alphabet = alphabet

    def set_ct(self,ct):
        self.ciphertext = ct

    def set_pt(self,pt):
        self.plaintext = pt

    def cut_foreign_chars(self):
        if self.ciphertext != None:
            self.ciphertext = ''.join(list(x for x in self.ciphertext if x in self.alphabet))
            self.ciphertext.lower()

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

    def encode(self):
        self.check_errors('encode')
        self.ciphertext = "ENCODED."
        return self.ciphertext

    def decode(self):
        self.check_errors('decode')
        self.cut_foreign_chars()
        print("Determining key length...")
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
        length_of_key = self.gcd_multiple(diff)
        print("Length of key:",length_of_key)
        print("Determining Key of length {0}...".format(length_of_key))



if __name__ == '__main__':
    cipher = vigenere()
    cipher.set_key(key)
    cipher.set_alpha('abcdefghijklmnopqrstuvwxyz')
    cipher.set_ct(ct.lower())
    #cipher.set_ct('oaak kwiermk wovlfm rviwtt fylxn snl bt ixhxakl gytvg wgolzz mhrm laeix sipvtjl tf uw t prmlxre')
    cipher.decode()
