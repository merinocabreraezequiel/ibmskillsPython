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
                    $('#listadoTareas tbody').append('<tr><td>'+tarea.id+'</td><td>'+tarea.titulo+'</td><td>'+tarea.descripcion+'</td><td>'+tarea.fecha+'</td><td>'+tarea.estado+'</td><td><button onclick="rellenar_actualizador('+tarea.id+')">editar</button></td></tr>');
                }
            }
            tablatareas = jsonresult.tareas;
        },
        error:function(XMLHttpRequest, textStatus, errorThrown){
            console.log('Status: '+textStatus+' Error: '+errorThrown);
        }
    });
    $('html, body').animate({ scrollTop: 0 }, 'slow');
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

function ActualizarTitulo(up_id, up_titulo){
    $.ajax({type:'GET',
        beforeSend: function (xhr){xhr.setRequestHeader("Authorization", "Basic " + btoa(username + ":"+ password));},
        url:'http://127.0.0.1:5000/v1/at/'+up_id+'/'+up_titulo,
        success:function(result){
            CargarTareas(true);
        },
        error:function(XMLHttpRequest, textStatus, errorThrown){
            console.log('Status: '+textStatus+' Error: '+errorThrown);
        }
    });
    limpiar_actualizador();
}

function ActualizarDescripcion(up_id, up_descripcion){
    $.ajax({type:'GET',
        beforeSend: function (xhr){xhr.setRequestHeader("Authorization", "Basic " + btoa(username + ":"+ password));},
        url:'http://127.0.0.1:5000/v1/ad/'+up_id+'/'+up_descripcion,
        success:function(result){
            CargarTareas(true);
        },
        error:function(XMLHttpRequest, textStatus, errorThrown){
            console.log('Status: '+textStatus+' Error: '+errorThrown);
        }
    });
    limpiar_actualizador();
}

function ActualizarFecha(up_id, up_fecha){
    $.ajax({type:'GET',
        beforeSend: function (xhr){xhr.setRequestHeader("Authorization", "Basic " + btoa(username + ":"+ password));},
        url:'http://127.0.0.1:5000/v1/af/'+up_id+'/'+up_fecha,
        success:function(result){
            CargarTareas(true);
        },
        error:function(XMLHttpRequest, textStatus, errorThrown){
            console.log('Status: '+textStatus+' Error: '+errorThrown);
        }
    });
    limpiar_actualizador();
}

function ActualizarEstado(up_id, up_estado){
    $.ajax({type:'GET',
        beforeSend: function (xhr){xhr.setRequestHeader("Authorization", "Basic " + btoa(username + ":"+ password));},
        url:'http://127.0.0.1:5000/v1/ce/'+up_id+'/'+up_estado,
        success:function(result){
            CargarTareas(true);
        },
        error:function(XMLHttpRequest, textStatus, errorThrown){
            console.log('Status: '+textStatus+' Error: '+errorThrown);
        }
    });
    limpiar_actualizador();
}
function EliminarTarea(up_id){
    $.ajax({type:'GET',
        beforeSend: function (xhr){xhr.setRequestHeader("Authorization", "Basic " + btoa(username + ":"+ password));},
        url:'http://127.0.0.1:5000/v1/et/'+up_id,
        success:function(result){
            CargarTareas(true);
        },
        error:function(XMLHttpRequest, textStatus, errorThrown){
            console.log('Status: '+textStatus+' Error: '+errorThrown);
        }
    });
    limpiar_actualizador();
}

function rellenar_actualizador(id_tarea){
    $('#up_titulo').val(tablatareas[id_tarea].titulo);
    $('#up_descripcion').val(tablatareas[id_tarea].descripcion);
    $('#up_fecha').val(tablatareas[id_tarea].fecha);
    _estado ='Pendiente';
    switch (tablatareas[id_tarea].estado){
        case 'Pendiente':
            _estado =0;
            break;
        case 'Completada':
            _estado =1;
            break;
        case 'En Curso':
            _estado =2;
            break;
        case 'Caducada':
            _estado =3;
            break;
        case 'Descartada':
            _estado =4;
            break;
    }
    $('#up_estado').val(_estado);
    $('#up_hidden_id').val(id_tarea);
    $('#up_titulo').focus();
}

function limpiar_actualizador(){
    $('#up_titulo').val('');
    $('#up_descripcion').val('');
    $('#up_fecha').val('');
    $('#up_estado').val('');
    $('#up_hidden_id').val('');
}