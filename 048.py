def check_str(s: str) -> bool:
        for i in range(len(s)):
            if s[i] in s[i+1:]:
                return False
        return True
def force(s: str) -> int:
        m=0
        if s != "":
            m=1
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i] != s[j]:
                    if check_str(s[i:j+1]):
                        m = max(m,len(s[i:j+1]))
        return m
    
N = input()
print(force(N))