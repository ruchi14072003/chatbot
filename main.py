#question:answer

qna = {
    "hi":"hey",
    "how are you":"i am fine",
    "what is your name":"my name is ruchi",
    "how old are you":"i am 20 years old",
}

while True:
    qs = input()

    if(qs == "quit"):
        break

    else:
        print(qna[qs])
        