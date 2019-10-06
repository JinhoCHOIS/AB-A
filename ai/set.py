# 과제 1 - set.py

class Set:

    def __init__(self, member = []):
        self.member = member
        for i in self.member:
            if self.member.count(i) != 1:
                self.member.remove(i)

    def append(self, a):
        self.member.append(a)
        for i in range(len(self.member)):
            if (self.member.count(a)) != 1:
                del self.member[i]

    def delete(self, a):
         if a in self.member:
            self.member.remove(a)

    def union(self, s2):
        d = self.member.copy()
        for i in s2.member:
            d.append(i)
        return Set(d)

    def intersection(self, s2):
        l = []
        for i in range(len(self.member)):
            if self.member[i] in s2.member:
                l.append(self.member[i])
        return Set(l)

    def difference(self, s2):
        k = self.member.copy()
        for i in self.member:
            if i in s2.member:
                Set(k).delete(i)
        return Set(k)

    def __add__(self, s2):
        return self.union(s2)

    def __sub__(self, s2):
        return self.difference(s2)

    def __truediv__(self, s2):
        return self.intersection(s2)

# + : union
# - : difference
# / : intersection

a = Set([1, 2, 3])
b = Set([2, 3, 4])

c = a.union(b)
print(c.member)

d = a.difference(b)
print(d.member)

e = a.intersection(b)
print(e.member)

c = a + b
print(c.member)

d = a - b
print(d.member)

e = a / b
print(e.member)