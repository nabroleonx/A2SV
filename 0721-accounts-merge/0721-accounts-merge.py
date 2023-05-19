class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj_list = defaultdict(list)
        n = len(accounts)

        for i in range(n):
            for email in accounts[i][1:]:
                adj_list[email].append(i)

        visited = set()
        res = []

        def dfs(i, merged_emails):
            if i in visited:
                return

            visited.add(i)

            for email in accounts[i][1:]:
                merged_emails.add(email)

                for j in adj_list[email]:
                    dfs(j, merged_emails)

        for i in range(n):
            if i not in visited:
                merged_emails = set()
                dfs(i, merged_emails)

                if merged_emails:
                    res.append([accounts[i][0]] + sorted(list(merged_emails)))

        return res