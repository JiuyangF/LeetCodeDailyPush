def letterCasePermutation(S):
    """
    :type S: str
    :rtype: List[str]
    """
    answers = [S]
    num_set = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    for i in range(len(S)):
        if S[i] in num_set:
            continue

        for one in answers[:]:
            if S[i].isupper():
                answers.append(one[:i] + one[i].lower() + one[i + 1:])
            elif S[i].islower():
                answers.append(one[:i] + one[i].upper() + one[i + 1:])
    print(answers)
    return answers


num_set = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')

answers = []


def letter_case_recursion(i, S):
    if i >= len(S) - 1:
        return
    for j in range(i, len(S)):
        if S[j] in num_set:
            continue
        answers.append(S)
        if S[j].isupper():
            answers.append(S[:i] + S[i].lower() + S[i + 1:])
            letter_case_recursion(i + 1, S)
        elif S[j].islower():
            answers.append(S[:i] + S[i].upper() + S[i + 1:])
            letter_case_recursion(j + 1, S)


if __name__ == '__main__':
    letterCasePermutation('78y9hj')
    letter_case_recursion(0,'78y9hj')
    print(answers)
