#
# @lc app=leetcode id=506 lang=python3
#
# [506] Relative Ranks
#

# @lc code=start
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Sắp xếp danh sách điểm số giảm dần và tạo từ điển ánh xạ
        sorted_score = sorted(score, reverse=True)
        rankings = {sorted_score[i]: str(i + 1) for i in range(len(sorted_score))}
        
        # Xác định xếp hạng tương ứng với từng điểm số
        result = []
        for s in score:
            if rankings[s] == '1':
                result.append("Huy chương vàng")
            elif rankings[s] == '2':
                result.append("Huy chương bạc")
            elif rankings[s] == '3':
                result.append("Huy chương đồng")
            else:
                result.append(rankings[s])
                
        return result1

# @lc code=end

