let tablatareas;

function ConvertToJSON(jsonrecibido){
    jsonobj = JSON.parse(jsonrecibido);
    return jsonobj;
}

function CargarTareas(limpiar=false){
    $.ajax({type:'GET',
        beforeSend: function (xhr){xhr.setRequestHeader("Authorization", "Basic " + btoa(username + ":"+ password));},
        url:'http://127.0.0.1:5000/v1/lt',
        success:function(result){
            jsonresult = ConvertToJSON(result);
            console.log(jsonresult);
            console.log(Object.keys(jsonresult.tareas).length);
            if(limpiar){$('#listadoTareas tbody').html('');}
            for(let item in jsonresult.tareas){
                if (jsonresult.tareas.hasOwnProperty(item)) {
                    let tarea = jsonresult.tareas[item];
                    $('#listadoTareas tbody').append('<tr><td>'+tarea.titulo+'</td><td>'+tarea.descripcion+'</td><td>'+tarea.fecha+'</td><td>'+tarea.estado+'</td><td><button onclick="rellenar_actualizador('+tarea.id+')">editar</button></td></tr>');
                }
            }
            tablatareas = jsonresult.tareas;
        },
        error:function(XMLHttpRequest, textStatus, errorThrown){
            console.log('Status: '+textStatus+' Error: '+errorThrown);
        }
    });
}

function NuevaTarea(titulo, descripcion, fecha){
    $.ajax({type:'GET',
        beforeSend: function (xhr){xhr.setRequestHeader("Authorization", "Basic " + btoa(username + ":"+ password));},
        url:'http://127.0.0.1:5000/v1/nt/'+titulo+'/'+descripcion+'/'+fecha,
        success:function(result){
            CargarTareas(true);
        },
        error:function(XMLHttpRequest, textStatus, errorThrown){
            console.log('Status: '+textStatus+' Error: '+errorThrown);
        }
    });
    $('#titulo').val('');
    $('#descripcion').val('');
    $('#fecha').val('');
}

function rellenar_actualizador(id_tarea){
    $('#up_titulo').val(tablatareas[id_tarea].titulo);
    $('#up_descripcion').val(tablatareas[id_tarea].descripcion);
    $('#up_fecha').val(tablatareas[id_tarea].fecha);
    $('#up_estado').val(tablatareas[id_tarea].estado);
    $('#up_hidden_id').val(id_tarea);
    $('#up_titulo').focus();
}