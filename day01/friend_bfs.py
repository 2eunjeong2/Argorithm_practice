# 실습 2 : 그래프 표현 — 딕셔너리로 친구 관계 저장
fr_info = {

    'Summer': ['John', 'Mike', 'Justin'],   # John, Justin, Mike

    'John':   ['Summer', 'Justin'],           # Summer, Justin

    'Justin': ['Summer', 'John', 'Mike', 'May'],  # John, Summer, Mike, May

    'Mike':   ['Summer', 'Justin'],           # Summer, Justin

    'May':    ['Justin', 'Kim'],           # Justin, Kim

    'Kim':    ['May'],                   # May

    'Tom':    ['Jerry'],                   # Jerry

    'Jerry':  ['Tom'],                   # Tom

}

# print("Summer의 친구:", fr_info['Summer'])
# print("May의 친구:", fr_info['May'])

# --------------------------------------------------------------------------------------



# 실습 3: 모든 친구 찾기 — BFS 빈칸 채우기
def print_all_friends(g, start):

    qu = []        # 앞으로 처리해야 할 사람들을 저장하는 큐

    done = []       # 이미 큐에 추가한 사람들을 기록하는 집합 (중복 방지)

    qu.append(start)   # 자신을 큐에 넣고 시작

    done.append(start) # 집합에도 추가

    while qu:           # 큐에 처리할 사람이 남아 있는 동안

        p = qu.pop(0)    # 큐 맨 앞에서 한 명 꺼내기 / 맨 앞 요소를 꺼내려면 pop(0)을 써야 함

        print(p)            # 이름 출력

        for x in g[p]:              # 꺼낸 사람의 친구들 중에서

            if x not in done:     # 아직 처리된 적 없는 사람만 / qu에서 처리된 저 없는 사람 -> done

                qu.append(x)   # 큐에 추가

                done.append(x)    # 집합에도 추가 / 집합 추가 : append

print("=== Summer의 모든 친구 ===")

print_all_friends(fr_info, 'Summer')

print()

print("=== Jerry의 모든 친구 ===")

print_all_friends(fr_info, 'Jerry')
