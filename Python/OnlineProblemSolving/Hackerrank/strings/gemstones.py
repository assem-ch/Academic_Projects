print len(reduce(set.intersection, [set(raw_input()) for t in xrange(input())]))