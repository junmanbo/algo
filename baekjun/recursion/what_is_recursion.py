def question(n, ini, ul):
    s1 = '"재귀함수가 뭔가요?"\n'
    s2 = '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n'
    s3 = '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n'
    s4 = '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."\n'

    if n == 0:
        return s1+s2+s3+s4
    elif n == ini:
        return question(n-1, ini, ul) + (ul*n + s1) + ul*n + '"재귀함수는 자기 자신을 호출하는 함수라네"'
    return question(n-1, ini, ul) + (ul*n + s1) + (ul*n + s2) + (ul*n + s3) + (ul*n + s4)


def answer(n, ini, ul):
    a = '라고 답변하였지.\n'

    if n == 0:
        return '라고 답변하였지.'
    return (ul*n + a) + answer(n-1, ini, ul)


ul = '____'
n = int(input())
ini = n
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
print(question(n, ini, ul))
print(answer(n, ini, ul))
