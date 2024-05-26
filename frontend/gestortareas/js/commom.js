$(document).ready(function(){
    username='gestor';
    password='ContrasenaSuperSecreta';
    CargarTareas();

    $('#btn_registro_tarea').click(function() {
        let titulo = $('#titulo').val();
        let descripcion = $('#descripcion').val();
        let fecha = $('#fecha').val();

        if(titulo==''){titulo='Sin título';}
        if(descripcion==''){descripcion='Sin descripción';}
        if(fecha==''){
            var date = new Date();
            var day = date.getDate();
            var month = date.getMonth() + 1;
            var year = date.getFullYear();
            if (month < 10) month = "0" + month;
            if (day < 10) day = "0" + day;
            fecha = year + "-" + month + "-" + day; 
        }

        NuevaTarea(titulo, descripcion, fecha);
    });

    $('#btn_up_tit').click(function() {
        let up_titulo = $('#up_titulo').val();
        let up_id = $('#up_hidden_id').val();

        ActualizarTitulo(up_id, up_titulo);
    });

    $('#btn_up_desc').click(function() {
        let up_desc = $('#up_descripcion').val();
        let up_id = $('#up_hidden_id').val();

        ActualizarDescripcion(up_id, up_desc);
    });

    $('#btn_up_fecha').click(function() {
        let up_fecha = $('#up_fecha').val();
        let up_id = $('#up_hidden_id').val();

        ActualizarFecha(up_id, up_fecha);
    });

    $('#btn_up_estado').click(function() {
        let up_estado= $('#up_estado').val();
        let up_id = $('#up_hidden_id').val();

        ActualizarEstado(up_id, up_estado);
    });

    $('#btn_eliminar').click(function() {
        let up_id = $('#up_hidden_id').val();

        EliminarTarea(up_id);
    });

})