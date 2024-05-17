function ConvertToJSON(jsonrecibido){
    jsonobj = JSON.parse(jsonrecibido);
    return jsonobj;
}

function CargarTareas(){
    $.ajax({type:'GET',
        beforeSend: function (xhr){xhr.setRequestHeader("Authorization", "Basic " + btoa(username + ":"+ password));},
        url:'http://127.0.0.1:5000/v1/lt',
        success:function(result){
            jsonresult = ConvertToJSON(result);
            
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
            //jsonresult = ConvertToJSON(result);
        },
        error:function(XMLHttpRequest, textStatus, errorThrown){
            console.log('Status: '+textStatus+' Error: '+errorThrown);
        }
    });
    $('#titulo').val('');
    $('#descripcion').val('');
    $('#fecha').val('');
}