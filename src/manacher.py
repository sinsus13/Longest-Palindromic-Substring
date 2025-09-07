#%%
class Manacher:
    def __init__(self, inp_str: str):
        self.inp_str = inp_str

    def process(self):
        lst_str = ['@', '#']
        for l in self.inp_str:
            lst_str.append(l)
            lst_str.append('#')
        lst_str.append('$')
        self.s = [0] * len(lst_str)
        self.lst_str = lst_str
        return self.find_manacher()

    def find_manacher(self):
        n = len(self.s)
        l = r = 0
        for i in range(1, n - 1):
            flip = l + r - i  #$
            # o1 = self.check(l, r)
            # if o1:
            #     return o1
            if i < r:
                self.s[i] = min(r - i, self.s[flip])
            #start from idx 2
            while self.lst_str[i + 1 + self.s[i]] == self.lst_str[i - 1 - self.s[i]]:
                self.s[i] += 1
            if i + self.s[i] > r:
                #reverse when over bound
                l = i - self.s[i]
                r = i + self.s[i]
        max_len,center=max((val,idx) for idx,val in enumerate(self.s))
        start=(center-max_len)//2 #2*c-i to original
        return self.inp_str[start:start+max_len]
    #2*c-i
    #traversing whole string even=s[cen] odd=s[cen+1]
    # def check(self, l, r):
    #     n = r - l + 1
    #     c = (l + r) // 2
    #     if n % 2 == 0:
    #         odd = 0
    #     else:
    #         odd = 1
    #     j = 2 * c + 2 + odd
    #     return n<= j
