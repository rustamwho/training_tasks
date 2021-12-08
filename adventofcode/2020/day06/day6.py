def yes_count(answers):
    return len(set(list(answers)))


def sum_answers():
    yes_answers = 0
    with open("input.txt", "r") as file:
        answers = ""
        for line in file:
            if line != '\n':
                answers += line.strip()
            else:
                yes_answers += yes_count(answers)
                answers = ""
    return yes_answers


def yes_count_part_two(answers):
    persons_count = len(answers)
    if persons_count == 1:
        return len(answers[0])
    answers = list("".join(answers))
    result = [x for x in set(answers) if answers.count(x) == persons_count]
    return len(result)


def sum_answers_part_two():
    yes_answers = 0
    with open("input.txt", "r") as file:
        answers = []
        for line in file:
            if line != '\n':
                answers.append(line.strip())
            else:
                yes_answers += yes_count_part_two(answers)
                answers.clear()
    return yes_answers


print("Anyone YES answers:", sum_answers())
print("Everyone YES answers: ", sum_answers_part_two())
