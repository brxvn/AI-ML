#### Definición de clase
---
<pre><code>class &ltnombre_de_la_clase&gt (&ltsuper_clase&gt):

	def __init__(self, &ltparams&gt):
		&ltexpresion&gt

	def  &ltnombre_del_metodo&gt (self, &ltparams&gt):
		&ltexpresion&gt</code>
</pre>

Pueden exitir variables publicas y privadas en las clases y en los métodos. Sólo aplica para las variables y metodos en una clase (creo).

**Declaracion de una variable privada:**
Se ocupa un guion bajo antes del nombre de la variable para decir que es privada `_nombre_variable`

 **Declaracion de un método privado:** 
Ocupamos el mismo concepto de las variables privadas y lo aplicamos a los métodos, por ejemplo: `def _mi_metodo_privado()`

Ejemplo de un método privado y una variable privada:
```python
def _nombre_del_metodo_privado(self):
	self._variable_privada = True
```
