'''
활용예시
- 웹 브라우저 뒤로가기 (방문기록)
- 함수 호출 
- DFS
''' 
stack = []
stack.append('A') # push A -> ['A'] 
stack.append('B') # push B -> ['A', 'B']
stack.append('C') # push C -> ['A', 'B', 'C']
print(stack.pop()) # -> 'C'
print(stack.pop()) # -> 'B'