import sys
import http.client


def do_request(headers):
    conn = http.client.HTTPConnection('127.0.0.1', 7777)
    conn.request('MEW', '', headers=headers)
    response = conn.getresponse()
    heads = response.headers.get_all('x-cat-value')
    return heads


def get_result(variables):
    known = {x: None for x in variables}

    if len(set(variables)) != len(variables):
        for variable in known.keys():
            headers = {'x-cat-variable': variable}
            value = do_request(headers)[0]
            known[variable] = value
        return [known[x] for x in variables]

    headers = {'x-cat-variable': ', '.join(x for x in variables[:3])}
    first_response = do_request(headers)

    headers = {'x-cat-variable': ', '.join(x for x in variables[2:])}
    second_response = do_request(headers)
    know = None
    for a in second_response:
        for b in first_response:
            if a == b:
                know = a
                second_response.remove(a)
                first_response.remove(a)
                break
    known[variables[2]] = know
    known[variables[3]] = second_response[0]

    unknowns = [x for x, y in known.items() if y is None]
    help = unknowns[0]
    unknown = unknowns[1]
    headers = {'x-cat-variable': help}
    third_response = do_request(headers)
    for a in third_response:
        for b in first_response:
            if a == b:
                know = a
                first_response.remove(a)
                break
    known[help] = know
    known[unknown] = first_response[0]
    return [x for x in known.values()]


def read_variables():
    variables = []
    for _ in range(4):
        variables.append(sys.stdin.readline().strip())
    return variables


if __name__ == '__main__':
    variables = read_variables()
    results = get_result(variables)
    for res in results:
        print(res)
