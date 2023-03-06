class TuclaseExamen():    
 def arithmetic_arranger(operaciones, mostrarRespuesta = False):
   
    if len(operaciones) > 5 :
        return "Error: Too many problems."
    else:
       
        parteAlta = ""
        parteBaja = ""
        delimitador = ""
        renglon_respuesta = ""
        problemas_ordenados = ""
        
        for p in operaciones:
            a = p.split()
            alta1 = a[0]
            baja1 = a[-1]
            operador = a[1]
            
         
            if not alta1.isnumeric() or not baja1.isnumeric():
                return "Error: Numbers must only contain digits."
            
           
            if len(alta1) > 4 or len(baja1) > 4:
                return "Error: Numbers cannot be more than four digits."
            
            
            if operador == '+':
                respuesta = int(alta1) + int(baja1)
            elif operador == '-':
                respuesta = int(alta1) - int(baja1)
            else:
                return "Error: Operator must be '+' or '-'."
            
       
            ancho = max(len(baja1),len(alta1)) + 2
            parteAlta += str(alta1).rjust(ancho)
            parteBaja += operador + str(baja1).rjust(ancho - 1)
            delimitador += "-" * ancho
            renglon_respuesta += str(respuesta).rjust(ancho)
            
        
            if operaciones.index(p) < len(operaciones) - 1:
                parteAlta += "    "
                parteBaja += "    "
                delimitador += "    "
                renglon_respuesta += "    "
        
      
        if mostrarRespuesta:
            problemas_ordenados = parteAlta + "\n" + parteBaja + "\n" + delimitador + "\n" + renglon_respuesta
        else:
            problemas_ordenados = parteAlta + "\n" + parteBaja + "\n" + delimitador
        
        return problemas_ordenados

       