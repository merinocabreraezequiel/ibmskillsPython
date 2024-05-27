let tablatareas;

function ConvertToJSON(jsonrecibido){
    /*
    Simple aplicación para no tener qeu estar llamando a la función json.parse insistentemetne.
    */
    jsonobj = JSON.parse(jsonrecibido);
    return jsonobj;
}

function CargarTareas(limpiar=false){
    /*
    Llama a la API para cargar la lista de tareas.
    Elimina la lista previa
    Crea el nuevo cuerpo de tabla con los datos cargados
    Realiza una animación para mostrar la web desde arriba en caso de estar fuera de pantalla
    */
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
    /*
    Crea una nueva tarea en base a los campos que recibe y recarga la lista de tareas
    */
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
    /*
    Llama a la API con el ID  y el titulo para actualizar y llama a la función de limpieza del editor
    */
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
    /*
    Llama a la API con el ID  y la descripción para actualizar y llama a la función de limpieza del editor
    */
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
    /*
    Llama a la API con el ID  y la fecha para actualizar y llama a la función de limpieza del editor
    */
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
    /*
    Llama a la API con el ID  y el estado para actualizar y llama a la función de limpieza del editor
    */
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
    /*
    Llama a la API con el ID para elimiar el registro y llama a la función de limpieza del editor
    */
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
    /*
    Carga los datos de la tarea a editar mediante el ID
    Convierte el numero de estado por el texto
    Focusea en el texto para empezar a editar
    Muestra el panel de edición
    */
    $('#editartarea').css('display','block');
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
    /*
    Borra los valores de los campos de actualización y oculta el panel
    */
    $('#up_titulo').val('');
    $('#up_descripcion').val('');
    $('#up_fecha').val('');
    $('#up_estado').val('');
    $('#up_hidden_id').val('');
    $('#editartarea').css('display','none');
}