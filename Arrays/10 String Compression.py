class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        index = 0
        suma = 1
        for i in range(0, len(chars)):            
            if i == len(chars) - 1:
                out = 1
            else:
                if chars[i] != chars[i+1]:
                    out = 1
                else:
                    suma = suma + 1
                    out = 0
            if out == 1:
                chars[index] = chars[i]
                if suma == 1:
                    index = index + 1
                elif suma < 10:
                    chars[index + 1] = str(suma)
                    index = index + 2
                elif suma >= 10 and suma < 99: 
                    dec = suma // 10
                    res = suma % 10
                    chars[index + 1] = str(dec)
                    chars[index + 2] = str(res)
                    index = index + 3
                elif suma >= 100 and suma < 999: 
                    cien = suma // 100
                    resCien = suma % 100
                    dec = resCien // 10
                    res = resCien % 10
                    chars[index + 1] = str(cien)
                    chars[index + 2] = str(dec)
                    chars[index + 3] = str(res)
                    index = index + 4
                elif suma >= 999 and suma < 9999: 
                    mil = suma // 1000
                    resMil = suma % 1000
                    cien = resMil // 100
                    resCien = resMil % 100
                    dec = resCien // 10
                    res = resCien % 10
                    chars[index + 1] = str(mil)
                    chars[index + 2] = str(cien)
                    chars[index + 3] = str(dec)
                    chars[index + 4] = str(res)
                    index = index + 5
                suma = 1
        return index