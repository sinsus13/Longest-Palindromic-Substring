class Manacher:

    def process(self,inp_str: str) -> str:
        self.inp_str = inp_str
        lst_str = ['@', '#']
        for l in self.inp_str:
            lst_str.append(l)
            lst_str.append('#')
        lst_str.append('$')
        s = [0] * len(lst_str)
        return self.find_manacher(s,lst_str)

    def find_manacher(self,p,lst_str) :
        n = len(p)
        center = r = 0
        for i in range(1, n - 1):
            flip = 2*center - i  #$
            if i < r:
                p[i] = min(r - i, p[flip])
            while lst_str[i + 1 + p[i]] == lst_str[i - 1 - p[i]]:
                p[i] += 1
            if i + p[i] > r:
                center = i
                r = i + p[i]
        max_len,center=max((val,idx) for idx,val in enumerate(p))
        start=(center-max_len)//2
        return self.inp_str[start:start+max_len]