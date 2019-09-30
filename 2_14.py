from linked_slist import Slist

def double_(class1, class2):
    class1_leng = class1.length()
    class2_leng = class2.length()
    result_Slist = Slist()
    result_Slist.insert_front('head')  # 들어온 객체와 똑같이 형식 맞춰주기 위해 'head' 삽입
    result_head = result_Slist.head

    i = class1_leng
    j = class2_leng

    refer1 = class1.head                # 각 'head'
    refer2 = class2.head

    while (i != 1) and (j != 1):        # 객체에서 요소가 하나가 될 때까지
        if (abs(i - j) != 0):           # 만약 두 객체의 길이가 다르다면
            if i > j:                   # i가 더 크면 더 큰 자리수에 있는 수를 컨트롤 하기 위해
                i -= 1
                result_Slist.insert_after(refer1.next.item, result_head)    # 더하기를 위해 쓰이지 않는 앞의 숫자들은 새로운 객체 앞으로 먼저 넣음
                refer1 = refer1.next
                result_head = result_head.next
            else:
                j -= 1
                result_Slist.insert_after(refer2.next.item, result_head)
                refer2 = refer2.next
                result_head = result_head.next
            continue


        values_sum = refer1.next.item + refer2.next.item    # 값 더한 후 저장
        if (values_sum > 100):                              # 올림 값 추출
            if result_head.item == 'head':                  # 앞이 숫자가 아니라 head일 경우
                result_head.item = 1                        # 값을 1로 저장
            else:
                result_head.item += 1                       # 1을 더해줌
            values_sum -= 100
        result_Slist.insert_after(values_sum, result_head)  # 해당 값 연결리스트에 추가
        refer1 = refer1.next
        refer2 = refer2.next
        result_head = result_head.next                      # 다음 숫자로 넘어가기
        i -= 1
        j -= 1

    return result_Slist.print_list()





s = Slist()
s.insert_front(22)
s.insert_front(0)
s.insert_front(1)
s.insert_front('head')
s.print_list()
e = Slist()
e.insert_front(88)
e.insert_front(99)
e.insert_front(99)
e.insert_front(2)
e.insert_front('head')
e.print_list()
double_(s, e)
