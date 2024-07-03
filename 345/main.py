def main(s):
	c = s.find('c')
	w1 = s[(c + 1):].find('w')
	w2 = s[(c + w1 + 2):].find('w')
	if c != -1 and w1 != -1 and w2 != -1:
		cww = w1 + w2 + 3
	else:
		cww = 101
	if s[(c + 1):].find('c') == -1:
		return cww
	else:
		return min(cww, cfind(s[(c + 1):]))
	
ans = cfind(input())
print(ans) if ans != 101 else print(-1)

if __name__ == "__main__":
    main()