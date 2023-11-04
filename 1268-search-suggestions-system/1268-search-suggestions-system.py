class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        n = len(searchWord)
        products.sort()
        
        letter_to_products = defaultdict(list)
        
        for i in range(n):
            seg = searchWord[:i+1]
            temp = []
            for product in products:
                if product[:i+1] == seg and len(temp) < 3:
                    temp.append(product)
            
            letter_to_products[seg] = temp

        return [v for k, v in letter_to_products.items()]