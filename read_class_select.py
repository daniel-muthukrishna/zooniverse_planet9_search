'''
Reading zoo classification reports and storing in database
'''
import json
import sys
import numpy as np

if __name__ == '__main__':
    #read zooniverse dump
    lines = open('test.txt', 'r').readlines()
    #create dictionary with content
    names=[]
    cands=[]
    n_cands=[]
    for i,line in enumerate(lines):
        js = json.loads(line)
        names.append(js['links']['subjects'][0])
        val=js['annotations'][0]['value']
        if val==0:
            cands.append(True)
            n_cands.append(len(js['annotations'][1]))
        if val==1:
            cands.append(False)
            n_cands.append(0)

    print zip((names, cands, n_cands))

    #list of unique file/image names
    fnames=list(set(names))

    # #lets populate a dictionary ordered by image
    image_dic={}
    for fn in fnames:
        image_dic[fn]={}


    #     print [js[i]['annotations'][0]['value'] for i in range(len(lines))]
    #     image_dic[fn]['n_users_yes']=np.sum([js[i]['annotations'][j]['value'] for i in range(len(lines)) if js[i]['annotations'][j]['value']==1])
    #     image_dic[fn]['n_users_no']=np.sum([js[i]['annotations'][j]['value'] for i in range(len(lines)) if js[i]['annotations'][j]['value']==0])
    #     print fn,image_dic[fn]
        # image_dic[fn]['n_users_yes_n_obj']={}
        # image_dic[fn]['n_users_yes_n_obj'][2]=
        # image_dic[fn]['n_users_yes_n_obj'][3]=
        # image_dic[fn]['n_users_yes_n_obj'][4]=



        # print js[i]['subjects'][0]#.keys()#['metadata']#['user']
        # #reading entries that have 
        # for j in range(len(js[i]['annotations'])):
        #     #3 types of value 0,1,dictionary of coords
        #     val= js[i]['annotations'][j]['value']
        #     if val==0:
        #         print 'no'
        #     elif val==1:
        #         print 'yes'
        #     else:
        #         print 'coords',len(val)
        #         print val

    # f_names = js["name"].keys()

    # #for each sne get classification percentages
    # for f_name in f_names:
    #     ob=fu.Transient.objects.get(byname=f_name)
    #     new_type= get_classification(f_name)
    #     if new_type!=None:
    #         update_type_db(f_name,new_type)
    #     else:
    #         continue
