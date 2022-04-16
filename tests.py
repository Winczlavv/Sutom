l="coucou"
l= l[:0]+l[1:]
print(l)




#  BOUCLE EFFECTUEE; NON VERIFIEE

            #     if C[s][0]==C[j][0]:
            #         countletters+=1

            # if countletters==1:
            #     for m in range(len(X)):
            #         if int(X[m][1])==1:
            #             wo = X[m][0]
            #             if C[j][0] in wo:
            #                 X[m][1] = 0
            # else:
            #     for o in range(len(C)):
            #         if C[o][0] == C[j][0]:
            #            D.append([C[o][0],int(C[o][1]),int(o)])
            #     if 1 not in D and 2 not in D:
            #         for v in range(len(X)):
            #             if int(X[v][1])==1:
            #                 wo = X[v][0]
            #                 if C[j][0] in wo:
            #                     X[v][1] = 0
            #     else:
            #         T = X.copy()
            #         for c in range(len(D)):
            #             if D[c][1]==2:
            #                 for d in range(len(T)):
            #                     wo= T[d][0]
            #                     pl = D[c][2]
            #                     wo[pl] = wo[:pl] + wo[pl+1:]
            #         counterone = 0
            #         counterspeclet = 0
            #         for e in range(len(D)):
            #             if D[e][2]==1:
            #                 counterone+=1
            #         for f in range(len(T)):
            #             wo = T[f][0]
            #             for g in range(len(wo)):
            #                 if wo[g]==C[j][0]:
            #                     counterspeclet+=1
            #             if counterspeclet != counterone:
            #                 X[f][1]==0
                            # else:
                            #     countletters = 0
                            #     D = []
                            #     for s in range(len(C)):
