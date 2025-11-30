class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ball,move = 0,0
        resu = [0] * len(boxes)
        for i in range(len(boxes)):
            resu[i] += ball+move
            move += ball
            ball += int(boxes[i])
        ball,move = 0,0
        for i in range(len(boxes)-1,-1,-1):
            resu[i] += ball+move
            move += ball
            ball += int(boxes[i])
        return resu

        