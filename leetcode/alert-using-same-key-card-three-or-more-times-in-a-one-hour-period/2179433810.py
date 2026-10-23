class Solution:
    def alertNames(self, keyName: list[str], keyTime: list[str]) -> list[str]:
        d = {}
        for name, time in zip(keyName, keyTime):
            h, m = map(int, time.split(":"))
            if name in d:
                d[name].append(h*60+m)
            else:
                d[name] = [h*60+m]

        ans = []
        
        for name, arr in d.items():
            arr.sort()
            for i in range(2, len(arr)):
                if arr[i]-arr[i-2]<=60:
                    if name not in ans:
                        ans.append(name)
        return sorted(ans)

