from .binary_search import BST

# height <= 1.44 log n


class AVL(BST):
    def insert(self, k):    # height 조건이 깨지면 조치를 취해야 함 > O(log n)
        v = super(AVL, self).insert(k)
        '''
        v에서부터 올라가면서 height 업데이트
        heigth 뺀 절댓값이 2 이상이 나오면 rotate
        균형이 처음으로 깨진 노드가 z 다음 y, x
        z - y - x의 관계에 따라 3가지 경우
        1. z right y left x > height 2
            - y에서 right rotate > z right x right z > height 2
            - z에서 left rotate > 부모 x 자식 left z right y > height 1 
                    
        2. z left y right x > height 2
            - y에서 left rotate > z left y left x > height 2
            - z에서 right rotate > 부모 x 자식 left y right z > height 0
        
        결국 z y x의 방향이 다르면 rotate를 2번해야됨    
        
        3. z left y left x > height 2
            - z에서 right rotate > 부모 y 자식 left x right z > hegith 1

            
        따라서 insert <= 2 rotations --> O(log n)
        
        '''

        pass

    def delete(self, x):    # x는 노드
        v = super(AVL, self).deleteByCopying(x) # 실제로 지워진 노드나 height가 처음으로 영향받는 노드를 리턴 받는다. m이 height가 처음으로 영향받음
        v = super(AVL, self).deleteByMerging(x) # m의 부모 노드가 height 처음으로 영향 받음
        ''' 위의 부분 주석 다시 한번 살펴보기, 교수님이 서로 바꿔서 설명한거 같음'''

        """
        처음으로 균형 깨진 노드 z
        지운 쪽이 가벼워지니깐 반대 방향에서 rotate 해줘야한다.
        y는 z의 자식 중 무거운 쪽, x는 y의 자식중 무거운 쪽
        
        z - y - x
        1. 같은 방향으로 연결 되어 있을 경우
            - z에서 rotate > 부모 y 자식 left x, right z
            - z의 부모의 다른 자식 쪽과 height 차이가 2 이상이 생길 수 있음 >
            
        2. 다른 방향으로 연결 되어 있을 경우
            -  rotate 2번 해줘야 함
            
        이 과정을 root 노드까지 올라가면서 계속 해줘야함
        
         delete      조정      최종 시간
        O(log n) + O(log n) = O(log n)      
        
        """