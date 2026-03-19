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

    done = set()       # 이미 큐에 추가한 사람들을 기록하는 집합 (중복 방지)

    qu.append(start)   # 자신을 큐에 넣고 시작

    done.add(start) # 집합에도 추가

    while qu:           # 큐에 처리할 사람이 남아 있는 동안

        p = qu.pop(0)    # 큐 맨 앞에서 한 명 꺼내기 / 맨 앞 요소를 꺼내려면 pop(0)을 써야 함

        print(p)            # 이름 출력

        for x in g[p]:              # 꺼낸 사람의 친구들 중에서

            if x not in done:     # 아직 처리된 적 없는 사람만 / qu에서 처리된 적 없는 사람 -> done

                qu.append(x)   # 큐에 추가

                done.add(x)    # 집합에도 추가 / 집합 추가 : append

print("=== Summer의 모든 친구 ===")

print_all_friends(fr_info, 'Summer')

print()

print("=== Jerry의 모든 친구 ===")

print_all_friends(fr_info, 'Jerry')

# -------------------------------------------------------------------------------

# 실습 4: 관찰 — Tom과 Jerry는 왜 무한 반복이 안 될까?
def print_all_friends_broken(g, start):

    qu = []

    # done 없이 실행 — 무한 반복 발생!

    qu.append(start)

    count = 0

    while qu and count < 20:   # 무한 루프 방지를 위해 20번만 실행

        p = qu.pop(0)

        print(p)

        for x in g[p]:

            qu.append(x)       # 중복 체크 없이 그냥 추가

        count += 1

print("=== done 없이 실행 (20번 제한) ===")

print_all_friends_broken(fr_info, 'Tom')

# 질문 4-1 : 어떤 이름이 계속 반복되나요? 
# 답 : Tom, Jerry

# 질문 4-2 : done 집합은 어떤 역할을 하나요?
# 답 : 중복 방지 역할

# 질문 4-3 : 로봇 경로 탐색에서 done에 해당하는 것은?
# 답 : 로봇이 이미 탐색한 위치 목록
#      move_base 패키지안의 Closed List와 같은 역할을 함
