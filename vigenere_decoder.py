from stats_helper import stats_helper

#Test case:
pt = '''I PROPOSE to consider the question, 'Can machines think?' This should begin with definitions of the meaning of the terms 'machine' and 'think'. The definitions might be framed so as to reflect so far as possible the normal use of the words, but this attitude is dangerous. If the meaning of the words 'machine' and 'think' are to be found by examining how they are commonly used it is difficult to escape the conclusion that the meaning and the answer to the question, 'Can machines think?' is to be sought in a statistical survey such as a Gallup poll. But this is absurd. Instead of attempting such a definition I shall replace the question by another, which is closely related to it and is expressed in relatively unambiguous words.

The new form of the problem can be described in terms of a game which we call the 'imitation game'. It is played with three people, a man (A), a woman (B), and an interrogator (C) who may be of either sex. The interrogator stays in a room apart from the other two. The object of the game for the interrogator is to determine which of the other two is the man and which is the woman. He knows them by labels X and Y, and at the end of the game he says either 'X is A and Y is B' or 'X is B and Y is A'. The interrogator is allowed to put questions to A and B thus:'''
key = '''start'''
ct = '''K GPDIWAG km rhvakucg mpm slchmqwp, 'Tyc fikjzltl bpkei?' Iaqa uymjel jgxgc pqbj ucubvqvzmcl wn vyc bxivkee dy bpg kcgfa 'uctfxgm' ipu 'rwbvs'. Vyc sxnqpzrxhva ozewm jm hiybxl aq rq ih zmhccrm aw hrp pl xwujgqem bjv ldkuin lqt hn bjv udkla, dlr iaqa ckrxmclg zq stvogimjl. Qn vyc bxivkee dy bpg nmgwa 'uctfxgm' ipu 'rwbvs' cic ih jm hfscw jg goybbvqpx fdp bpgp ygx kwodmceg cuvb xm qa fzdubkcnk rd xakcgc iam kqeaanaqqe rwtb bjv kttvqpx ycw bpg rlhpmz vf rwx ycgjrxhv, 'Kce kpvpqpvq iaqvm?' zq ih jm ufsvab qp r qitbqukgrtt awittr acey yh t Oincse iwtn. Ssi mpqu zq puactu. Gclbmcu mu tbbgdnibvo ulaw t lmhzlxmqwp Z qwttt tvnatkm vyc fnmavzmc ug ipfrwxz, ejzaw ba knfqteg zgcyixl bq zr pgl qu vvekmauvb xg zmnrrxomta llpfjqilmjl ewtuq.

Iam vgn ddku wh kft izwdccb viv dv btlkzkscs bv bgikh hn i irkt ppqey ut vitn kft 'buqvrrxhv ocdc'. Xm qa rcynxl ekkf iazmg gcditm, c dyc (T), i eqdyc (U), ivf rl xgbmtimvtbwt (T) uwh uia sc dy mqvycg lmf. Vyc xgbmtimvtbwt jrpra qp r pdhu irrpi yzwo kft hbpgi rlh. Bpg fzyxkb qw rwx oiov ddk bpg zlixzzqxyihz qu km sxbmtdgcx epktf dy bpg frwxz byf gh mpm orl pgl ejzaw ba bjv udfiv. Jv ichea vycb ug tcscal F ipu W, pgl iv kft xvl qw rwx oiov ft ligu vgiamz 'Z zq P tvl A zq Q' hz 'F kj Z pgl G kj Y'. Iam qpkcgkwockmg ba incmlxl bq gsi jcmukgdga bq R ycw J bjlq:'''

class vigenere:
    def __init__(self,key=None,ciphertext=None,plaintext=None,alphabet=None):
        self.key = key
        self.ciphertext = ciphertext
        self.plaintext = plaintext
        self.alphabet = alphabet

    def set_key(self,key):
        self.key = key

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
        #for i in range(len(ciphertext_shifted_list)):
        #    print(ciphertext_shifted_list[i])
        coincidences_list = []
        for i in range(1,len(ciphertext_shifted_list)):
            coincidence = 0
            for j in range(len(ciphertext_shifted_list[0])):
                if ciphertext_shifted_list[0][j] == ciphertext_shifted_list[i][j]:
                    coincidence += 1
            coincidences_list.append(coincidence)
        stats = stats_helper(coincidences_list)
        iqr = stats.iqr()
        third_quartile = stats.quartiles()[2]
        print(iqr)
        pos_list = []
        for i in range(len(coincidences_list)):
            if coincidences_list[i] > third_quartile + (1 * iqr):
                pos_list.append(i)
        count = 0
        diff = 0
        for i in range(1,len(pos_list)):
            diff += (pos_list[i]-pos_list[i-1])
            count += 1
        possible_key_length = diff/count
        print(possible_key_length)

if __name__ == '__main__':
    cipher = vigenere()
    cipher.set_key(key)
    cipher.set_alpha('abcdefghijklmnopqrstuvwxyz')
    #cipher.set_ct(ct.lower())
    cipher.set_ct('oaak kwiermk wovlfm rviwtt fylxn snl bt ixhxakl gytvg wgolzz mhrm laeix sipvtjl tf uw t prmlxre')
    cipher.decode()
