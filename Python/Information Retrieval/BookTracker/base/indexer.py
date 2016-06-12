#! usr/bin/python
#coding: utf-8



import sys
import os, os.path
from whoosh.filedb.filestore import FileStorage
from whoosh.fields import Schema, STORED, ID, KEYWORD, TEXT
from browser import *










def init_index(index=".index"):
	indexZ=index
	if not os.path.exists(indexZ):
		os.mkdir(indexZ)      # os.rmdir(index)
	storage = FileStorage(indexZ)
	schema = Schema(name=TEXT(stored=True),ext=KEYWORD,title=TEXT(stored=True),content=TEXT,path=ID   (stored=True),tags=KEYWORD)
	ix = storage.create_index(schema)
	ix = storage.open_index()
	return ix

 



if __name__ == "__main__" :
 	cpt0=0
	ix=init_index()
	writer = ix.writer()
	regx=build_ext_regx(bk_ext)
	is_book=re.compile(regx)
	lien_de_base=args()
	listZ=rec_browse(is_book,lien_de_base)
	cptZ=len(listZ)
	for x in listZ:
		cpt0+=1
		#print cpt0,":",x
		a=writer.add_document(name=x["name"].decode("utf-8"),path=x["path"].decode("utf-8"),ext=x["ext"].decode("utf-8"))
	writer.commit()	
	print u"\033[0;31m",cptZ,u"\033[mfiles found"
	print "\033[0;31m %d \033[mdocs indexed" % ix.doc_count_all()







		
