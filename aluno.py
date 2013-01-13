#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

class Aluno():
    version =1.2
    def __init__(self,ra,name,curso):
        self.__name=name
        self.__ra=ra
        self.__curso=curso
    def __getRa(self):
	 return self.__ra
    def __setRa(self, ra):
	 try: 
             self.__ra=ra
             return True
         except ValueError:
             print "- Erro: RA inválido"
             return False
    Ra = property(__getRa, __setRa)
    def __getName(self):
	 return self.__name
    def __setName(self, name):
	 try: 
             self.__name=name
             assert name!=""
             return True
         except AssertionError:
             print "- Erro: Name inválido"
             return False
    Name = property(__getName, __setName)
    def __getCurso(self):
	 return self.__curso
    def __setCurso(self, curso):
	 try: 
             self.__curso=curso
             assert curso!=""
             return True
         except AssertionError:
             print "- Erro: Curso inválido"
             return False
    Curso = property(__getCurso, __setCurso)
    
    def mostra(self):
        print "Ra:%4d - Nome:\t%s\t - Curso: %11s"%(self.__ra,self.__name,self.__curso)


