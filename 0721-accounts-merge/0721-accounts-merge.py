class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        adj_list = defaultdict(list)

        for i in range(n):
            for email in accounts[i][1:]:
                adj_list[email].append(i)

        visited = set()
        res = []

        for email in adj_list.keys():
            if email not in visited:
                merged_emails = []
                stack = [email]

                while stack:
                    curr_email = stack.pop()
                    if curr_email not in visited:
                        visited.add(curr_email)
                        for i in adj_list[curr_email]:
                            merged_emails.extend(accounts[i][1:])
                            stack.extend(accounts[i][1:])

                res.append([accounts[i][0]] + sorted(set(merged_emails)))

        return res