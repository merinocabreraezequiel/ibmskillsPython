$(document).ready(function(){
    /*
    Datos de conexión con la API
    */
    username='gestor';
    password='ContrasenaSuperSecreta';

    /*
    Llama al función general de carga de tareas
    */
    CargarTareas();

    /*
    Acción para el botón de de registro de tareas
    Valida que los campos se hayan cumplimentado y si no poner valores por defecto
    */
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

    /*
    Carga datos de actualización de titulo y llama la función
    */
    $('#btn_up_tit').click(function() {
        let up_titulo = $('#up_titulo').val();
        let up_id = $('#up_hidden_id').val();

        ActualizarTitulo(up_id, up_titulo);
    });

    /*
    Carga datos de actualización de la descripción y llama la función
    */
    $('#btn_up_desc').click(function() {
        let up_desc = $('#up_descripcion').val();
        let up_id = $('#up_hidden_id').val();

        ActualizarDescripcion(up_id, up_desc);
    });

    /*
    Carga datos de actualización de fecha y llama la función
    */
    $('#btn_up_fecha').click(function() {
        let up_fecha = $('#up_fecha').val();
        let up_id = $('#up_hidden_id').val();

        ActualizarFecha(up_id, up_fecha);
    });

    /*
    Carga datos de actualización de estado y llama la función
    */
    $('#btn_up_estado').click(function() {
        let up_estado= $('#up_estado').val();
        let up_id = $('#up_hidden_id').val();

        ActualizarEstado(up_id, up_estado);
    });

    /*
    Carga datos de id para eliminar y llama a la función
    */
    $('#btn_eliminar').click(function() {
        let up_id = $('#up_hidden_id').val();

        EliminarTarea(up_id);
    });

})