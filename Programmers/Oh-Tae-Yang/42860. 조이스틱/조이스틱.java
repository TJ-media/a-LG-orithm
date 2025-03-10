class Solution {
    public int solution(String name) {
        int answer = 0;
        int length = name.length();

        int idx; //다음 값 확인에 사용
        int move = length - 1; //좌우 움직임 수를 체크

        for (int i = 0; i < name.length(); i++) {
            answer += Math.min(name.charAt(i) - 'A', 'Z' - name.charAt(i) + 1);

            idx = i + 1;

            while (idx < length && name.charAt(idx) == 'A') {
                idx ++;
            }

            move = Math.min(move, i * 2 + length - idx);
            move = Math.min(move, (length - idx) * 2 + i);
        }
        answer += move;
        return answer;
    }
}