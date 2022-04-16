word = str(input())
double_word = ""
for i in range(len(word)):
    double_word = word[i] + word[i]
    print(double_word, end="")