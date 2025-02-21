# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution(object):
    def subdomainVisits(self, cpdomains):

        domainCounts = {}
        for entry in cpdomains:
            countStr, domain = entry.split()
            count = int(countStr)
            if domain in domainCounts:
                domainCounts[domain] += count
            else:
                domainCounts[domain] = count
        
        subdomainCounts = {}
        for domain, total in domainCounts.items():
            parts = domain.split('.')
            for i in range(len(parts)):
                subdomain = '.'.join(parts[i:])
                if subdomain in subdomainCounts:
                    subdomainCounts[subdomain] += total
                else:
                    subdomainCounts[subdomain] = total
        
        result = []
        for subdomain, count in subdomainCounts.items():
            result.append(" ".join([str(count), subdomain]))
        
        return result
               