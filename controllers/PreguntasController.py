# -*- coding: utf-8 -*-
# intente algo como
from gluon.serializers import json
def index():
   	response.view='PreguntasController/index.html'
   	return dict()
	
def seleccionar_pregunta():
	respuesta={}
	resultado=[] #lista que almacenara el diccionario de categoria,pregunta y respuesta
	resul_categoria = db.executesql('SELECT id,descripcion FROM categorias ORDER BY RAND() LIMIT 1')
	for row in resul_categoria:
 		categoria = {'idCat': row[0], 'descCat': row[1]}
 
	resul_pregunta = db.executesql('SELECT id,descripcion,imagen FROM preguntas WHERE idcat='+ str(categoria['idCat']) +' ORDER BY RAND() LIMIT 1')
	for row in resul_pregunta:
	 	pregunta = {'idPreg': row[0], 'descPreg': row[1], 'imagen':row[2]}


	resul_respuesta=db.executesql('SELECT id,descripcion FROM RESPUESTAPREGUNTAS WHERE idPreg='+str(pregunta['idPreg']))
	x=0
	for row in resul_respuesta:
	 	respuesta['idResp'+str(x)] = row[0] 
	 	respuesta['descResp'+str(x)] = row[1]
	 	x=x+1

 	resultado.append(categoria)
 	resultado.append(pregunta)
 	resultado.append(respuesta)
 
 	return response.json(resultado)


def verificar_respuesta():
	idPreg= request.vars.idPreg
	resp_usuario= request.vars.resp

	opcion=db.executesql('SELECT descripcion from respuestapreguntas WHERE opcion="V" AND idPreg='+str(idPreg))
	for resp in opcion:
		if str(resp[0])==resp_usuario:
			respuesta='V'
		else:
			respuesta='F'

 	return (respuesta)

def indexCarga():
	response.view='PreguntasController/indexCarga.html'
   	return dict()

def cargarPreg():
	datos = request.post_vars
	db.preguntas.insert(descripcion=datos.desc,idCat=datos.cat,imagen=datos.img)
	idpreg = db.executesql('SELECT max(id) from preguntas')
	for preg in idpreg:
		db.respuestapreguntas.insert(id=1,idPreg=preg[0],descripcion=datos.resp1,opcion=datos.opcion1)
		db.respuestapreguntas.insert(id=2,idPreg=preg[0],descripcion=datos.resp2,opcion=datos.opcion2)
		db.respuestapreguntas.insert(id=3,idPreg=preg[0],descripcion=datos.resp3,opcion=datos.opcion3)
	return dict()


	









