$(document).ready(function(){
    username='gestor';
    password='ContrasenaSuperSecreta';
    CargarTareas();

    $('#btn_registro_tarea').click(function() {
        const titulo = $('#titulo').val();
        const descripcion = $('#descripcion').val();
        const fecha = $('#fecha').val();

        NuevaTarea(titulo, descripcion, fecha);
    });

})