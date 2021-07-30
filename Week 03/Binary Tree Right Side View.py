class Solution:
	def rightSideView(self, root: TreeNode) -> List[int]:
		if not root:
			return []
		q1 = [root]
		q2 = []

		ans = []
		while q1:
			ans.append(q1[-1].val)
			for node in q1:
				if node.left:
					q2.append(node.left)
				if node.right:
					q2.append(node.right)
			q1, q2 = q2, []

		return ans