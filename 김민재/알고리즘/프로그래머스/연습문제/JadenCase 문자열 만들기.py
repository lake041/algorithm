def solution(s):
    ans = ""
    save = ""
    for char in s:
        if char == " ":
            ans += save
            ans += " "
            save = ""
        else:
            save += char.upper() if save == "" else char.lower()
    ans += save

    return ans